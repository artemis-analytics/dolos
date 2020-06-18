#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2019.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test protobuf model implementation
"""

import unittest
import tempfile
import uuid
import logging
import io
import csv

# from collections import OrderedDict
from artemis_format.pymodels.table_pb2 import Table
from artemis_format.pymodels.cronus_pb2 import TableObjectInfo
from dolos.recordbatchgen import RecordBatchGen

logging.getLogger().setLevel(logging.INFO)


class RBGenTestCase(unittest.TestCase):
    def setUp(self):
        print("================================================")
        print("Beginning new TestCase %s" % self._testMethodName)
        print("================================================")

    def test_rbgen_csv(self):
        """
        This method generates a test
        record batch as a CSV, and displays
        the results to the console.
        """
        # define the schema for the data
        g_table = Table()  # Define a table instance
        g_table.name = "EvolveModel"  # Name the table
        g_table.uuid = str(uuid.uuid4())  # Create a UUID
        schema = g_table.info.schema.info  # Access the schema unit

        field = schema.fields.add()  # Add a field
        field.name = "Name"  # Set the field name
        field.info.type = "float"  # Set the type of the field
        field.info.length = 10  # Set the field length
        field.info.aux.generator.name = "normal"  # Generator name, we need to trace this
        
        """
        # We're adding in the parameters here. These mimic the tests that are found in the ArtemisFaker module itself
        params = field.info.aux.generator.parameters.add()
        params.name = "Mean"
        params.value = 3
        params.type = "int"

        params2 = field.info.aux.generator.parameters.add()
        params2.name = "STD"
        params2.value = 3
        params2.type = "int"
        """
        g_table_msg = g_table.SerializeToString()  # Create a string instance of this

        # This is the record batch generator
        # All the configurations are set in the
        # generator to produce the output.
        generator = RecordBatchGen(
            "generator",  # Unknown parameter
            nbatches=1,  # Total number of batches that are used
            num_rows=10,  # Total rows to be generated
            file_type=1,  # Encodes the data as csv
            table_id=g_table.uuid,  # Sets the table UUID
            table_msg=g_table_msg,  # Sets the table message
        )

        generator.initialize()  # Create the generator
        # Data returned as a pyarrow buffer
        # Convert to raw python bytes objects
        # Use io wrapper and read as csv
        for batch in generator:  # Generator is some kind of iterator
            data = batch.to_pybytes()  # Access the batch, convert to bytes
            # Create a text output, this turns it into a string
            with io.TextIOWrapper(io.BytesIO(data)) as textio:
                for row in csv.reader(textio):  # Spit out the row in the buffer
                    print(row)  # Print the row


if __name__ == "__main__":
    unittest.main()  # Execute the unit tests

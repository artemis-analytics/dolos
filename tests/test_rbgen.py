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

# from collections import OrderedDict
from cronus.core.cronus import BaseObjectStore
from artemis_format.pymodels.table_pb2 import Table
from artemis_format.pymodels.cronus_pb2 import TableObjectInfo
from dolos.recordbatchgen import RecordBatchGen


logging.getLogger().setLevel(logging.INFO)


class RBGenTestCase(unittest.TestCase):
    def setUp(self):
        print("================================================")
        print("Beginning new TestCase %s" % self._testMethodName)
        print("================================================")

    def test_rbgen(self):
        with tempfile.TemporaryDirectory() as dirpath:
            store = BaseObjectStore(dirpath, "artemis")

            g_dataset = store.register_dataset()
            store.new_partition(g_dataset.uuid, "generator")
            job_id = store.new_job(g_dataset.uuid)

            # define the schema for the data
            g_table = Table()
            g_table.name = "EvolveModel"
            g_table.uuid = str(uuid.uuid4())
            schema = g_table.info.schema.info
            field = schema.fields.add()
            field.name = "Name"
            field.info.type = "String"
            field.info.length = 10
            field.info.aux.generator.name = "name"

            tinfo = TableObjectInfo()
            store.register_content(
                g_table,
                tinfo,
                dataset_id=g_dataset.uuid,
                job_id=job_id,
                partition_key="generator",
            )

            generator = RecordBatchGen(
                "generator",
                nbatches=1,
                num_rows=10000,
                file_type=1,
                table_id=g_table.uuid,
            )

            generator.initialize()
            for batch in generator:
                print(batch)


if __name__ == "__main__":
    unittest.main()

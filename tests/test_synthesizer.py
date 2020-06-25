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
import logging

from artemis_format.pymodels.table_pb2 import Table
from dolos.simutable.synthesizer import Synthesizer


logging.getLogger().setLevel(logging.INFO)


class SynthesizerTestCase(unittest.TestCase):
    def setUp(self):
        print("================================================")
        print("Beginning new TestCase %s" % self._testMethodName)
        print("================================================")

    def test(self):
        model = Table()
        model.name = "EvolveModel"
        schema = model.info.schema.info
        field = schema.fields.add()
        field.name = "Name"
        field.info.type = "String"
        field.info.length = 10
        field.info.aux.generator.name = "name"
        print(model)

    def test_gen_from_proto(self):

        model = Table()
        model.name = "EvolveModel"
        schema = model.info.schema.info
        field = schema.fields.add()
        field.name = "Name"
        field.info.type = "String"
        field.info.length = 10
        field.info.aux.generator.name = "name"

        s2 = Synthesizer(model,   seed=4053)
        print(s2.generate())

    def test_glm_proto(self):
        model = Table()
        schema = model.info.schema.info
        field1 = schema.fields.add()
        field1.name = "Value1"
        field1.info.type = "Float"
        field1.info.length = 10
        field1.info.aux.generator.name = "random_int"
        field1.info.aux.dependent = "Prediction"

        field2 = schema.fields.add()
        field2.name = "Value2"
        field2.info.type = "Float"
        field2.info.length = 10
        field2.info.aux.generator.name = "random_int"
        field2.info.aux.dependent = "Prediction"

        field3 = schema.fields.add()
        field3.name = "Prediction"
        field3.info.type = "Float"
        field3.info.length = 10
        field3.info.aux.generator.name = "glm"

        beta1 = field3.info.aux.generator.parameters.add()
        beta1.name = "beta1"
        beta1.value = 10
        beta1.type = "int"
        beta2 = field3.info.aux.generator.parameters.add()
        beta2.name = "beta2"
        beta2.value = 0.1
        beta2.type = "float"
        beta3 = field3.info.aux.generator.parameters.add()
        beta3.name = "beta3"
        beta3.value = 100
        beta3.type = "int"
        sigma = field3.info.aux.generator.parameters.add()
        sigma.name = "sigma"
        sigma.value = 1
        sigma.type = "int"

        var1 = field3.info.aux.generator.parameters.add()
        var1.name = "Value1"
        var1.type = "Field"
        var1.variable.CopyFrom(field1)

        var2 = field3.info.aux.generator.parameters.add()
        var2.name = "Value2"
        var2.type = "Field"
        var2.variable.CopyFrom(field2)

        s2 = Synthesizer(model)
        print(s2.generate())

    def test_xduplicates(self):

        model = Table()

        model.info.aux.duplicate.probability = 1
        model.info.aux.duplicate.distribution = "uniform"
        model.info.aux.duplicate.maximum = 1
        schema = model.info.schema.info

        field1 = schema.fields.add()
        field1.name = "record_id"
        field1.info.type = "String"
        field1.info.length = 10

        field2 = schema.fields.add()
        field2.name = "Name"
        field2.info.type = "String"
        field2.info.length = 10
        field2.info.aux.generator.name = "name"

        field3 = schema.fields.add()
        field3.name = "UPC"
        field3.info.type = "Integer"
        field3.info.length = 13
        field3.info.aux.generator.name = "ean"

        parm = field3.info.aux.generator.parameters.add()
        parm.name = "ndigits"
        parm.value = 13
        parm.type = "int"

        s2 = Synthesizer(model,   seed=4053)
        print(s2.generate())

    def test_xmodifer(self):

        model = Table()
        schema = model.info.schema.info

        field1 = schema.fields.add()
        field1.name = "record_id"
        field1.info.type = "String"
        field1.info.length = 10

        field2 = schema.fields.add()
        field2.name = "Name"
        field2.info.type = "String"
        field2.info.length = 10
        field2.info.aux.generator.name = "name"

        field3 = schema.fields.add()
        field3.name = "SIN"
        field3.info.type = "String"
        field3.info.length = 10
        field3.info.aux.generator.name = "ssn"

        field4 = schema.fields.add()
        field4.name = "StreetNumber"
        field4.info.type = "String"
        field4.info.length = 40
        field4.info.aux.generator.name = "building_number"

        field5 = schema.fields.add()
        field5.name = "Street"
        field5.info.type = "String"
        field5.info.length = 40
        field5.info.aux.generator.name = "street_name"

        field6 = schema.fields.add()
        field6.name = "City"
        field6.info.type = "String"
        field6.info.length = 40
        field6.info.aux.generator.name = "city"

        field7 = schema.fields.add()
        field7.name = "Province"
        field7.info.type = "String"
        field7.info.length = 40
        field7.info.aux.generator.name = "province"

        field8 = schema.fields.add()
        field8.name = "PostalCode"
        field8.info.type = "String"
        field8.info.length = 40
        field8.info.aux.generator.name = "postcode"

        field9 = schema.fields.add()
        field9.name = "DOB"
        field9.info.type = "DateTime"
        field9.info.length = 40
        field9.info.aux.generator.name = "date"

        field10 = schema.fields.add()
        field10.name = "PhoneNum"
        field10.info.type = "String"
        field10.info.length = 11
        field10.info.aux.generator.name = "phone_number"

        model.info.aux.duplicate.probability = 1
        model.info.aux.duplicate.distribution = "uniform"
        model.info.aux.duplicate.maximum = 5

        modifier = model.info.aux.record_modifier

        modifier.max_modifications_in_record = 1
        modifier.max_field_modifiers = 1
        modifier.max_record_modifiers = 1

        name_mod = modifier.fields.add()
        name_mod.selection = 0.1
        name_mod.name = "Name"
        prob = name_mod.probabilities

        prob.insert = 0.1  # insert character in field
        prob.delete = 0.1  # delete character in field
        prob.substitute = 0.1  # substitute character in field
        prob.misspell = 0.0  # use mispelling dictionary
        prob.transpose = 0.1  # transpose adjacent characters
        prob.replace = 0.1  # replace with another value of same fake
        prob.swap = 0.1  # swap two words/values in field
        prob.split = 0.1  # split a field
        prob.merge = 0.1  # merge a field
        prob.nullify = 0.1  # convert to null
        prob.fill = 0.1  # fill empty field with expected type

        street_mod = modifier.fields.add()
        street_mod.selection = 0.9
        street_mod.name = "Street"
        prob2 = street_mod.probabilities

        prob2.insert = 0.1  # insert character in field
        prob2.delete = 0.1  # delete character in field
        prob2.substitute = 0.1  # substitute character in field
        prob2.misspell = 0.0  # use mispelling dictionary
        prob2.transpose = 0.1  # transpose adjacent characters
        prob2.replace = 0.1  # replace with another value of same fake
        prob2.swap = 0.1  # swap two words/values in field
        prob2.split = 0.1  # split a field
        prob2.merge = 0.1  # merge a field
        prob2.nullify = 0.1  # convert to null
        prob2.fill = 0.1  # fill empty field with expected type
        s2 = Synthesizer(model,   seed=4053)
        protorows = []
        for _ in range(10):
            protorows.append(s2.generate())
        print(protorows)


if __name__ == "__main__":
    unittest.main()

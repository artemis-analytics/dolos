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

"""
from importlib import import_module
import os


def create_fakers(live_modules):
    """
    This method takes the live methods,
    and extracts the describe property 
    from them.
    """
    fakers = set()  # This is our set
    for module in live_modules:  # Iterate over all the live modules
        # Add the provider, as well as the describer to the set
        fakers.add((module.Provider(), module.Provider().describe))
    return fakers # Return the values back to the program


MODULE_PATH = 'modules'  # Define the modules directory
# Take all the array contents from 1 -> len(x)
MODULE_INFO = [dir for dir in os.walk(MODULE_PATH)][1:]
# Array is created to load in the modules
LIVE_MODULES = [import_module(module[0].replace("/", "."))
                for module in MODULE_INFO if "__pycache__" not in module[0]]  # Process them so long as they are not the pycache


# This is the provider set that we use in simutable
PROVIDERS = create_fakers(LIVE_MODULES)

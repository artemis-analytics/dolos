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


from importlib import import_module
import yaml
import os


def get_configs(location):
    """
    This method takes in a
    yaml file, containing the
    numpy and scipy methods
    that you want made available
    and injects those into this system.
    """
    with open(location, 'r') as raw_file:  # Open up the location of the yaml file
        existant_methods = yaml.load(raw_file,Loader=yaml.FullLoader)  # Load in that data
    return existant_methods  # Return out the date to the program


def get_modules_from_configs(data):
    """
    This method gets the module names and methods
    from the YAML data dump.
    """
    modules = set()  # Empty array to hold the module names
    for entry in data:  # Get the entries in the yaml file
        for subentry in entry:  # Access the subentries in the data
            if isinstance(subentry, str):  # Get the string entries
                # Create the full name of the module
                full_name = subentry+"."+entry[subentry]['module']
                for method in entry[subentry]['methods']:
                    modules.add((full_name, method))
                break  # Break out of loop
    return modules  # Return the modules


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
    return fakers  # Return the values back to the program


MODULE_CONFIG_LOCATION = "configs/modules.yaml"  # Path to the settings file
MODULE_PATH = 'providers'  # Define the modules directory
# Take all the array contents from 1 -> len(x)
MODULE_INFO = [dir for dir in os.walk(MODULE_PATH)][1:]
# Array is created to load in the modules
LIVE_MODULES = [import_module(module[0].replace("/", "."))
                for module in MODULE_INFO if "__pycache__" not in module[0]]  # Process them so long as they are not the pycache
# Array contains modules named in the YAML file, we'll need to load these in sepperately
STRING_MODULES = get_modules_from_configs(get_configs(MODULE_CONFIG_LOCATION))
# This is the provider set that we use in simutable
BASE_PROVIDERS = create_fakers(LIVE_MODULES)
# This gives us the total array of the providerss
PROVIDERS = [STRING_MODULES, BASE_PROVIDERS]
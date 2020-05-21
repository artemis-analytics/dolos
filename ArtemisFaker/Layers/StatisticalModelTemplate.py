"""
Copyright © Her Majesty the Queen in Right of Canada, 
as represented by the Minister of Statistics Canada, 2020

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import importlib as ipl
from inspect import signature

class AbstractModel():

    def __init__(self, model: object, seed=False, imported=True):
        if imported:
            self.model = ipl.import_module(model)
        else:
            self.model = model
        if (seed):
            self.seed = seed
        
    def create_instance(self, method):
        if self.seed:
            # Now set the seed
            seed_setter = getattr(self.model, "seed")
            seed_setter(self.seed)
        self.method = getattr(self.model, method)
    
    def generate_random(self, params=False):
        if params:
            return self.method(*params)
        else:
            return self.method()
        





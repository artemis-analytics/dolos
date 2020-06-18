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

class ModelInterface():

    def __init__(self, parent, method):
        self.parent = parent  # Assumes instantiated class or method (1)
        self.method = method # The method is loaded (2)
        self.psudo_switch = {"scipy.stats": self.scipygen,
                             "numpy.random": self.numpygen}  # Executes known actions (3)
        
    def generate_random(self, params=None): # Generate the results
        self.params = params  # Set params
        try:
            try:
                name = self.parent.__name__
            except AttributeError:
                name  = self.parent.__class__.__name__
            result = self.psudo_switch[name] # Grab method from (3)
            return result()
        except KeyError:
            return self.custom()  # Othewise get custom method as the "default" for (3)

    def scipygen(self): # For scipy methods
        generator = getattr(self.parent, self.method)
        try:
            
            getattr(generator, "rvs")  # Check if an rvs method
            if self.params:
                return generator(*self.params).rvs()
            else:
                return generator().rvs()

        except AttributeError: # Otherwise skip that
            if self.params:
                return self._fetch_and_return_params()
            else:
                return self._fetch_and_return()

    def numpygen(self): # For numpy
        if self.params: # Control for params
            return self._fetch_return_params()
        else:
            return self._fetch_and_return()

    def custom(self): # For custom code
        if self.params: # Control the params
            return self._fetch_return_params()
        else:
            return self._fetch_and_return()
    
    def _fetch_return_params(self):
        return getattr(self.parent, self.method)(*self.params)
    
    def _fetch_and_return(self):
        return getattr(self.parent, self.method)()
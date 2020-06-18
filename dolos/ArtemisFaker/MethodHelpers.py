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

from importlib import import_module  # Import libary module tool

class MethodHandler():

    def get_parent(self, parent, method):
        """
        This runs some checks against the 
        parent method to ensure that the
        method is actually in the parent class.
        """
        self.parent = parent # Load in the parent
        try: # Run the check
            assert isinstance(method, str) and isinstance(parent, str) # Check that the data is a string
            self.method = method # Set the method
        except AssertionError: # If not
            try: # Check if not numpy, will trip only if seeded
                if not self._is_numpy(): # Run the check numpy
                    self.method = method # Load in the method
                    self._check_child() # Check that it exists
                    return self.parent # Return out the parent
                elif self._is_numpy(): # If it actually is numpy
                    self.method = method
                    self._check_child()
                    return self.parent
            except AssertionError: # If that fails
                raise ImportError("Error: Failed to resolve module.") # Complain if the model fails all this
        self.parent = import_module(self.parent) # We mutate the self.parent variable here.
        self._check_child() # Verify that the submethod is valid
        return self.parent # Return it as inst object

    def _is_numpy(self):
        """
        Check if the method is numpy
        """
        try: # Verify that is is numpy
            assert self.parent != "numpy.random" # Assert the method name
            return False # Return false 
        except AssertionError: # if it fails
            return True # return True

    def _check_child(self):
        """
        Verify that the method is
        inside the parent.
        """
        if hasattr(self.parent, self.method): # Check if parent contains child
            return True
        else:
            raise AttributeError("No method named %s")
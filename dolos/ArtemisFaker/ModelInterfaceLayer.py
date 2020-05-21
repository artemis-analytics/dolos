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
import inspect

class ModelInterface():

    def __init__(self, seed=False, engine=None):
        self.seed = seed
        if (engine is not None):
            if isinstance(engine, str):
                if ("scipy" not in engine.lower()) and (not seed):
                    self.model = ipl.import_module(engine)
                else:
                    self.model = engine
            else:
                self.model = engine
        else:
            raise ValueError

    def custom_generator(self, method=None, function=False):
        """
        Method allowing importing external
        custom synthetic data generators.
        This code provides access to methods
        within the custom generators.
        """
        # Set generator
        if not function:
            generator = getattr(self.model, method)

                # Set seed
            if self.seed:
                set_seed = getattr(self.model, "set_seed")
                set_seed(self.seed)

                # Call generator with or without params
            self.generator = generator

        else:
            # Just skips over the entire setting process
            self.generator = self.model

    def numpy_generator(self, method):
        """
        Method provides access to numpy
        random number generation tools.
        Allows seeding of generator.
        """
        # Import numpy dynamically
        model = ipl.import_module("numpy.random")
        if self.seed:
            # Now set the seed
            seed_setter = getattr(model, "seed")
            seed_setter(self.seed)

        # Get the specific generator
        self.generator = getattr(model, method)

    def generate_random(self, params=None):
        """
        Factory method for returning
        the random number generator.
        """
        model = self.generator
        params = params
        if params:
            return model(*params)
        else:
            return model()

    def scipy_generator(self, method):
        """
        Method for providing access
        to scipy random number generators.
        May also be seeded.
        """
        # Instantiate the model
        model = ipl.import_module(self.model) # There is an error in here. Walk through with a debugger.
        # Instantiate a numpy instance in the same scope
        if self.seed:
            rng = ipl.import_module("numpy.random")
            # Now set the seed
            seed_setter = getattr(rng, "seed")
            seed_setter(self.seed)

        # Now instantiate the generator
        self.generator = getattr(model, method)

    def generate_random_scipy(self, params, rvs=False):
        # Call generator with
        if params:
            if rvs:
                return self.generator(*params).rvs()
            else:
                return self.generator(*params)
        elif not params:
            if rvs:
                return self.generator().rvs()
            else:
                return self.generator()
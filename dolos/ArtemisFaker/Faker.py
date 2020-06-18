import numpy.random as random  # Random number genreator Numpy
from importlib import import_module  # Import module
from ArtemisFaker.MethodHelpers import MethodHandler  # Get the method helpers
from ArtemisFaker.ModelHelpers import ModelInterface  # Get the model helpers

class ArtemisFaker(MethodHandler):

    def __init__(self, seed=None):
        self.numpy = random  # Setting the classes RNG backed to be numpy
        super().__init__()  # Initiate the superclass
        # Key-value hashmap for the available methods (1)
        self.are_avilable = {}
        self.seed = seed  # Set the seed (2)
        if self.seed is not None:  # Check the seed
            self._set_seed()  # Set the seed if existant

    def _set_seed(self):
        """
        Method sets the seed
        for the system.
        """
        self.numpy.seed(
            self.seed)  # Set the seed in the numpy instance from (2)

    def add_faker(self, parent, method):
        """
        This adds the faker instance to the
        hashmap, and gets all the params
        that are needed for instantiating.
        """
        parent = super().get_parent(parent, method)  # Fetch the method
        try:
            if parent.__name__ != self.numpy.__name__:  # Check if the variable is numpy
                # Create a model interface instance
                interface = ModelInterface(parent, method)
            else:  # If it is, don't use the parent
                # Create the model interface
                interface = ModelInterface(self.numpy, method)
        except AttributeError:
            interface = ModelInterface(parent, method)
        # Insert the value into the key value pair (1)
        self.are_avilable[method] = interface

    def fake(self, method, params=None):
        """
        This method is the RNG access route,
        and we use it to generate the value.
        What this does it provide an shim to access
        the RNGs with invariate syntax.
        """
        if not (isinstance(params, list) or (params is None)) :
            params = [params]
        if isinstance(method, list):
            if len(method) != 1:
                raise IndexError("Multiple methods passed")
            else:
                method = method[-1]
        try:  # Check if the genrator is inside the hashmap (1)
            # Get it from the hashmap (1)
            interface = self.are_avilable[method.lower()]
            # Produce the random value
            return interface.generate_random(params)

        except KeyError:  # Catch the error if it is not instantiated
            # Raise an error if it is not there.
            raise KeyError("Faker %s method not available." %method)

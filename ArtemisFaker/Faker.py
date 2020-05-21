from Layers import FakerModelInterfaceLayer, FakerModelInterfaceLayer, StatisticalModelTemplate

class ArtemisFaker():

    def __init__(self):
        self.providers = []

    def add_provider(self, provider, configs):
        spec_providers = ("numpy", "scipy")
        instance = FakerModelInterfaceLayer.ModelInterface()
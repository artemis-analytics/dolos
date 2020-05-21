from Layers import FakerModelInterfaceLayer, FakerModelInterfaceLayer, StatisticalModelTemplate

class ArtemisFaker():

    def __init__(self):
        self.providers = []

    def add_provider(self, engine, params, isPackage=False):
        if isPackage:
            instance = FakerModelInterfaceLayer.ModelInterface(engine=engine)
        else:
            instance = FakerModelInterfaceLayer.ModelInterface(engine=None)
        return provider
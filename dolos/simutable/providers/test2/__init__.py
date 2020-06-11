
class Provider():

    def __init__(self):
        self.generator_name = "name"
    
    @property
    def describe(self):
        return self.generator_name

    def name(self):
        return "TM3"

class Provider():
    def __init__(self):
        self.name = "name_gen"
    
    @property
    def describe(self):
        return self.name
    
    def name_gen(self, param):
        return "TM2"

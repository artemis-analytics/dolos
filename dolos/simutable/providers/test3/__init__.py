
class Provider():

    def __init__(self):
        self.generator_name = "test_method_2"
    
    @property
    def describe(self):
        return self.generator_name

    def test_method_2(self):
        return "TM2"

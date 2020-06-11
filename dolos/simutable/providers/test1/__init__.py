
class Provider():

    def __init__(self):
        self.generator_name = "test_method_1"
    
    @property
    def describe(self):
        return self.generator_name

    def test_method_1(self):
        return "TM1"
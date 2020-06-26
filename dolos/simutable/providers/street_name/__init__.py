import numpy.random as numpy

class Provider():

    def __init__(self):
        self.generator_name = "address"
    
    @property
    def describe(self):
        return self.generator_name

    def apartment(self):
        room = str(numpy.randint(0, 1000)) 
        street = str(numpy.randint(0, 10000))
        return "%s-%s" %(room, street)

    def house(self):
        return str(numpy.randint(0, 10000))

    def switch(self, condition):
        cases = {
            "house": self.house
            "apartment": self.apartment
        }
        try:
            result = cases[condition]
        except KeyError:
            result = self.house

        return result()

    def address(self, param):
        return self.switch(param)
        
        

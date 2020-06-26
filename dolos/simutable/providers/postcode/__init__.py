import numpy.random as numpy

class Provider():

    def __init__(self):
        self.generator_name = "postcode"
    
    @property
    def describe(self):
        return self.generator_name
    
    @property
    def alphabet_dict(self):
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        number_dict = {}
        for i, letter in enumerate(letters):
            number_dict[i] = letter
        return number_dict

    def postcode(self):
        postal = ""
        number_dict = self.alphabet_dict
        numeric_list = [numpy.randint(0, 23) for _ in range(7)]
        for i, entry in enumerate(numeric_list):
            if ((i % 2) == 0):
                postal = postal+number_dict[i]
            elif ((i%2) != 0) and (i != 3):
                try:
                    postal = postal+(list(str(entry))[-1])
                except TypeError:
                    postal = postal+(str(entry))
            elif (i == 3):
                postal = postal+" "

        return postal
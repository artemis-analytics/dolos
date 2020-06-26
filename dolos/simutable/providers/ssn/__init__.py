import numpy.random as numpy

class Provider():

    def __init__(self):
        self.generator_method = "ssn_generator"

    @property
    def describe(self):
        """
        Method returns name of 
        main generator method
        """
        return self.generator_method

    def ssn_generator(self):
        """
        Generates a fake, SSN number.
        The SSN number is not Luhn valid.
        """
        ssn = []
        for i in range(1, 10):
            if i != 1:
                start = 0
            else:
                start = 1
            ssn.append(numpy.randint(start, 9))
            if i % 3 == 0:
                ssn.append(" ")
        ssn = [str(i) for i in ssn]
        return "".join(ssn)
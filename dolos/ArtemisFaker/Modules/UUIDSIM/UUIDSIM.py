"""
Copyright © Her Majesty the Queen in Right of Canada, 
as represented by the Minister of Statistics Canada, 2020

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from numpy import random
from StringIO import StringIO

class UUIDSimulator():
    """
    This is a simple UUID simulator
    used to generate random fake UUID
    placeholders. This method is class
    is used in unit testing the code.

    """
    def __init__(self):
        self.alpha = self.GenerateAlphaDict()

    def GenerateAlphaDict(self):
        """
        Method builds a dict of 
        valid Hexa letters.
        """
        alphadict = {}
        alpha = list("abcdef")
        for i in range(1, len(alpha)+1):
            alphadict.update({i: alpha[i-1]})
        return alphadict

    def IsAlpha(self):
        """
        Method generates a random
        probability for adding in
        a Hexa letter.
        """
        value = random.uniform(0, 1)
        if value <= 0.2:
            return True
        else:
            return False

    def generate(self):
        """
        Method generates a 
        random UUID value.
        """
        output = StringIO()
        lenghts = [8, 4, 4, 12]
        for i in lenghts:
            for _ in range(i):
                if self.IsAlpha():
                    num = random.randint(1, 7)
                    result = self.alpha[num]
                    output.write(str(result))
                else:
                    num = str(random.randint(0, 9))
                    output.write(num)
            if i != 12:
                output.write("-")
        uuid = output.getvalue()
        return uuid

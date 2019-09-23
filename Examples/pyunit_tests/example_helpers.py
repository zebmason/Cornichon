import unittest

class Helpers(unittest.TestCase):
    def GivenAnInitial(self, value):
        print("      Given an initial ", value)

    def WhenYouAddA(self, second):
        print("      When you add a ", second)

    def ThenTheResultIs(self, sum):
        print("      Then the result is ", sum)

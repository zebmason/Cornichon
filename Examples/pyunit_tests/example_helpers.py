import unittest

class AddOneOtherHelper(unittest.TestCase):
    def __init__(self):
        print("  Feature: Accumulator")
        print("    Scenario: Add one other")

    def GivenAnInitial(self, value):
        print("      Given an initial ", value)

    def WhenYouAddA(self, second):
        print("      When you add a ", second)

    def ThenTheResultIs(self, sum):
        print("      Then the result is ", sum)

class AddTwoOthersHelper(unittest.TestCase):
    def __init__(self):
        print("  Feature: Accumulator")
        print("    Scenario: Add two others")

    def GivenAnInitial(self, value):
        print("      Given an initial ", value)

    def WhenYouAddA(self, second):
        print("      When you add a ", second)

    def ThenTheResultIs(self, sum):
        print("      Then the result is ", sum)

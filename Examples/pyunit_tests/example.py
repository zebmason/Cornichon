import unittest
from example_helpers import *

class Example(unittest.TestCase):

    def AddOneOther(self, value, second, sum):
        print("  Feature: Accumulator")
        print("    Scenario: Add one other")
        helpers = AddOneOtherHelper()
        helpers.GivenAnInitial(value);
        helpers.WhenYouAddA(second);
        helpers.ThenTheResultIs(sum);

    def AddTwoOthers(self, value, second, third, sum):
        print("  Feature: Accumulator")
        print("    Scenario: Add two others")
        helpers = AddTwoOthersHelper()
        helpers.GivenAnInitial(value);
        helpers.WhenYouAddA(second);
        helpers.WhenYouAddA(third);
        helpers.ThenTheResultIs(sum);

    def test_addOneOther_1_2_3(self):
        self.AddOneOther(1, 2, 3)

    def test_addOneOther_2_2_4(self):
        self.AddOneOther(2, 2, 4)

    def test_addTwoOthers_1_2_3_6(self):
        self.AddTwoOthers(1, 2, 3, 6)

    def test_addTwoOthers_2_3_4_9(self):
        self.AddTwoOthers(2, 3, 4, 9)

if __name__ == '__main__':
    unittest.main()

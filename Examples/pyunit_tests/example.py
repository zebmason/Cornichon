import unittest
from example_helpers import *

class Example(unittest.TestCase):
    """Gherkin DSL feature"""

    def AddOneOther(self, value, second, sum):
        """Gherkin DSL scenario"""
        helpers = AddOneOtherHelper()
        helpers.GivenAnInitial(value);
        helpers.WhenYouAddA(second);
        helpers.ThenTheResultIs(sum);

    def AddTwoOthers(self, value, second, third, sum):
        """Gherkin DSL scenario"""
        helpers = AddTwoOthersHelper()
        helpers.GivenAnInitial(value);
        helpers.WhenYouAddA(second);
        helpers.WhenYouAddA(third);
        helpers.ThenTheResultIs(sum);

    def test_addOneOther_1_2_3(self):
        """Gherkin DSL test"""
        self.AddOneOther(1, 2, 3)

    def test_addOneOther_2_2_4(self):
        """Gherkin DSL test"""
        self.AddOneOther(2, 2, 4)

    def test_addTwoOthers_1_2_3_6(self):
        """Gherkin DSL test"""
        self.AddTwoOthers(1, 2, 3, 6)

    def test_addTwoOthers_2_3_4_9(self):
        """Gherkin DSL test"""
        self.AddTwoOthers(2, 3, 4, 9)

if __name__ == '__main__':
    unittest.main()

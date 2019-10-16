import unittest
from example2_scenarios import *


class Accumulator2(unittest.TestCase):
    """Gherkin DSL feature"""

    def test_add_one_other(self):
        """Gherkin DSL test"""
        scenario = Scenarios.AddOneOther()
        scenario.GivenAnInitial6()
        scenario.WhenYouAddA5()
        scenario.ThenTheResultIs11()

    def test_add_two_others(self):
        """Gherkin DSL test"""
        scenario = Scenarios.AddTwoOthers()
        scenario.GivenAnInitial6()
        scenario.WhenYouAddA8()
        scenario.WhenYouAddA4()
        scenario.ThenTheResultIs18()


if __name__ == '__main__':
    unittest.main()

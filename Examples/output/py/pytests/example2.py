import pytest
from example2_scenarios import *


def test_add_one_other():
    """Gherkin DSL test"""
    scenario = Scenarios.AddOneOther()
    scenario.GivenAnInitial6()
    scenario.WhenYouAddA5()
    scenario.ThenTheResultIs11()


def test_add_two_others():
    """Gherkin DSL test"""
    scenario = Scenarios.AddTwoOthers()
    scenario.GivenAnInitial6()
    scenario.WhenYouAddA8()
    scenario.WhenYouAddA4()
    scenario.ThenTheResultIs18()

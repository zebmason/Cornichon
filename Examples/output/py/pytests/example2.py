import pytest
from example2_scenarios import *


def test_AddOneOther():
    """Gherkin DSL test"""
    scenario = Scenarios.AddOneOther()
    scenario.GivenAnInitial6()
    scenario.WhenYouAddA5()
    scenario.ThenTheResultIs11()


def test_AddTwoOthers():
    """Gherkin DSL test"""
    scenario = Scenarios.AddTwoOthers()
    scenario.GivenAnInitial6()
    scenario.WhenYouAddA8()
    scenario.WhenYouAddA4()
    scenario.ThenTheResultIs18()

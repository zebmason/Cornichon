import pytest
from example_scenarios import *


@pytest.mark.parametrize(
    "value, second, sum",
    [
        (
            1, 2, 3,
        ),
        (
            2, 2, 4,
        ),
    ],
)
def test_add_one_other(value, second, sum):
    """Gherkin DSL test"""
    scenario = Scenarios.AddOneOther()
    scenario.GivenAnInitial(value)
    scenario.WhenYouAddA(second)
    scenario.ThenTheResultIs(sum)


@pytest.mark.parametrize(
    "value, second, third, sum",
    [
        (
            1, 2, 3, 6,
        ),
        (
            2, 3, 4, 9,
        ),
    ],
)
def test_add_two_others(value, second, third, sum):
    """Gherkin DSL test"""
    scenario = Scenarios.AddTwoOthers()
    scenario.GivenAnInitial(value)
    scenario.WhenYouAddA(second)
    scenario.WhenYouAddA(third)
    scenario.ThenTheResultIs(sum)

import unittest
from scenarios_cornichon import *


class Cornichon(unittest.TestCase):
    """Gherkin DSL feature"""

    def Cppunittest(self, name):
        """Gherkin DSL scenario"""
        scenario = CppunittestScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCppunittest()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Cppscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = CppscenariosScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCppscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Googletest(self, name):
        """Gherkin DSL scenario"""
        scenario = GoogletestScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsGoogletest()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyunit_tests(self, name):
        """Gherkin DSL scenario"""
        scenario = Pyunit_testsScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPyunit_tests()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = PyscenariosScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPyscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Unittesting(self, name):
        """Gherkin DSL scenario"""
        scenario = UnittestingScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsUnittesting()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Nunit(self, name):
        """Gherkin DSL scenario"""
        scenario = NunitScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsNunit()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Csscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = CsscenariosScenario()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCsscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def test_cppunittest_example(self):
        """Gherkin DSL test"""
        self.Cppunittest("example")

    def test_cppscenarios_example(self):
        """Gherkin DSL test"""
        self.Cppscenarios("example")

    def test_googletest_example(self):
        """Gherkin DSL test"""
        self.Googletest("example")

    def test_pyunit_tests_example(self):
        """Gherkin DSL test"""
        self.Pyunit_tests("example")

    def test_pyscenarios_example(self):
        """Gherkin DSL test"""
        self.Pyscenarios("example")

    def test_unittesting_example(self):
        """Gherkin DSL test"""
        self.Unittesting("example")

    def test_nunit_example(self):
        """Gherkin DSL test"""
        self.Nunit("example")

    def test_csscenarios_example(self):
        """Gherkin DSL test"""
        self.Csscenarios("example")


if __name__ == '__main__':
    unittest.main()

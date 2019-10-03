import unittest
from helpers import *


class Cornichon(unittest.TestCase):
    """Gherkin DSL feature"""

    def Cppunittest(self, name):
        """Gherkin DSL scenario"""
        helpers = CppunittestHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsCppunittest()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Cpphelpers(self, name):
        """Gherkin DSL scenario"""
        helpers = CpphelpersHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsCpphelpers()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Googletest(self, name):
        """Gherkin DSL scenario"""
        helpers = GoogletestHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsGoogletest()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyunittests(self, name):
        """Gherkin DSL scenario"""
        helpers = PyunittestsHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsPyunittests()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyhelpers(self, name):
        """Gherkin DSL scenario"""
        helpers = PyhelpersHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsPyhelpers()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Unittesting(self, name):
        """Gherkin DSL scenario"""
        helpers = UnittestingHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsUnittesting()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Nunit(self, name):
        """Gherkin DSL scenario"""
        helpers = NunitHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsNunit()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Cshelpers(self, name):
        """Gherkin DSL scenario"""
        helpers = CshelpersHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsCshelpers()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def test_cppunittest_example(self):
        """Gherkin DSL test"""
        self.Cppunittest("example")

    def test_cpphelpers_example(self):
        """Gherkin DSL test"""
        self.Cpphelpers("example")

    def test_googletest_example(self):
        """Gherkin DSL test"""
        self.Googletest("example")

    def test_pyunittests_example(self):
        """Gherkin DSL test"""
        self.Pyunittests("example")

    def test_pyhelpers_example(self):
        """Gherkin DSL test"""
        self.Pyhelpers("example")

    def test_unittesting_example(self):
        """Gherkin DSL test"""
        self.Unittesting("example")

    def test_nunit_example(self):
        """Gherkin DSL test"""
        self.Nunit("example")

    def test_cshelpers_example(self):
        """Gherkin DSL test"""
        self.Cshelpers("example")


if __name__ == '__main__':
    unittest.main()

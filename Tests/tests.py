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

    def Pyunit_tests(self, name):
        """Gherkin DSL scenario"""
        helpers = Pyunit_testsHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsPyunit_tests()
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyhelpers(self, name):
        """Gherkin DSL scenario"""
        helpers = PyhelpersHelper()
        helpers.GivenAFeatureFileCalled(name)
        helpers.WhenTheGeneratorIsPyhelpers()
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

    def test_pyunit_tests_example(self):
        """Gherkin DSL test"""
        self.Pyunit_tests("example")

    def test_pyhelpers_example(self):
        """Gherkin DSL test"""
        self.Pyhelpers("example")


if __name__ == '__main__':
    unittest.main()

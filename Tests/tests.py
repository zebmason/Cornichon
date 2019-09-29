import unittest
from helpers import *

class Cornichon(unittest.TestCase):

    def Cppunittest(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: cppunittest")
        helpers = CppunittestHelper()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCppunittest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Cpphelpers(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: cpphelpers")
        helpers = CpphelpersHelper()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCpphelpers();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Googletest(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: googletest")
        helpers = GoogletestHelper()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsGoogletest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Pyunit_tests(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: pyunit_tests")
        helpers = Pyunit_testsHelper()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsPyunit_tests();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Pyhelpers(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: pyhelpers")
        helpers = PyhelpersHelper()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsPyhelpers();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def test_cppunittest_example(self):
        self.Cppunittest("example")

    def test_cpphelpers_example(self):
        self.Cpphelpers("example")

    def test_googletest_example(self):
        self.Googletest("example")

    def test_pyunit_tests_example(self):
        self.Pyunit_tests("example")

    def test_pyhelpers_example(self):
        self.Pyhelpers("example")

if __name__ == '__main__':
    unittest.main()

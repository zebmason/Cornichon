import unittest
from helpers import Helpers

class Cornichon(unittest.TestCase):

    def Cppunittest(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: cppunittest")
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCppunittest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Cpphelpers(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: cpphelpers")
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCpphelpers();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Googletest(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: googletest")
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsGoogletest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Pyunit_tests(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: pyunit_tests")
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsPyunit_tests();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Pyhelpers(self, name):
        print("  Feature: Cornichon")
        print("    Scenario: pyhelpers")
        helpers = Helpers()
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

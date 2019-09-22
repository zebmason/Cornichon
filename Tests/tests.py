import unittest
from helpers import Helpers

class Cornichon(unittest.TestCase):

    def Cppunittest(self, name):
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCppunittest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Cpphelpers(self, name):
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsCpphelpers();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def Googletest(self, name):
        helpers = Helpers()
        helpers.GivenAFeatureFileCalled(name);
        helpers.WhenTheGeneratorIsGoogletest();
        helpers.ThenTheGeneratedTestIsTheSameAsTheSaved();

    def test_cppunittest_example(self):
        self.Cppunittest("example")

    def test_cpphelpers_example(self):
        self.Cpphelpers("example")

    def test_googletest_example(self):
        self.Googletest("example")

if __name__ == '__main__':
    unittest.main()

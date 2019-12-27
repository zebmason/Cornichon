import unittest
from scenarios_cornichon import *


class Cornichon(unittest.TestCase):
    """Gherkin DSL feature"""

    def Cppunittest(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Cppunittest()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCppunittest()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Cppscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Cppscenarios()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCppscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Unnested(self, name, namespace):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Unnested()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCppscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAs(namespace)

    def Googletest(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Googletest()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsGoogletest()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyunit_tests(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Pyunit_tests()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPyunit_tests()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pyscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Pyscenarios()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPyscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pytests(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Pytests()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPytests()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Pytestscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Pytestscenarios()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsPyscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Unittesting(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Unittesting()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsUnittesting()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Nunit(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Nunit()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsNunit()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Csscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Csscenarios()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsCsscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Vbunittesting(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Vbunittesting()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsUnittesting()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Vbnunit(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Vbnunit()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsNunit()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def Vbscenarios(self, name):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Vbscenarios()
        scenario.GivenAFeatureFileCalled(name)
        scenario.WhenTheGeneratorIsVbscenarios()
        scenario.ThenTheGeneratedTestIsTheSameAsTheSaved()

    def test_cppunittest_example(self):
        """Gherkin DSL test"""
        self.Cppunittest("example")

    def test_cppunittest_example2(self):
        """Gherkin DSL test"""
        self.Cppunittest("example2")

    def test_cppscenarios_example(self):
        """Gherkin DSL test"""
        self.Cppscenarios("example")

    def test_cppscenarios_example2(self):
        """Gherkin DSL test"""
        self.Cppscenarios("example2")

    def test_unnested_example2_namespace2(self):
        """Gherkin DSL test"""
        self.Unnested("example2", "namespace2")

    def test_googletest_example(self):
        """Gherkin DSL test"""
        self.Googletest("example")

    def test_googletest_example2(self):
        """Gherkin DSL test"""
        self.Googletest("example2")

    def test_pyunit_tests_example(self):
        """Gherkin DSL test"""
        self.Pyunit_tests("example")

    def test_pyunit_tests_example2(self):
        """Gherkin DSL test"""
        self.Pyunit_tests("example2")

    def test_pyscenarios_example(self):
        """Gherkin DSL test"""
        self.Pyscenarios("example")

    def test_pyscenarios_example2(self):
        """Gherkin DSL test"""
        self.Pyscenarios("example2")

    def test_pytests_example(self):
        """Gherkin DSL test"""
        self.Pytests("example")

    def test_pytests_example2(self):
        """Gherkin DSL test"""
        self.Pytests("example2")

    def test_pytestscenarios_example(self):
        """Gherkin DSL test"""
        self.Pytestscenarios("example")

    def test_pytestscenarios_example2(self):
        """Gherkin DSL test"""
        self.Pytestscenarios("example2")

    def test_unittesting_example(self):
        """Gherkin DSL test"""
        self.Unittesting("example")

    def test_unittesting_example2(self):
        """Gherkin DSL test"""
        self.Unittesting("example2")

    def test_nunit_example(self):
        """Gherkin DSL test"""
        self.Nunit("example")

    def test_nunit_example2(self):
        """Gherkin DSL test"""
        self.Nunit("example2")

    def test_csscenarios_example(self):
        """Gherkin DSL test"""
        self.Csscenarios("example")

    def test_csscenarios_example2(self):
        """Gherkin DSL test"""
        self.Csscenarios("example2")

    def test_vbunittesting_example(self):
        """Gherkin DSL test"""
        self.Vbunittesting("example")

    def test_vbunittesting_example2(self):
        """Gherkin DSL test"""
        self.Vbunittesting("example2")

    def test_vbnunit_example(self):
        """Gherkin DSL test"""
        self.Vbnunit("example")

    def test_vbnunit_example2(self):
        """Gherkin DSL test"""
        self.Vbnunit("example2")

    def test_vbscenarios_example(self):
        """Gherkin DSL test"""
        self.Vbscenarios("example")

    def test_vbscenarios_example2(self):
        """Gherkin DSL test"""
        self.Vbscenarios("example2")


if __name__ == '__main__':
    unittest.main()

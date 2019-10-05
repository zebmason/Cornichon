import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../Cornichon')
sys.path.insert(0, subdir)
import cornichon


class Scenarios(unittest.TestCase):
    """Test class scenario"""
    def GivenAFeatureFileCalled(self, name):
        """Gherkin DSL step"""
        self.name = name

    def ThenTheGeneratedTestIsTheSameAsTheSaved(self):
        """Gherkin DSL step"""
        inFileName = os.path.join('../Examples/tests', self.name + '.feature')
        f = open(inFileName, "r")
        self.settings["gherkin"] = f.readlines()
        f.close()
        contents = self.header + cornichon.Generate(self.settings, self.output)
        filePath = '../Examples/output/%s/%s%s' % (self.folder, self.name, self.ext)
        self.DiffScenario(contents, filePath)

    def DiffScenario(self, contents, filename):
        """Gherkin DSL step"""
        newlines = contents.split('\n')
        oldlines = []
        if os.path.isfile(filename):
            fp = open(filename, "r")
            oldlines = fp.readlines()
            fp.close()
        else:
            fp = open(filename, "w")
            fp.write(contents)
            fp.close()
            self.fail("Writing test output to file")
        num = len(newlines)
        num2 = len(oldlines)
        diffs = abs(num - num2)
        if os.path.exists(filename + ".fail"):
            os.remove(filename + ".fail")
        if num2 < num:
            num = num2
        for i in range(num):
            old = oldlines[i].rstrip()
            if old != newlines[i]:
                fp = open(filename + ".fail", "w")
                fp.write(contents)
                fp.close()
            self.assertEqual(old, newlines[i])


class CppunittestScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsCppunittest(self):
        """Gherkin DSL step"""
        self.output = "cpp/cppunittest"
        self.folder = "cpp/cppunittest"
        self.ext = ".cpp"
        self.header = ""
        self.settings = cornichon.Settings(self.output)
        self.settings["scenarios file"] = "../cppscenarios/%s.h" % self.name


class CppscenariosScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsCppscenarios(self):
        """Gherkin DSL step"""
        self.output = "cpp/cppscenarios"
        self.folder = "cpp/cppscenarios"
        self.ext = ".h"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = cornichon.Settings(self.output)


class GoogletestScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsGoogletest(self):
        """Gherkin DSL step"""
        self.output = "cpp/googletest"
        self.folder = "cpp/googletest"
        self.ext = ".cpp"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = cornichon.Settings(self.output)
        self.settings["scenarios file"] = "../cppscenarios/%s.h" % self.name


class Pyunit_testsScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsPyunit_tests(self):
        """Gherkin DSL step"""
        self.output = "py/pyunit_tests"
        self.folder = "py/pyunit_tests"
        self.ext = ".py"
        self.header = ""
        self.settings = cornichon.Settings(self.output)
        self.settings["scenarios file"] = "example_scenarios"


class PyscenariosScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsPyscenarios(self):
        """Gherkin DSL step"""
        self.output = "py/pyscenarios"
        self.folder = "py/pyunit_tests"
        self.ext = "_scenarios.py"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class UnittestingScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsUnittesting(self):
        """Gherkin DSL step"""
        self.output = "cs/unittesting"
        self.folder = "cs/unittesting"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class NunitScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsNunit(self):
        """Gherkin DSL step"""
        self.output = "cs/nunit"
        self.folder = "cs/nunit"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class CsscenariosScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsCsscenarios(self):
        """Gherkin DSL step"""
        self.output = "cs/csscenarios"
        self.folder = "cs/csscenarios"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class VbunittestingScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsUnittesting(self):
        """Gherkin DSL step"""
        self.output = "vb/unittesting"
        self.folder = "vb/unittesting"
        self.ext = ".vb"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class VbnunitScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsNunit(self):
        """Gherkin DSL step"""
        self.output = "vb/nunit"
        self.folder = "vb/nunit"
        self.ext = ".vb"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class VbscenariosScenario(Scenarios):
    """Test class scenario"""
    def WhenTheGeneratorIsVbscenarios(self):
        """Gherkin DSL step"""
        self.output = "vb/vbscenarios"
        self.folder = "vb/vbscenarios"
        self.ext = ".vb"
        self.header = ""
        self.settings = cornichon.Settings(self.output)

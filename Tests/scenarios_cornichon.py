import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../Cornichon')
sys.path.insert(0, subdir)
import cornichon


class Helpers(unittest.TestCase):
    """Test class helper"""
    def GivenAFeatureFileCalled(self, name):
        """Gherkin DSL step"""
        self.name = name

    def ThenTheGeneratedTestIsTheSameAsTheSaved(self):
        """Gherkin DSL step"""
        self.settings["stub"] = self.name
        inFileName = os.path.join('../Examples/tests', self.name + '.feature')
        f = open(inFileName, "r")
        self.settings["gherkin"] = f.readlines()
        f.close()
        contents = self.header + cornichon.Generate(self.settings, self.output)
        filePath = '../Examples/output/%s/%s%s' % (self.folder, self.name, self.ext)
        self.DiffHelper(contents, filePath)

    def DiffHelper(self, contents, filename):
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


class CppunittestHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsCppunittest(self):
        """Gherkin DSL step"""
        self.output = "cpp/cppunittest"
        self.folder = "cppunittest"
        self.ext = ".cpp"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class CpphelpersHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsCpphelpers(self):
        """Gherkin DSL step"""
        self.output = "cpp/cpphelpers"
        self.folder = "cpphelpers"
        self.ext = ".h"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = cornichon.Settings(self.output)


class GoogletestHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsGoogletest(self):
        """Gherkin DSL step"""
        self.output = "cpp/googletest"
        self.folder = "googletest"
        self.ext = ".cpp"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = cornichon.Settings(self.output)


class PyunittestsHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsPyunittests(self):
        """Gherkin DSL step"""
        self.output = "py/pyunit_tests"
        self.folder = "pyunit_tests"
        self.ext = ".py"
        self.header = ""
        self.settings = cornichon.Settings(self.output)
        self.settings["helpers"] = "example_helpers"


class PyhelpersHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsPyhelpers(self):
        """Gherkin DSL step"""
        self.output = "py/pyhelpers"
        self.folder = "pyunit_tests"
        self.ext = "_helpers.py"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class UnittestingHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsUnittesting(self):
        """Gherkin DSL step"""
        self.output = "cs/unittesting"
        self.folder = "unittesting"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class NunitHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsNunit(self):
        """Gherkin DSL step"""
        self.output = "cs/nunit"
        self.folder = "nunit"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)


class CshelpersHelper(Helpers):
    """Test class helper"""
    def WhenTheGeneratorIsCshelpers(self):
        """Gherkin DSL step"""
        self.output = "cs/cshelpers"
        self.folder = "cshelpers"
        self.ext = ".cs"
        self.header = ""
        self.settings = cornichon.Settings(self.output)

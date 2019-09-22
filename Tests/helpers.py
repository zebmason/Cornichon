import unittest, os, os.path, sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Cornichon')
sys.path.insert(0, subdir)
import cornichon

class Helpers(unittest.TestCase):
    def GivenAFeatureFileCalled(self, name):
        self.name = name

    def WhenTheGeneratorIsCppunittest(self):
        self.output = "cppunittest"
        self.ext = ".cpp"
        self.header = ""
        self.settings = {}
        self.settings["rootnamespace"] = "Cornichon::"
        self.settings["helpers"] = "../helpers/"

    def WhenTheGeneratorIsCpphelpers(self):
        self.output = "cpphelpers"
        self.ext = ".h"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = {}
        self.settings["rootnamespace"] = "Cornichon::"
        self.settings["helpers"] = "../helpers/"

    def WhenTheGeneratorIsGoogletest(self):
        self.output = "googletest"
        self.ext = ".cpp"
        self.header = "// Copyright (c) 2019 ...\n\n"
        self.settings = {}
        self.settings["rootnamespace"] = "Cornichon::"
        self.settings["helpers"] = "../helpers/"

    def DiffHelper(self, contents, filename):
        newlines = contents.split('\n')
        fp = open(filename, "r")
        oldlines = fp.readlines()
        fp.close()
        num = len(newlines)
        num2 = len(oldlines)
        diffs = abs(num - num2)
        if num2 < num:
            num = num2
        for i in range(num):
            self.assertEqual(oldlines[i].rstrip(), newlines[i])
            
    def ThenTheGeneratedTestIsTheSameAsTheSaved(self):
        self.settings["stub"] = self.name
        inFileName = os.path.join('../Examples/tests', self.name + '.feature')
        f = open(inFileName, "r")
        self.settings["gherkin"] = f.readlines()
        f.close()
        contents = self.header + cornichon.Generate(self.settings, self.output)
        self.DiffHelper(contents, '../Examples/%s/%s%s' % (self.output, self.name, self.ext))

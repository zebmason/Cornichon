import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../Cornichon')
sys.path.insert(0, subdir)
import common
import cornichon

sys.path.insert(0, os.path.join(subdir, "cpp"))
import cpputils

sys.path.insert(0, os.path.join(subdir, "py"))
import pyutils


class TemplatedHelper(unittest.TestCase):
    def GivenAnArgument(self, arg):
        self.arg = arg

    def GivenAType(self, type):
        self.type = type

    def GivenATemplate(self, template):
        self.templates = {}
        self.templates[self.type] = template

    def ThenItHasCorresponding(self, output):
        out = common.Argument(self.arg, self.type, self.templates)
        if out != output:
            print("\n{} isn't {}".format(out, output))
        self.assertEqual(out, output)


class TokenizedHelper(unittest.TestCase):
    def GivenAnArgument(self, arg):
        self.arg = arg

    def ThenItHasCorresponding(self, output):
        out = common.Tokenise(self.arg)
        if out != output:
            print("\n{} isn't {}".format(out, output))
        self.assertEqual(out, output)


class SnakedHelper(unittest.TestCase):
    def GivenAnArgument(self, arg):
        self.arg = arg

    def ThenItHasCorresponding(self, output):
        out = common.SnakeCase(self.arg)
        if out != output:
            print("\n{} isn't {}".format(out, output))
        self.assertEqual(out, output)


class ArgumentalHelper(unittest.TestCase):
    def GivenArguments(self, args):
        self.args = args.split(",")

    def GivenTypes(self, types):
        self.types = types.split(",")

    def GivenALanguage(self, language):
        self.language = language

    def GivenItIsADeclaration(self, declaration):
        self.declaration = declaration

    def ThenItHasCorresponding(self, output):
        settings = {}
        if self.language == "cpp":
            settings = cornichon.Settings("cpp/cpphelpers")
        elif self.language == "python":
            settings = cornichon.Settings("py/pyhelpers")

        formats = {}
        argModifier = common.AsSymbol
        if self.declaration:
            formats = settings["types"]
        else:
            formats = settings["values"]
            if self.language == "cpp":
                argModifier = cpputils.ArgModifier
            elif self.language == "python":
                argModifier = pyutils.ArgModifier

        out = common.ArgumentList(self.args, self.types, formats, argModifier)
        if out != output:
            print("\n{} isn't {}".format(out, output))
        self.assertEqual(out, output)

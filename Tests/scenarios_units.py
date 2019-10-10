import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../cornichon')
sys.path.insert(0, subdir)
import common
import cornichon

sys.path.insert(0, os.path.join(subdir, "cpp"))
import cpputils

sys.path.insert(0, os.path.join(subdir, "py"))
import pyutils


class Scenarios:

    class Templated(unittest.TestCase):
        """Test class scenario"""

        def GivenAnArgument(self, arg):
            """Gherkin DSL step"""
            self.arg = arg

        def GivenAType(self, type):
            """Gherkin DSL step"""
            self.type = type

        def GivenATemplate(self, template):
            """Gherkin DSL step"""
            self.templates = {}
            self.templates[self.type] = template

        def ThenItHasCorresponding(self, output):
            """Gherkin DSL step"""
            out = common.Argument(self.arg, self.type, self.templates)
            if out != output:
                print("\n{} isn't {}".format(out, output))
            self.assertEqual(out, output)

    class Tokenized(unittest.TestCase):
        """Test class scenario"""
        def GivenAnArgument(self, arg):
            """Gherkin DSL step"""
            self.arg = arg

        def ThenItHasCorresponding(self, output):
            """Gherkin DSL step"""
            out = common.Tokenise(self.arg)
            if out != output:
                print("\n{} isn't {}".format(out, output))
            self.assertEqual(out, output)

    class Snaked(unittest.TestCase):
        """Test class scenario"""
        def GivenAnArgument(self, arg):
            """Gherkin DSL step"""
            self.arg = arg

        def ThenItHasCorresponding(self, output):
            """Gherkin DSL step"""
            out = common.Tokenise(self.arg, "snake")
            if out != output:
                print("\n{} isn't {}".format(out, output))
            self.assertEqual(out, output)

    class Argumental(unittest.TestCase):
        """Test class scenario"""
        def GivenArguments(self, args):
            """Gherkin DSL step"""
            self.args = args.split(",")

        def GivenTypes(self, types):
            """Gherkin DSL step"""
            self.types = types.split(",")

        def GivenALanguage(self, language):
            """Gherkin DSL step"""
            self.language = language

        def GivenItIsADeclaration(self, declaration):
            """Gherkin DSL step"""
            self.declaration = declaration

        def ThenItHasCorresponding(self, output):
            """Gherkin DSL step"""
            settings = {}
            if self.language == "cpp":
                settings = cornichon.Settings("cpp/cppscenarios")
            elif self.language == "python":
                settings = cornichon.Settings("py/pyscenarios")

            formats = {}
            argModifier = common.UnmodifiedArg
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

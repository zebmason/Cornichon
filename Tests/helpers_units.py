import unittest

import os, os.path, sys
subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Cornichon')
sys.path.insert(0, subdir)
import common

class TypesHelper(unittest.TestCase):
    def GivenAnInput(self, value):
        self.value = value

    def ThenItHasCorresponding(self, type):
        conv = common.Type(self.value)
        if conv != type:
            print("\n{} isn't {}".format(self.value, type))
        self.assertEqual(conv, type)

class WorstHelper(unittest.TestCase):
    def GivenAFirstType(self, first):
        self.first = first

    def GivenASecondType(self, second):
        self.second = second

    def ThenItHasCorresponding(self, type):
        worst = common.Worst(self.first, self.second)
        if worst != type:
            print("\n{} isn't {}".format(worst, type))
        self.assertEqual(worst, type)

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


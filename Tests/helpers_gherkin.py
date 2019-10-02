import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../Cornichon')
sys.path.insert(0, subdir)
import gherkin


class TypesHelper(unittest.TestCase):
    def GivenAnInput(self, value):
        self.value = value

    def ThenItHasCorresponding(self, type):
        conv = gherkin.Type(self.value)
        if conv != type:
            print("\n{} isn't {}".format(self.value, type))
        self.assertEqual(conv, type)


class WorstHelper(unittest.TestCase):
    def GivenAFirstType(self, first):
        self.first = first

    def GivenASecondType(self, second):
        self.second = second

    def ThenItHasCorresponding(self, type):
        worst = gherkin.Worst(self.first, self.second)
        if worst != type:
            print("\n{} isn't {}".format(worst, type))
        self.assertEqual(worst, type)

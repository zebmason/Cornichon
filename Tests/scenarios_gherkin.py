import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../cornichon')
sys.path.insert(0, subdir)
import gherkin


class Scenarios:

    class Types(unittest.TestCase):
        """Test class scenario"""
        def GivenAnInput(self, value):
            """Gherkin DSL step"""
            self.value = value

        def ThenItHasCorresponding(self, type):
            """Gherkin DSL step"""
            conv = gherkin.Type(self.value)
            if conv != type:
                print("\n{} isn't {}".format(self.value, type))
            self.assertEqual(conv, type)

    class Worst(unittest.TestCase):
        """Test class scenario"""
        def GivenAFirstType(self, first):
            """Gherkin DSL step"""
            self.first = first

        def GivenASecondType(self, second):
            """Gherkin DSL step"""
            self.second = second

        def ThenItHasCorresponding(self, type):
            """Gherkin DSL step"""
            worst = gherkin.Worst(self.first, self.second)
            if worst != type:
                print("\n{} isn't {}".format(worst, type))
            self.assertEqual(worst, type)

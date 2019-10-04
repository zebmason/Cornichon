import unittest
import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../Cornichon')
sys.path.insert(0, subdir)
import cornichon
import gherkin


class TestHelpSettings(unittest.TestCase):

    def TestALevel(self, settings, help, level):
        for key in settings:
            try:
                if key not in help:
                    print('Missing {}["{}"]'.format(level, key))
                    self.undoc = True
                    continue
                if type(settings[key]) is str:
                    continue
                sublevel = '{}["{}"]'.format(level, key)
                self.TestALevel(settings[key], help[key], sublevel)
            except TypeError:
                print('Error on {}["{}"]'.format(level, key))
                self.undoc = True

    def TestAModule(self, output):
        try:
            settings = cornichon.Settings(output)
            mod = gherkin.Import(output)
            help = mod.HelpSettings()
            self.TestALevel(settings, help, output)
        except TypeError:
            self.undoc = True

    def testAll(self):
        self.undoc = False
        for sub in os.listdir('../Cornichon'):
            if sub == "__pycache__":
                continue
            path = os.path.join('../Cornichon', sub)
            if not os.path.isdir(path):
                continue
            skip = ["__pycache__", sub + "utils.py", sub + "scenarios.py"]
            for item in os.listdir(path):
                if item in skip:
                    continue
                self.TestAModule(sub + "/" + os.path.splitext(item)[0])
        if self.undoc:
            self.fail("There are undocumented settings")


if __name__ == '__main__':
    unittest.main()

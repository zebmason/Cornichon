import os, os.path, sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Cornichon')
sys.path.insert(0, subdir)
import cornichon

def Process(stub, bit):

    f = open(stub + '.feature', "r")
    gherkin = f.readlines()
    f.close()

    settings = cornichon.Settings("py/pyunit_tests")
    settings["stub"] = stub
    settings["gherkin"] = gherkin
    settings["helpers"] = "helpers" + bit
    fp = open('tests' + bit + '.py', "w")
    fp.write(cornichon.Generate(settings, "py/pyunit_tests"))
    fp.close()

    settings = cornichon.Settings("py/pyhelpers")
    settings["gherkin"] = gherkin
    fp = open('helpers' + bit + '.py', "w")
    fp.write(cornichon.Generate(settings, "py/pyhelpers"))
    fp.close()

features = {}
features['cornichon'] = ''
features['units'] = '_units'
for stub in features:
    Process(stub, features[stub])

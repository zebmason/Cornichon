import os, os.path, sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Cornichon')
sys.path.insert(0, subdir)
import cornichon

settings = {}
settings["stub"] = 'cornichon'
settings["helpers"] = "helpers"

def Process(stub, bit):
    f = open(stub + '.feature', "r")
    settings["gherkin"] = f.readlines()
    f.close()

    fp = open('tests' + bit + '.py', "w")
    fp.write(cornichon.Generate(settings, "pyunit_tests"))
    fp.close()

    fp = open('helpers' + bit + '.py', "w")
    fp.write(cornichon.Generate(settings, "pyhelpers"))
    fp.close()

features = {}
features['cornichon'] = ''
features['units'] = '_units'
for stub in features:
    Process(stub, features[stub])

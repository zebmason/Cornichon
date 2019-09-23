import os, os.path, sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Cornichon')
sys.path.insert(0, subdir)
import cornichon

settings = {}
settings["stub"] = 'cornichon'
settings["rootnamespace"] = "Cornichon::"
settings["helpers"] = "helpers"

f = open('cornichon.feature', "r")
settings["gherkin"] = f.readlines()
f.close()

fp = open('tests.py', "w")
fp.write(cornichon.Generate(settings, "pyunit_tests"))
fp.close()

fp = open('helpers.py', "w")
fp.write(cornichon.Generate(settings, "pyhelpers"))
fp.close()

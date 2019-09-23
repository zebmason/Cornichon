import os
import os.path
import sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Cornichon')
sys.path.insert(0, subdir)
import cornichon

settings = {}
settings["rootnamespace"] = "Cornichon::"
settings["helpers"] = "../helpers/"

header = "// Copyright (c) 2019 ...\n\n"

for filename in os.listdir('Examples/tests'):
    inFileName = os.path.join('Examples/tests', filename)
    stub, ext = os.path.splitext(filename)
    if ext == '.feature':
        print(filename)
        settings["stub"] = stub
        f = open(inFileName, "r")
        settings["gherkin"] = f.readlines()
        f.close()
        
        ofilename = 'Examples/cppunittest/' + stub + ".cpp"
        if os.path.exists(ofilename):
            ofilename = 'Examples/cppunittest/' + stub + ".fpp"
        fp = open(ofilename, "w")
        fp.write(cornichon.Generate(settings, "cppunittest"))
        fp.close()
        
        ofilename = 'Examples/cpphelpers/' + stub + ".h"
        if os.path.exists(ofilename):
            ofilename = 'Examples/cpphelpers/' + stub + ".f"
        fp = open(ofilename, "w")
        fp.write(header + cornichon.Generate(settings, "cpphelpers"))
        fp.close()

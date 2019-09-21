import os
import os.path
import sys

subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Cornichon')
sys.path.insert(0, subdir)
import cornichon

settings = {}
settings["header"] = "// Copyright (c) 2019 ...\n\n"
settings["rootnamespace"] = "Cornichon::"

for filename in os.listdir('Examples/tests'):
    inFileName = os.path.join('Examples/tests', filename)
    stub, ext = os.path.splitext(filename)
    if ext == '.feature':
        print(filename)
        ofilename = 'Examples/cppunittest/' + stub + ".cpp"
        if os.path.exists(ofilename):
            #ofilename = stub + ".fpp"
            os.remove(ofilename)
        fp = open(ofilename, "w")
        settings["stub"] = stub
        settings["inFileName"] = inFileName
        fp.write(cornichon.Generate(settings))
        fp.close()

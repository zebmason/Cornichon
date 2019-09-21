import os
import os.path
import sys
import gherkin

for filename in os.listdir('.'):
    bits = os.path.splitext(filename)
    if bits[1] == '.feature':
        print filename
        ofilename = bits[0] + ".cpp"
        if os.path.exists(ofilename):
            ofilename = bits[0] + ".fpp"
        fp = file(ofilename, "w")
        fp.write(gherkin.Generate(filename))
        fp.close()

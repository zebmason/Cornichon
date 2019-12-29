import os
import os.path
import sys

curdir = os.path.dirname(os.path.realpath(__file__))
subdir = os.path.join(curdir, '../cornichon')
sys.path.insert(0, subdir)
import cornichon


def Process(stub):
    # Read the Gherkin DSL
    f = open(stub + '.feature', "r")
    gherkin = f.readlines()
    f.close()

    # Only need to call Settings for the test framework as it builds
    # on those settings for the scenarios
    settings = cornichon.Settings("py/pyunit_tests")
    settings["scenarios file"] = 'scenarios_' + stub

    # Overwrite the tests
    fp = open('test_' + stub + '.py', "w")
    fp.write(cornichon.Generate(gherkin, settings, "py/pyunit_tests"))
    fp.close()

    # Overwrite the test scenarios
    fp = open('scenarios_' + stub + '.py', "w")
    fp.write(cornichon.Generate(gherkin, settings, "py/pyscenarios"))
    fp.close()


features = ['cornichon', 'units', 'gherkin']
for stub in features:
    Process(stub)

# Cornichon

[![Build Status](https://api.travis-ci.org/zebmason/Cornichon.svg?branch=master)](https://travis-ci.org/zebmason/Cornichon)

## Introduction
A small Gherkin DSL parser which reads in a feature file and produces stub code
against a given test framework. This allows BDD to be integrated into new and existing
projects without the need to depend on [Cucumber](https://cucumber.io/).

The generated code is split into two files - the tests themselves and a set of scenario classes.
This is to allow for:
* easier version control of the source code
* re-use of the scenario classes generation between unit test frameworks for the same language

The parser is written in Python and loads plug-ins for the desired output type.

## Usage

A very basic test generator might look like
```
import cornichon


# Read the Gherkin DSL
f = open("example.feature", "r")
gherkin = f.readlines()
f.close()

# Only need to call Settings for the test framework as it builds
# on those settings for the scenarios
settings = cornichon.Settings("cpp/cppunittest")
settings["rootnamespace"] = "Cornichon::"
settings["scenarios file"] = "example.h"

# Generate the tests
fp = open("example.cpp", "w")
fp.write(cornichon.Generate(gherkin, settings, "cpp/cppunittest"))
fp.close()

# Generate the test scenarios
fp = open("example.h", "w")
fp.write(cornichon.Generate(gherkin, settings, "cpp/cppscenarios"))
fp.close()
```

The values of the settings can be listed,
```
cornichon.PrintSettings(settings)
```

An explanation of those values can be printed,
```
cornichon.HelpSettings("cpp/cppunittest")
```

The list of available output types can be printed,
```
cornichon.ListModules()
```

## Test frameworks

### C++

The scenario classes are generated using `cpp/cppscenarios`.

The supported frameworks are:
* `cpp/cppunittest` - Microsoft's Visual C++ test framework
* `cpp/googletest` - Google Test

### C#

The scenario classes are generated using `cs/csscenarios`.

The supported frameworks are:
* `cs/nunit` - NUnit
* `cs/unittesting` - Microsoft's Unit Testing framework

### Python

The scenario classes are generated using `py/pyscenarios`.

The supported frameworks are:
* `py/pytests` - pytest, the pytest framework
* `py/pyunit_tests` - unittest, the standard Python unit testing framework

### Visual Basic

The scenario classes are generated using `vb/vbscenarios`.

The supported frameworks are:
* `vb/nunit` - NUnit
* `vb/unittesting` - Microsoft's Unit Testing framework

## Contributing

Contributions are welcome. Please read the testing documentation.
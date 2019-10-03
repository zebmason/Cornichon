# Cornichon

## Introduction
A small Gherkin DSL parser that has evolved from a CodeProject article:
["A Slice of Cucumber"](https://www.codeproject.com/Articles/1084071/A-Slice-of-Cucumber).

The code comprises a Python script which reads in a feature file and produces stub code
against a given test framework. This allows BDD to be integrated into new and existing
projects without the need to depend on [Cucumber](https://cucumber.io/).

The generated code is split into two files - the tests themselves and a set of helper functions.
This is to allow for:
* easier version control of the source code
* re-use of the helper function generation between unit test frameworks for the same language

## Test frameworks

### C++

The helper functions are generated using `cpphelpers`.

The supported frameworks are:
* `cppunittest` - Microsoft's Visual C++ test framework
* `googletest` - Google Test

### C#

The helper functions are generated using `cshelpers`.

The supported frameworks are:
* `unittesting` - Microsoft's Unit Testing framework
* `nunit` - NUnit

### Python

The helper functions are generated using `pyhelpers`.

The supported frameworks are:
* `pyunit_tests` - unittest, the standard Python unit testing framework

## Usage

The main example of usage is in [features.py](./features.py).
This script generates both `cppunittest` and `cpphelpers` into separate subdirectories
from Gherkin DSL `.feature` files in another subdirectory. If the file to be generated
already exists then a mangled file extension is used to allow for easy identification
when the updated tests are diff'ed.

For the settings for the other generators please refer to the unit tests in
[helpers.py](./Tests/helpers.py).

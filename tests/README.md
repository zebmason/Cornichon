# Development and testing

## Introduction

This project uses Continuous Integration provided by [travis CI](https://travis-ci.com/)
which uses [tox](https://pypi.org/project/tox/). To execute the test suite
before submission run `python -m tox` in the root directory of the repository.

## Adding a new framework

1. Copy an existing framework generator, e.g. `/cornichon/cs/nunit.py`.
2. Add it to the tests in `/Tests/cornichon.feature`.
3. Regenerate the test code by running `/Tests/generate.py`.
4. Revert the changes to the Python files which aren't `/Tests/*_cornichon.py`.
5. Revert the changes to `/Tests/*_cornichon.py` which aren't additions and fill in the stub code.
6. Run `/Tests/tests_cornichon.py` to generate new stub code in `/Examples/output`.
7. Edit the new stub code to the form it should be for the new test framework.
8. Iterate between editing the framework generator and running `/Tests/tests_cornichon.py`

## Adding a new language

Roughly follow the procedure for adding a new framework but copy a whole
language directory, e.g. `/cornichon/cs`.

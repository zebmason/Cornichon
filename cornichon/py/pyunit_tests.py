import common
import pyutils


def Settings():
    settings = pyutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "snake"
    settings["scenarios file"] = "scenarios"
    return settings


def HelpSettings():
    settings = pyutils.HelpSettings()
    settings["scenarios file"] = "The generated scenarios to import"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]

    buffer = """
import unittest
from [[scenarios file]] import *


class [[className]](unittest.TestCase):
    [[comment]]

[[TestBody]]


if __name__ == '__main__':
    unittest.main()
"""[1:]

    className = common.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[className]]", className)
    buffer = buffer.replace("[[comment]]", '"""Gherkin DSL feature"""')
    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])

    py = pyutils.Python(settings)
    testBody = py.TestBody(scenarios, settings)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

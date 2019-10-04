import common
import pyutils
import gherkin


def Description(lines, indent):
    des = ''
    for line in lines.split('\n'):
        if line.strip() == '':
            continue
        line = '"%s"' % line
        line = line.replace(' + ""', '')
        line = line.replace(' "" + ', ' ')
        buffer = """
        print([[line]])"""
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]


def Steps(scenario, settings):
    concat = ""
    steps = []
    # parse the sections
    for s in scenario.Steps():
        lines = s[1].split('\n')
        step = gherkin.Step(s[0], s[1])
        camelCase = step.Tokenise(settings["cases"]["step"])
        if 0 != steps.count(camelCase):
            continue
        steps.append(camelCase)

        arguments = step.ArgumentList(scenario.examples.types, settings["types"])
        if len(arguments) > 0:
            arguments = ", " + arguments
        buffer = """
    def [[camelCase]](self[[arguments]]):
        [[comment]]
[[Description]]

"""[1:]
        buffer = buffer.replace("[[comment]]", '"""Gherkin DSL step"""')
        buffer = buffer.replace("[[camelCase]]", camelCase)
        buffer = buffer.replace("[[arguments]]", arguments)
        lines = "%s%s %s" % ('      ', s[0], s[1])
        description = Description(step.Sub(lines, '" + str(%s) + "'), '    ')
        buffer = buffer.replace("[[Description]]", description)
        concat += buffer
    return concat.rstrip()


def Settings():
    settings = pyutils.Settings()
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    lines = "%s%s %s" % ('  ', 'Feature:', feature)
    featureDesc = Description(lines, '  ')
    concat = """
import unittest

"""[1:]

    for scenario in scenarios:
        buffer = """
class [[Scenario]](unittest.TestCase):
    [[comment1]]
    def __init__(self):
        [[comment2]]
[[documentation]]

[[steps]]

"""

        buffer = buffer.replace("[[comment1]]", '"""Test class scenario"""')
        buffer = buffer.replace("[[comment2]]", '"""Initialiser"""')
        buffer = buffer.replace("[[steps]]", Steps(scenario, settings))
        scenarioName = common.Tokenise(scenario.lines + " Scenario", settings["cases"]["class"])
        buffer = buffer.replace("[[Scenario]]", scenarioName)
        lines = "%s%s %s" % ('    ', 'Scenario:', scenario.lines)
        desc = Description(lines, '    ')
        documentation = featureDesc + "\n" + desc
        buffer = buffer.replace("[[documentation]]", documentation)
        concat += buffer

    return concat

import common


def Description(section, lines, params, indent, lindent):
    des = ''
    first = True
    for line in lines:
        if line.strip() == '':
            continue
        if first:
            first = False
            line = "%s%s %s" % (indent, section, line)
        line = '"%s"' % line
        for i in range(len(params)):
            if params[i][0] == '<':
                sub = '" << %s << "' % params[i][1:-1]
                line = line.replace(params[i], sub)
                continue
            line = line.replace(params[i], '" << arg%d << "' % (i+1))
        line = line.replace(' << ""', '')
        line = line.replace(' "" << ', ' ')
        line = line.replace(' << ', ', ')
        buffer = """
        print([[line]])"""
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]


def Feature(feature, indent):
    lines = feature.split('\n')
    camelCase, args, params = common.CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ', indent)


def Steps(scenario):
    concat = ""
    steps = []
    # parse the sections
    for s in scenario.Steps():
        lines = s[1].split('\n')
        camelCase, args, params = common.CamelCase(s[0], lines[0])
        if 0 != steps.count(camelCase):
            continue
        steps.append(camelCase)

        arguments = common.Arguments(args, ', ')
        buffer = """
    def [[camelCase]](self[[arguments]]):
        [[comment]]
[[Description]]

"""[1:]
        buffer = buffer.replace("[[comment]]", '"""Gherkin DSL step"""')
        buffer = buffer.replace("[[camelCase]]", camelCase)
        buffer = buffer.replace("[[arguments]]", arguments)
        description = Description(s[0], lines, params, '      ', '    ')
        buffer = buffer.replace("[[Description]]", description)
        concat += buffer
    return concat.rstrip()


def Settings():
    settings = common.Settings()
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName, featureDesc = Feature(feature, '  ')
    concat = """
import unittest

"""[1:]

    for scenario in scenarios:
        buffer = """
class [[Helper]](unittest.TestCase):
    [[comment1]]
    def __init__(self):
        [[comment2]]
[[documentation]]

[[steps]]

"""

        buffer = buffer.replace("[[comment1]]", '"""Test class helper"""')
        buffer = buffer.replace("[[comment2]]", '"""Initialiser"""')
        buffer = buffer.replace("[[steps]]", Steps(scenario))
        helper = common.Camel(scenario.lines + " Helper")
        buffer = buffer.replace("[[Helper]]", helper)
        lines = scenario.lines.split('\n')
        desc = Description('Scenario:', lines, [], '    ', '    ')
        documentation = featureDesc + "\n" + desc
        buffer = buffer.replace("[[documentation]]", documentation)
        concat += buffer

    return concat

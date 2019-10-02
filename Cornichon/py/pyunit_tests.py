import common
import pyutils
import pyhelpers

def PrintScenario(scenario, arguments, steps, settings, indent):
    buffer = """
    def [[scenario]](self, [[arguments]]):
        [[comment]]
        helpers = [[scenario]]Helper()
[[steps]]
"""[1:]
    buffer = buffer.replace("[[comment]]", '"""Gherkin DSL scenario"""')
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[arguments]]", arguments)

    concat = ""
    for step in steps:
        concat += step + "\n"
    buffer = buffer.replace("[[steps]]", concat.rstrip())
    return buffer


def Scenarios(scenarios, settings, indent):
    concat = ""
    # parse the scenarios
    for s in scenarios:
        fullArgs = s.examples.ArgumentsList(settings["types"])
        steps = []
        for step in s.Steps():
            lines = step[1].split('\n')
            camelCase, args, params = common.CamelCase(step[0], lines[0])
            for i in range(len(params)):
                args[i] = params[i]
            arguments = common.Arguments(args, '', ', ')
            arguments = arguments.replace('<', '').replace('>', '')
            buffer = '        helpers.[[camelCase]]([[arguments]])'
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = common.CamelCase('Scenario:', lines[0])
        concat += PrintScenario(scenarioName, fullArgs, steps, settings, indent)
        concat += "\n"
    return concat.rstrip()


def ScenarioInsts(scenarios, settings, indent):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = common.CamelCase('Scenario:', lines[0])
        if s.examples.Exists():
            lines = s.examples.lines.split('\n')
            for line in lines[2:]:
                args = line.strip()[1:-2].replace('|', ' ')
                if '' == args:
                    continue
                testName = " ".join(["test", common.Lower(scenario), args])
                testName = common.SnakeCase(testName)
                arguments2 = s.examples.ArgumentsInstance(settings["values"], line, pyutils.ArgModifier)
                buffer = """
    def [[testName]](self):
        [[comment]]
        self.[[Scenario]]([[arguments2]])
"""
                buffer = buffer.replace("[[comment]]", '"""Gherkin DSL test"""')
                buffer = buffer.replace("[[scenario]]", common.Lower(scenario))
                buffer = buffer.replace("[[Scenario]]", scenario)
                buffer = buffer.replace("[[testName]]", testName)
                buffer = buffer.replace("[[arguments2]]", arguments2)
                concat += buffer
        else:
            buffer = """
    [[scenario]]Inst()
"""
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()


def Settings():
    settings = pyutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "snake"
    settings["helpers"] = "helpers"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    namespace = settings["stub"]
    namespace, args, params = common.CamelCase('', namespace)

    buffer = """
import unittest
from [[helpers]] import *


class [[namespace]](unittest.TestCase):
    [[comment]]

[[Scenarios]]
[[ScenarioInsts]]


if __name__ == '__main__':
    unittest.main()
"""[1:]

    buffer = buffer.replace("[[comment]]", '"""Gherkin DSL feature"""')
    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[namespace]]", namespace)
    sub = Scenarios(scenarios, settings, "  ")
    buffer = buffer.replace("[[Scenarios]]", sub)
    sub = ScenarioInsts(scenarios, settings, "  ")
    buffer = buffer.replace("[[ScenarioInsts]]", sub)

    return buffer

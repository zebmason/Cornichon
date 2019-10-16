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


class Python(pyutils.Python):
    def __init__(self, settings):
        super().__init__(settings)
        self.settings = settings
        self.testdecl = """

def test_{0}({1}):
    %s
"""[1:] % '"""Gherkin DSL test"""'
        self.step = '    scenario.[[method]]([[arguments]])\n'

    def PreScenarioDecl(self, fullArgs, examples, settings):
        concat = """
@pytest.mark.parametrize(
    "%s",
    [
""" % fullArgs
        lines = examples.lines.split('\n')
        for line in lines[2:]:
            if len(line.strip()) == 0:
                continue
            arguments = examples.ArgumentsInstance(settings["values"], line, self.argModifier)
            if "" == arguments:
                continue
            concat += """
        (
            %s,
        ),
"""[1:] % arguments
        return concat + """
    ],
)
"""[1:]

    def TestDecl(self, line, fullArgs):
        scenarioName = common.Tokenise(line, self.settings["cases"]["test"])
        return self.testdecl.format(scenarioName, fullArgs)

    def Scenario(self, scenario, settings):
        lines = scenario.lines.split('\n')
        if scenario.examples.Exists():
            fullArgs = scenario.examples.ArgumentsList(settings["types"])
            concat = self.PreScenarioDecl(fullArgs, scenario.examples, settings)
            return concat + self.TestDecl(lines[0], fullArgs)[1:]
        return self.TestDecl(lines[0], "")

    def Examples(self, scenarios, settings):
        return ""

    def Body(self, scenario, steps):
        buffer = """
    scenario = Scenarios.[[className]]()
[[steps]]

"""[1:]
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        buffer = buffer.replace("[[className]]", className)
        buffer = buffer.replace("[[steps]]", steps.rstrip())
        return buffer


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]

    buffer = """
import pytest
from [[scenarios file]] import *

[[TestBody]]
"""[1:]

    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])

    py = Python(settings)
    testBody = py.TestBody(scenarios, settings)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

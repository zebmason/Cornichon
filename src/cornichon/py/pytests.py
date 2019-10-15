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
        self.altdecl = """

def test_{0}():
    %s
"""[1:] % '"""Gherkin DSL test"""'

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

    def ScenarioDecl(self, line, fullArgs, examples, settings):
        concat = self.PreScenarioDecl(fullArgs, examples, settings)
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        decl = concat + """
def test_{0}({1}):
    {2}
"""[1:]
        return decl.format(scenarioName, fullArgs, '"""Gherkin DSL test"""')

    def TestDecl(self, line):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        return self.altdecl.format(scenarioName)

    def StepTemplate(self):
        return '    scenario.[[method]]([[arguments]])\n'

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

    def Example(self, line, arguments):
        return ""


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
    testBody = common.TestBody(scenarios, settings, py)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

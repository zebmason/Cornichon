import common
import gherkin


def Settings():
    settings = common.Settings()
    settings["cases"]["class"] = "Camel"
    settings["cases"]["param"] = "camel"
    settings["cases"]["step"] = "Camel"
    return settings


def HelpSettings():
    settings = common.HelpSettings()
    return settings


def ArgModifier(val, type):
    if type == "bool":
        return common.Upper(val)
    if type == "string":
        return val.replace('"', '\\"')
    return val


def FeatureName(feature, case):
    lines = feature.split('\n')
    camelCase = common.Tokenise(lines[0], case)
    return camelCase


class Python:
    def __init__(self, settings):
        self.settings = settings
        self.argModifier = ArgModifier
        self.altdecl = """
    def test_{0}(self):
        %s
"""[1:] % '"""Gherkin DSL test"""'

    @staticmethod
    def ScenarioBody(className, steps):
        buffer = """
        scenario = Scenarios.[[className]]()
[[steps]]
"""[1:]
        buffer = buffer.replace("[[className]]", className)

        concat = ""
        for step in steps:
            concat += step + "\n"
        buffer = buffer.replace("[[steps]]", concat.rstrip())
        return buffer

    def ScenarioDecl(self, line, fullArgs):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        decl = """
    def {0}({1}):
        {2}
"""[1:]
        if len(fullArgs) > 0:
            fullArgs = "self, " + fullArgs
        else:
            fullArgs = "self"
        return decl.format(scenarioName, fullArgs, '"""Gherkin DSL scenario"""')

    def TestDecl(self, line):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        return self.altdecl.format(scenarioName)

    def Body(self, scenario):
        steps = []
        for step in scenario.Steps():
            lines = step[1].split('\n')
            st = gherkin.Step(step[0], step[1])
            camelCase = st.Tokenise(self.settings["cases"]["step"])
            arguments = st.ParameterList(scenario.examples.types)
            buffer = '        scenario.[[camelCase]]([[arguments]])'
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        return Python.ScenarioBody(className, steps) + "\n"

    def Example(self, line, arguments):
        buffer = """
[[testName]]        self.[[scenario]]([[arguments]])
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.altdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

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


class Python(common.PrintTestBody):
    def __init__(self, settings):
        self.settings = settings
        self.argModifier = ArgModifier
        self.testdecl = """
    def test_{0}(self):
        %s
"""[1:] % '"""Gherkin DSL test"""'
        self.step = '        scenario.[[method]]([[arguments]])\n'

    def ScenarioDecl(self, line, fullArgs, settings):
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
        scenarioName = common.Tokenise(line, self.settings["cases"]["test"])
        return self.testdecl.format(scenarioName)

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
        buffer = """
[[testName]]        self.[[scenario]]([[arguments]])
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.testdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

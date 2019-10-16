import common
import gherkin


def Settings():
    settings = common.Settings()
    settings["rootnamespace"] = "Cornichon."
    settings["cases"]["class"] = "Camel"
    settings["cases"]["namespace"] = "Camel"
    settings["cases"]["param"] = "camel"
    settings["cases"]["step"] = "Camel"
    settings["types"]["bool"] = "{} As Boolean"
    settings["types"]["int"] = "{} As Integer"
    settings["types"]["uint"] = "{} As UInteger"
    settings["types"]["float"] = "{} As Double"
    settings["types"]["string"] = "{} As String"
    return settings


def HelpSettings():
    settings = common.HelpSettings()
    settings["rootnamespace"] = "The concatenated namespace ending in a ."
    settings["cases"]["namespace"] = settings["cases"]["class"]
    return settings


def ArgModifier(val, type):
    if type == "bool":
        return common.Lower(val)
    if type == "string":
        return val.replace('"', '\\"')
    return val


class VBasic(common.PrintTestBody):
    def __init__(self, settings, decorator):
        self.settings = settings
        self.argModifier = ArgModifier
        self.testdecl = """
    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <%s>
    Public Sub {0}()
"""[1:] % decorator
        self.step = '      scenario.[[method]]([[arguments]])\n'

    def ScenarioDecl(self, line, fullArgs, settings):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        decl = """
    ' <summary>
    ' Gherkin DSL scenario
    ' </summary>
    Private Shared Sub {0}({1})
"""[1:]
        return decl.format(scenarioName, fullArgs)

    def TestDecl(self, line):
        scenarioName = common.Tokenise(line, self.settings["cases"]["test"])
        return self.testdecl.format(scenarioName)

    def Body(self, scenario, steps):
        buffer = """
      Dim scenario As Scenarios.[[className]] = New Scenarios.[[className]]()
[[steps]]
    End Sub

"""[1:]
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        buffer = buffer.replace("[[className]]", className)
        buffer = buffer.replace("[[steps]]", steps.rstrip())
        return buffer

    def Example(self, line, arguments):
        buffer = """
[[testName]]      [[scenario]]([[arguments]])
    End Sub
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.testdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

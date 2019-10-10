import common
import gherkin


def Settings():
    settings = common.Settings()
    settings["rootnamespace"] = "Cornichon."
    settings["cases"]["class"] = "Camel"
    settings["cases"]["namespace"] = "Camel"
    settings["cases"]["param"] = "camel"
    settings["cases"]["step"] = "Camel"
    settings["types"]["bool"] = "bool {}"
    settings["types"]["int"] = "int {}"
    settings["types"]["uint"] = "uint {}"
    settings["types"]["float"] = "double {}"
    settings["types"]["string"] = "string {}"
    return settings


def HelpSettings():
    settings = common.HelpSettings()
    settings["rootnamespace"] = "The concatenated namespace ending in a ."
    settings["cases"]["namespace"] = settings["cases"]["class"]
    return settings


def Macro():
    settings = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings[type] = "_{}"
    return settings


def ArgModifier(val, type):
    if type == "bool":
        return common.Lower(val)
    if type == "string":
        return val.replace('"', '\\"')
    return val


def FeatureName(feature, case):
    lines = feature.split('\n')
    camelCase = common.Tokenise(lines[0], case)
    return camelCase


class CSharp:
    def __init__(self, settings, decorator):
        self.settings = settings
        self.argModifier = ArgModifier
        self.altdecl = """
    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [%s]
    public void {0}()
"""[1:] % decorator

    @staticmethod
    def ScenarioBody(className, steps):
        buffer = """
    {
      var scenario = new Scenarios.[[className]]();
[[steps]]
    }
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
    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void {0}({1})
"""[1:]
        return decl.format(scenarioName, fullArgs)

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
            buffer = '      scenario.[[camelCase]]([[arguments]]);'
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        return CSharp.ScenarioBody(className, steps) + "\n"

    def Example(self, line, arguments):
        buffer = """
[[testName]]    {
      [[scenario]]([[arguments]]);
    }
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.altdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

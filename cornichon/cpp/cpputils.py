import common
import gherkin


def Settings():
    settings = common.Settings()
    settings["rootnamespace"] = "Cornichon::"
    settings["cases"]["class"] = "Camel"
    settings["cases"]["namespace"] = "Camel"
    settings["cases"]["param"] = "camel"
    settings["cases"]["step"] = "Camel"
    settings["types"]["bool"] = "bool {}"
    settings["types"]["int"] = "int {}"
    settings["types"]["uint"] = "unsigned int {}"
    settings["types"]["float"] = "double {}"
    settings["types"]["string"] = "const std::string& {}"
    return settings


def HelpSettings():
    settings = common.HelpSettings()
    settings["rootnamespace"] = "The concatenated C++ 17 namespace ending in ::"
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


class Cpp:
    def __init__(self, settings, decl, altdecl, indent):
        self.settings = settings
        self.decl = decl
        self.altdecl = altdecl
        self.indent = indent
        self.argModifier = ArgModifier

    @staticmethod
    def ScenarioBody(className, steps, indent):
        buffer = """
[[indent]]{
[[indent]]  Scenarios::[[className]] scenario;
[[steps]]
[[indent]]}
"""[1:]
        buffer = buffer.replace("[[indent]]", indent)
        buffer = buffer.replace("[[className]]", className)

        concat = ""
        for step in steps:
            concat += step + "\n"
        buffer = buffer.replace("[[steps]]", concat.rstrip())
        return buffer

    def ScenarioDecl(self, line, fullArgs):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        return self.decl.format(scenarioName, fullArgs)

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
            buffer = '[[indent]]  scenario.[[camelCase]]([[arguments]]);'
            buffer = buffer.replace("[[indent]]", self.indent)
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        return Cpp.ScenarioBody(className, steps, self.indent) + "\n"

    def Example(self, line, arguments):
        buffer = """
[[testName]][[indent]]{
[[indent]]  [[scenario]]([[arguments]]);
[[indent]]}
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.altdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[indent]]", self.indent)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

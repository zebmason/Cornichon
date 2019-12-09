import common
import gherkin


def Settings():
    settings = common.Settings()
    settings["nested namespaces"] = "true"
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
    settings["nested namespaces"] = "Whether to use C++ 17 nested namespaces"
    settings["rootnamespace"] = "The concatenated C++ 17 namespace ending in ::"
    settings["cases"]["namespace"] = settings["cases"]["class"]
    return settings


def ArgModifier(val, type):
    if type == "bool":
        return common.Lower(val)
    if type == "string":
        return val.replace('"', '\\"')
    return val


class NameSpace:
    def __init__(self, settings, namespace):
        self.settings = settings
        self.namespace = settings["rootnamespace"] + namespace

    def Begin(self):
        if self.settings["nested namespaces"] == "true":
            return self.namespace
        return self.namespace.replace("::", " namespace { ")

    def End(self):
        if self.settings["nested namespaces"] == "true":
            return "}"
        num = self.namespace.count("::")
        val = "}"
        for i in range(num):
            val += " }"
        return val


class Cpp(common.PrintTestBody):
    def __init__(self, settings, decl, testdecl, indent):
        self.settings = settings
        self.decl = decl
        self.testdecl = testdecl
        self.indent = indent
        self.argModifier = ArgModifier
        self.step = self.indent + '  scenario.[[method]]([[arguments]]);\n'

    def ScenarioDecl(self, line, fullArgs, settings):
        scenarioName = common.Tokenise(line, self.settings["cases"]["scenario"])
        return self.decl.format(scenarioName, fullArgs)

    def TestDecl(self, line):
        scenarioName = common.Tokenise(line, self.settings["cases"]["test"])
        return self.testdecl.format(scenarioName)

    def Body(self, scenario, steps):
        buffer = """
[[indent]]{
[[indent]]  Scenarios::[[className]] scenario;
[[steps]]
[[indent]]}

"""[1:]
        buffer = buffer.replace("[[steps]]", steps.rstrip())
        buffer = buffer.replace("[[indent]]", self.indent)
        lines = scenario.lines.split('\n')
        className = common.Tokenise(lines[0], self.settings["cases"]["class"])
        buffer = buffer.replace("[[className]]", className)
        return buffer

    def Example(self, line, arguments):
        buffer = """
[[testName]][[indent]]{
[[indent]]  [[scenario]]([[arguments]]);
[[indent]]}
"""
        scenario = common.Tokenise(line, self.settings["cases"]["scenario"])
        testName = " ".join([scenario, arguments])
        testName = common.Tokenise(testName, self.settings["cases"]["test"])
        testName = self.testdecl.format(testName)
        buffer = buffer.replace("[[testName]]", testName)
        buffer = buffer.replace("[[indent]]", self.indent)
        buffer = buffer.replace("[[scenario]]", scenario)
        buffer = buffer.replace("[[arguments]]", arguments)
        return buffer

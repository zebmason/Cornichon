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


def PrintScenario(className, scenario, arguments, steps, settings):
    buffer = """
    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void [[scenario]]([[arguments]])
    {
      var scenario = new Scenarios.[[className]]();
[[steps]]
    }
"""[1:]
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[className]]", className)
    buffer = buffer.replace("[[arguments]]", arguments)

    concat = ""
    for step in steps:
        concat += step + "\n"
    buffer = buffer.replace("[[steps]]", concat.rstrip())
    return buffer


def FeatureName(feature, case):
    lines = feature.split('\n')
    camelCase = common.Tokenise(lines[0], case)
    return camelCase


def Scenarios(scenarios, settings, indent):
    concat = ""
    # parse the scenarios
    for s in scenarios:
        fullArgs = s.examples.ArgumentsList(settings["types"])
        steps = []
        for step in s.Steps():
            lines = step[1].split('\n')
            st = gherkin.Step(step[0], step[1])
            camelCase = st.Tokenise(settings["cases"]["step"])
            arguments = st.ParameterList(s.examples.types)
            buffer = '[[indent]]  scenario.[[camelCase]]([[arguments]]);'
            buffer = buffer.replace("[[indent]]", indent)
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = s.lines.split('\n')
        className = common.Tokenise(lines[0], settings["cases"]["class"])
        scenarioName = common.Tokenise(lines[0], settings["cases"]["scenario"])
        concat += PrintScenario(className, scenarioName, fullArgs, steps, settings)
        concat += "\n"
    return concat.rstrip()


def ScenarioInsts(scenarios, settings, decorator, indent):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario = common.Tokenise(lines[0], settings["cases"]["scenario"])
        if s.examples.Exists():
            lines = s.examples.lines.split('\n')
            for line in lines[2:]:
                if len(line.strip()) == 0:
                    continue
                arguments = s.examples.ArgumentsInstance(settings["values"], line, ArgModifier)
                if "" == arguments:
                    continue
                buffer = """
[[indent]]/// <summary>
[[indent]]/// Gherkin DSL test
[[indent]]/// </summary>
[[indent]][[[decorator]]]
[[indent]]public void [[testName]]()
[[indent]]{
[[indent]]  [[scenario]]([[arguments]]);
[[indent]]}
"""
                testName = " ".join([scenario, arguments])
                testName = common.Tokenise(testName, settings["cases"]["test"])
                buffer = buffer.replace("[[testName]]", testName)
                buffer = buffer.replace("[[decorator]]", decorator)
                buffer = buffer.replace("[[indent]]", indent)
                buffer = buffer.replace("[[scenario]]", scenario)
                buffer = buffer.replace("[[arguments]]", arguments)
                concat += buffer
        else:
            buffer = """
[[indent]][[scenario]]Inst();
"""
            buffer = buffer.replace("[[indent]]", indent)
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()

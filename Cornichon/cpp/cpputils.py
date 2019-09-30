import common, gherkin

def Settings():
    settings = common.Settings()
    settings["rootnamespace"] = "Cornichon::"
    settings["types"]["bool"] = "bool {}"
    settings["types"]["int"] = "int {}"
    settings["types"]["uint"] = "unsigned int {}"
    settings["types"]["float"] = "double {}"
    settings["types"]["string"] = "const std::string& {}"
    return settings

def Macro():
    settings = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings[type]   = "_{}"
    return settings

def Arguments(examples, header):
    settings = Macro()
    return common.ArgumentList(header, examples.types, settings, common.AsUpperSymbol)

def Concat(examples, header):
    settings = Macro()
    return common.ArgumentList(header, examples.types, settings, common.AsUpperSymbol, " ## ")

def Stringify(examples, header):
    settings = Macro()
    settings["string"] = "#_{}"
    return common.ArgumentList(header, examples.types, settings, common.AsUpperSymbol)

def PrintScenario(scenario, arguments, steps, documentation, settings, indent):
    buffer = """
[[indent]]static void [[scenario]]([[arguments]])
[[indent]]{
[[documentation]]
[[indent]]  [[rootnamespace]]Helpers::[[feature]] instance;
[[steps]]
[[indent]]}
"""[1:]
    buffer = buffer.replace("[[indent]]", indent)
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[arguments]]", arguments)
    buffer = buffer.replace("[[documentation]]", documentation)
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[feature]]", settings["feature"])
    
    concat = ""
    for step in steps:
        concat += step + "\n"
    buffer = buffer.replace("[[steps]]", concat.rstrip())
    return buffer

def Description(section, lines, params, indent, lindent):
    des = ''
    first = True
    for line in lines:
        if line.strip() == '':
            continue
        if first:
            first = False
            line = "%s%s %s" % (indent, section, line)
        line = '"%s"' % line
        for i in range(len(params)):
            if params[i][0] == '<':
                line = line.replace(params[i], '" << %s << "' % params[i][1:-1])
                continue
            line = line.replace(params[i], '" << arg%d << "' % (i+1))
        line = line.replace(' << ""', '')
        line = line.replace(' "" << ', ' ')
        buffer = """
[[indent]]  std::clog << [[line]] << std::endl;"""
        buffer = buffer.replace("[[indent]]", lindent)
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]

def Feature(feature, indent):
    lines = feature.split('\n')
    camelCase, args, params = common.CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ', indent)

def Scenarios(scenarios, feature, settings, indent):
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
            arguments = common.Arguments(args, '').replace('<', '').replace('>', '')
            buffer = '[[indent]]  instance.[[camelCase]]([[arguments]]);'
            buffer = buffer.replace("[[indent]]", indent)
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = common.CamelCase('Scenario:', lines[0])
        scenario = feature + "\n" + Description('Scenario:', lines, [], '    ', indent)
        concat += PrintScenario(scenarioName, fullArgs, steps, scenario, settings, indent)
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
                arguments = s.examples.ArgumentsInstance(settings["values"], line, common.BoolAsLower)
                if "" == arguments:
                    continue
                buffer = """
[[indent]][[scenario]]Inst([[arguments]]);
"""
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



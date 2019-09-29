def ExtractParams(line, delim1, delim2):
    params = []
    while True:
        i = line.find(delim1)
        if -1 == i:
            break
        j = line.find(delim2, i+1)
        if -1 == j:
            break
        params.append(line[i:j+1])
        line = line[:i] + line[j+1:]
    return line, params

def CamelCase(section, line):
    if 1 == ['Given', 'When', 'Then', 'But'].count(section):
        line = section + ' ' + line
    line, params = ExtractParams(line, '"', '"')
    line, p = ExtractParams(line, '<', '>')
    params.extend(p)
    
    line = line.replace('\'', ' Apostrophe ')
    line = line.replace('?', ' QuestionMark ')
    line = line.replace(':', ' Colon ')
    line = line.replace(',', '')
    line = line.replace('-', ' ')

    bits = line.split()
    cased = ''
    args = []
    for i in range(len(params)):
        if params[i][0] == '<':
            args.append(params[i][1:-1])
            continue
        args.append('arg%d' % (i+1))
    for bit in bits:
        cased += bit[0].upper() + bit[1:]
    return cased, args, params

def Arguments(args, type):
    arguments = ''
    for arg in args:
        arguments = "%s%s%s, " % (arguments, type, arg)
    if len(arguments) > 0:
        arguments = arguments[:-2]
    return arguments

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
    camelCase, args, params = CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ', indent)

def Scenarios(scenarios, feature, settings, indent):
    concat = ""
    # parse the scenarios
    for s in scenarios:
        fullArgs = ''
        if s.examples != '':
            args = ''
            lines = s.examples.split('\n')
            for line in lines[1:]:
                args = line.strip()[1:-2].replace('|', ' ')
                break
            fullArgs = Arguments(args.split(), 'std::string ')
        steps = []
        for step in s.Steps():
            lines = step[1].split('\n')
            camelCase, args, params = CamelCase(step[0], lines[0])
            for i in range(len(params)):
                args[i] = params[i]
            arguments = Arguments(args, '').replace('<', '').replace('>', '')
            buffer = '[[indent]]  instance.[[camelCase]]([[arguments]]);'
            buffer = buffer.replace("[[indent]]", indent)
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps.append(buffer)
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = CamelCase('Scenario:', lines[0])
        scenario = feature + "\n" + Description('Scenario:', lines, [], '    ', indent)
        concat += PrintScenario(scenarioName, fullArgs, steps, scenario, settings, indent)
        concat += "\n"
    return concat.rstrip()

def ScenarioInsts(scenarios, indent):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = CamelCase('Scenario:', lines[0])
        if s.examples != '':
            lines = s.examples.split('\n')
            for line in lines[2:]:
                args = line.strip()[1:-2].replace('|', ' ')
                if '' == args:
                    continue
                arguments = Arguments(args.split(), '')
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

def Type(value):
    if value == "true" or value == "True" or value == "false" or value == "False":
        return "bool"
    try:
        i = int(value)
        if i < 0:
            return "int"
        elif value == "0" or i > 0:
            return "uint"
    except:
        pass
    try:
        f = float(value)
        return "float"
    except:
        pass
    if value.isalnum():
        return "symbol"
    return "string"

def WorseComb(type, other, types, first):
    if type == types[0]:
        if other in types[1:]:
            return type
    if first:
        return WorseComb(other, type, types, False)
    return "none"

def Worst(other, type):
    if type == "none" or type == other:
        return other
    if other == "none":
        return type
    if type == "string" or other == "string":
        return "string"
    comb = WorseComb(type, other, ["int", "uint"], True)
    if comb != "none":
        return comb
    comb = WorseComb(type, other, ["symbol", "uint"], True)
    if comb != "none":
        return comb
    comb = WorseComb(type, other, ["float", "int", "uint"], True)
    if comb != "none":
        return comb
    return "string"

def Argument(arg, type, templates):
    if type == "symbol":
        return Argument(arg, "string", templates)
    return templates[type].format(arg)

def Tokenise(arg):
    return ''.join([i for i in arg if i.isalnum()])
    
def SnakeCase(line):
    line = line.replace(" ", "_")
    line = ''.join([i for i in line if (i.isalnum() or i == "_")])
    while line.find("__") != -1:
        line = line.replace("__", "_")
    while line[-1] == "_":
        line = line[:-1]
    return line

def Upper(word):
    return word[0].upper() + word[1:]

def Lower(word):
    return word[0].lower() + word[1:]

def Camel(line):
    return ''.join([Upper(i) for i in line.split()])

def Settings(language):
    settings = {}
    settings["gherkin"] = ""
    settings["types"] = {}
    settings["values"] = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings["types"][type] = "{}"
        settings["values"][type] = "{}"
    
    settings["values"]["string"] = "\"{}\""
    if language == "cpp":
        settings["rootnamespace"] = "Cornichon::"
        settings["types"]["bool"] = "bool {}"
        settings["types"]["int"] = "int {}"
        settings["types"]["uint"] = "unsigned int {}"
        settings["types"]["float"] = "double {}"
        settings["types"]["string"] = "const std::string& {}"
    elif language == "python":
        pass
    return settings

def SymbolToString(type):
    if type == "symbol":
        return "string"
    return type

def BoolAsUpper(val, type):
    if type == "bool":
        return Upper(val)
    return val

def BoolAsLower(val, type):
    if type == "bool":
        return Lower(val)
    return val

def BoolAsIs(val, type):
    return val

def ArgumentList(args, types, formats, boolModifier):
    if len(args) == 0:
        return ""
    
    line = ""
    for i in range(len(args)):
        type = SymbolToString(types[i])
        line = "{}, {}".format(line, formats[type].format(boolModifier(args[i], type)))
    
    return line[2:]

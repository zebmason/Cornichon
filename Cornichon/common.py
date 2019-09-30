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

def Arguments(args, type, joiner = ", "):
    arguments = ''
    for arg in args:
        arguments = "%s%s%s%s" % (arguments, type, arg, joiner)
    if len(arguments) > 0:
        arguments = arguments[:-len(joiner)]
    return arguments

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

def Settings():
    settings = {}
    settings["gherkin"] = ""
    settings["types"] = {}
    settings["values"] = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings["types"][type] = "{}"
        settings["values"][type] = "{}"
    
    settings["values"]["string"] = "\"{}\""
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

def AsSymbol(val, type):
    return val

def AsUpperSymbol(val, type):
    return val.upper()

def ArgumentList(args, types, formats, argModifier, sep = ", "):
    if len(args) == 0:
        return ""
    
    line = ""
    for i in range(len(args)):
        type = SymbolToString(types[i])
        bit = formats[type].format(argModifier(args[i], type))
        if len(bit.strip()) == 0:
            continue
        line = "{}{}{}".format(line, sep, bit)
    
    return line[len(sep):]

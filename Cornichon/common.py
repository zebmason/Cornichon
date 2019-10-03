def ExtractParams(line, delim1, delim2):
    params = []
    while True:
        i = line.find(delim1)
        if -1 == i:
            break
        j = line.find(delim2, i + 1)
        if -1 == j:
            break
        params.append(line[i:j + 1])
        line = line[:i] + line[j + 1:]
    return line, params


def Argument(arg, type, templates):
    if type == "symbol":
        return Argument(arg, "string", templates)
    return templates[type].format(arg)


def Tokenise(line, case=""):
    line = ''.join([i for i in line if (i.isalnum() or i == " ")])
    while line.find("  ") != -1:
        line = line.replace("  ", " ")

    if case == "Camel":
        return ''.join([Upper(i) for i in line.split()])
    elif case == "camel":
        return ''.join([Lower(i) for i in line.split()])
    elif case == "snake":
        return '_'.join([Lower(i) for i in line.split()])

    return line.replace(" ", "")


def Upper(word):
    return word[0].upper() + word[1:]


def Lower(word):
    return word[0].lower() + word[1:]


def Settings():
    settings = {}
    settings["gherkin"] = ""
    settings["cases"] = {}
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


def AsSymbol(val, type):
    return val


def AsUpperSymbol(val, type):
    return val.upper()


def ArgumentList(args, types, formats, argModifier, sep=", "):
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

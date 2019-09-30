import common

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

import common


def Settings():
    settings = common.Settings()
    settings["cases"]["class"] = "Camel"
    settings["cases"]["param"] = "camel"
    settings["cases"]["step"] = "Camel"
    return settings


def HelpSettings():
    settings = common.HelpSettings()
    return settings


def ArgModifier(val, type):
    if type == "bool":
        return common.Upper(val)
    if type == "string":
        return val.replace('"', '\\"')
    return val


def FeatureName(feature, case):
    lines = feature.split('\n')
    camelCase = common.Tokenise(lines[0], case)
    return camelCase

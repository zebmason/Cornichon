import common


def ArgModifier(val, type):
    if type == "bool":
        return common.Upper(val)
    if type in ["string", "symbol"]:
        return val.replace('"', '\\"')
    return val

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

class Scenario:
    def __init__(self, lines, background):
        self.lines = lines
        self.background = background
        self.steps = []
        self.examples = ''

    def Steps(self):
        steps = []
        steps.extend(self.background)
        steps.extend(self.steps)
        return steps

def GetScenarios(sections):
    scenarios = []
    feature = None
    background = []
    for section in sections:
        if 1 == ['Given', 'When', 'Then', 'But', 'And'].count(section[0]):
            if scenarios == []:
                background.append(section)
            else:
                scenarios[-1].steps.append(section)
        elif 'Feature:' == section[0]:
            feature = section[1]
        elif 'Examples:' == section[0]:
            scenarios[-1].examples = section[1]
        elif 'Scenario:' == section[0]:
            scenarios.append(Scenario(section[1], background))
    return [scenarios, feature]

def GetSections(settings):
    section = ''
    sections = []
    for line in settings["gherkin"]:
        if line.lstrip()[:1] == '#':
            continue
        bits = line.split()
        if len(bits) > 0 and 1 == ['Feature:', 'Scenario:', 'Examples:', 'Given', 'When', 'Then', 'But', 'And'].count(bits[0]):
            if bits[0] != 'And':
                section = bits[0]
            line = ' '.join(bits[1:]) + '\n'
            sections.append([section, line])
        elif len(bits) > 2 and ' '.join(bits[:2]) == 'Scenario Outline:':
            line = ' '.join(bits[2:]) + '\n'
            sections.append(['Scenario:', line])
        elif line.strip() == 'Background:':
            continue
        else:
            sections[-1][1] += line
    return sections

def Parse(settings):
    sections = GetSections(settings)
    return GetScenarios(sections)

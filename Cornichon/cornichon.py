import importlib

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
    return scenarios, feature

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

def Generate(settings, output):
    sections = GetSections(settings)
    scenarios, feature = GetScenarios(sections)
    
    mod = importlib.import_module(output)
    return mod.Generate(scenarios, feature, settings)

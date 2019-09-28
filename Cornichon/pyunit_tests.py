import common

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

def Arguments(args, type, joiner):
    arguments = ''
    for arg in args:
        arguments = "%s%s%s%s" % (arguments, type, arg, joiner)
    if len(arguments) > 0:
        arguments = arguments[:-len(joiner)]
    return arguments

def PrintScenario(scenario, arguments, steps, documentation, settings, indent):
    buffer = """
    def [[scenario]](self,[[arguments]]):
[[documentation]]
        helpers = Helpers()
[[steps]]
"""[1:]
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[arguments]]", arguments)
    buffer = buffer.replace("[[documentation]]", documentation)
    
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
        print([[line]])"""
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
            fullArgs = Arguments(args.split(), ' ', ', ')
        steps = []
        for step in s.Steps():
            lines = step[1].split('\n')
            camelCase, args, params = CamelCase(step[0], lines[0])
            for i in range(len(params)):
                args[i] = params[i]
            arguments = Arguments(args, '', ', ').replace('<', '').replace('>', '')
            buffer = '        helpers.[[camelCase]]([[arguments]]);'
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
                testName = " ".join(["test", scenario[0].lower() + scenario[1:], args])
                testName = common.SnakeCase(testName)
                arguments2 = Arguments(args.split(), '', ', ')
                buffer = """
    def [[testName]](self):
        self.[[Scenario]]([[arguments2]])
"""
                buffer = buffer.replace("[[scenario]]", scenario[0].lower() + scenario[1:])
                buffer = buffer.replace("[[Scenario]]", scenario)
                buffer = buffer.replace("[[testName]]", testName)
                buffer = buffer.replace("[[arguments2]]", arguments2)
                concat += buffer
        else:
            buffer = """
    [[scenario]]Inst();
"""
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()

def Generate(scenarios, feature, settings):
    namespace = settings["stub"]
    namespace, args, params = CamelCase('', namespace)
    
    featureName, featureDesc = Feature(feature, '  ')
    settings["feature"] = featureName

    buffer = """
import unittest
from [[helpers]] import *

class [[namespace]](unittest.TestCase):

[[Scenarios]]
[[ScenarioInsts]]

if __name__ == '__main__':
    unittest.main()
"""[1:]

    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[namespace]]", namespace)
    buffer = buffer.replace("[[Scenarios]]", Scenarios(scenarios, featureDesc, settings, "  "))
    buffer = buffer.replace("[[ScenarioInsts]]", ScenarioInsts(scenarios, "  "))

    return buffer

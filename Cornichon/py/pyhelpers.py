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

def Arguments(args, type):
    arguments = ''
    for arg in args:
        arguments = "%s%s%s, " % (arguments, type, arg)
    if len(arguments) > 0:
        arguments = arguments[:-2]
    return arguments

def Description(section, lines, params, indent, lindent):
    des = ''
    first = True
    for line in lines:
        if line.strip() == '':
            continue
        if first:
            first = False
            line = '"%s%s %s' % (indent, section, line)
        for i in range(len(params)):
            if params[i][0] == '<':
                line = line.replace(params[i], '", %s' % params[i][1:-1])
                continue
            line = line.replace(params[i], ', arg%d' % (i+1))
        buffer = """
        print([[line]])"""
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]

def Feature(feature, indent):
    lines = feature.split('\n')
    camelCase, args, params = CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ', indent)

def Steps(scenario):
    concat = ""
    steps = []
    # parse the sections
    for s in scenario.Steps():
        lines = s[1].split('\n')
        camelCase, args, params = CamelCase(s[0], lines[0])
        if 0 != steps.count(camelCase):
            continue
        steps.append(camelCase)

        arguments = Arguments(args, ', ')
        buffer = """
    def [[camelCase]](self[[arguments]]):
[[Description]]

"""[1:]
        buffer = buffer.replace("[[camelCase]]", camelCase)
        buffer = buffer.replace("[[arguments]]", arguments)
        buffer = buffer.replace("[[Description]]", Description(s[0], lines, params, '      ', '    '))
        concat += buffer
    return concat.rstrip()

def Settings():
    settings = common.Settings()
    return settings

def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    concat = """
import unittest
"""[1:]

    for scenario in scenarios:
        buffer = """
class [[Helper]](unittest.TestCase):
[[steps]]
"""

        buffer = buffer.replace("[[steps]]", Steps(scenario))
        buffer = buffer.replace("[[Helper]]", common.Camel(scenario.lines + " Helper"))
        concat += buffer

    return concat
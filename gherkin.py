import sys


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


def PrintScenario(scenario, arguments, feature, steps, documentation):
    buffer = ""
    buffer += """
        static void %s(%s)
        {
"""[1:] % (scenario, arguments)
    buffer += documentation
    buffer += """
            %s instance;
""" % feature
    for step in steps:
        buffer += step + "\n"
    buffer += """
        }
"""[1:]
    return buffer


def Description(section, lines, params, indent):
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
        des += """
            std::clog << %s << std::endl;""" % line
    return des[1:]


def Feature(feature):
    lines = feature.split('\n')
    camelCase, args, params = CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ')


def Steps(scenarios):
    buffer = ""
    steps = []
    # parse the sections
    for scenario in scenarios:
        for s in scenario.Steps():
            lines = s[1].split('\n')
            camelCase, args, params = CamelCase(s[0], lines[0])
            if 0 != steps.count(camelCase):
                continue
            steps.append(camelCase)

            arguments = Arguments(args, 'std::string ')
            buffer += """
        void %s(%s)
        {
%s
        }

"""[1:] % (camelCase, arguments, Description(s[0], lines, params, '      '))
    return buffer


def Scenarios(scenarios, featureName, feature):
    buffer = ""
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
            steps.append('            instance.%s(%s);' % (camelCase, arguments))
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = CamelCase('Scenario:', lines[0])
        scenario = feature + "\n" + Description('Scenario:', lines, [], '    ')
        buffer += PrintScenario(scenarioName, fullArgs, featureName, steps, scenario)
        buffer += "\n"
    return buffer


def ScenarioInsts(scenarios):
    buffer = ""
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
                buffer += """
        %sInst(%s);
""" % (scenario, arguments)
        else:
            buffer += """
        %sInst();
""" % (scenario)
    return buffer


def TestMethods(scenarios):
    buffer = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = CamelCase('Scenario', lines[0])

        if s.examples != '':
            args = ''
            lines = s.examples.split('\n')
            for line in lines[1:]:
                args = line.strip()[1:-2].replace('|', ' ').upper()
                break
            arguments = Arguments(args.split(), '_')
            concat = arguments.replace(', _', ' ## _')
            stringify = arguments.replace('_', '#_')
            buffer += """
#define %sInst(%s) \\
    TEST_METHOD(%s ## %s) \\
    { \\
        %s(%s); \\
    }

"""[1:] % (scenario, arguments, scenario, concat, scenario, stringify)
        else:
            buffer += """
#define %sInst() \\
    TEST_METHOD(%s ## Impl) \\
    { \\
        %s(); \\
    }

"""[1:] % (scenario, scenario, scenario)
    return buffer


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


def GetSections(filename):
    section = ''
    sections = []
    for line in open(filename):
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


def Tabify(lines):
    lines = lines.replace('\n            ', '\n\t\t\t')
    lines = lines.replace('\n        ', '\n\t\t')
    lines = lines.replace('\n    ', '\n\t')
    return lines


def Generate(filename):
    sections = GetSections(filename)
    scenarios, feature = GetScenarios(sections)
    lines = GenerateCpp(scenarios, feature, filename)
    return Tabify(lines)


def GenerateCpp(scenarios, feature, filename):
    buffer = """
#include "stdafx.h"
#include "CppUnitTest.h"

#include "TestUtils/LogStream.h"

#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

"""[1:]

    # Print the macros
    buffer += TestMethods(scenarios)
    buffer += "\n"

    # start the namespace
    namespace = filename.split('.')[0]
    namespace, args, params = CamelCase('', namespace)
    buffer += """
namespace %s
{
"""[1:] % namespace

    # Print the class
    featureName, featureDesc = Feature(feature)
    buffer += """
    TEST_CLASS(%s)
    {
        static std::streambuf* oldBuffer;
        static std::shared_ptr<std::streambuf> newBuffer;

"""[1:] % featureName
    buffer += Steps(scenarios)
    buffer += Scenarios(scenarios, featureName, featureDesc)
    buffer += """

        TEST_CLASS_INITIALIZE(ClassInitialize)
        {
            newBuffer = std::make_shared<TestUtils::LogStream>();
            oldBuffer = std::clog.rdbuf(newBuffer.get());
            std::clog << "Entering %s" << std::endl;
        }

        TEST_CLASS_CLEANUP(ClassCleanup)
        {
            std::clog << "Exiting %s" << std::endl;
            std::clog.rdbuf(oldBuffer);
            newBuffer = nullptr;
        }

    public:
"""[1:] % (namespace, namespace)
    buffer += ScenarioInsts(scenarios)
    buffer += """
    };

    std::streambuf* %s::oldBuffer = nullptr;
    std::shared_ptr<std::streambuf> %s::newBuffer = nullptr;
}

"""[1:] % (featureName, featureName)

    return buffer

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(Generate(sys.argv[1]))

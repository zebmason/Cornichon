from common import *

def PrintScenario(scenario, arguments, steps, documentation, settings):
    buffer = """
  static void [[scenario]]([[arguments]])
  {
[[documentation]]
    [[rootnamespace]]Helpers::[[feature]] instance;
[[steps]]
  }
"""[1:]
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[arguments]]", arguments)
    buffer = buffer.replace("[[documentation]]", documentation)
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[feature]]", settings["feature"])
    
    concat = ""
    for step in steps:
        concat += step + "\n"
    buffer = buffer.replace("[[steps]]", concat.rstrip())
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
    concat = ""
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
            buffer = """
    void [[camelCase]]([[arguments]])
    {
[[Description]]
    }

"""[1:]
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[Description]]", Description(s[0], lines, params, '      '))
            concat += buffer
    return concat

def Scenarios(scenarios, feature, settings):
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
            steps.append('    instance.%s(%s);' % (camelCase, arguments))
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = CamelCase('Scenario:', lines[0])
        scenario = feature + "\n" + Description('Scenario:', lines, [], '    ')
        buffer += PrintScenario(scenarioName, fullArgs, steps, scenario, settings)
        buffer += "\n"
    return buffer.rstrip()

def ScenarioInsts(scenarios):
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
                arguments = Arguments(args.split(), '')
                concat += """
  %sInst(%s);
""" % (scenario, arguments)
        else:
            concat += """
  %sInst();
""" % (scenario)
    return concat.rstrip()

def TestMethods(scenarios, namespace):
    concat = ""
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
            concat2 = arguments.replace(', _', ' ## _')
            stringify = arguments.replace('_', '#_')
            buffer = """
#define [[scenario]]Inst([[arguments]]) \\
  TEST([[namespace]], [[scenario]] ## [[concat2]]) \\
  { \\
    [[scenario]]([[stringify]]); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[namespace]]", namespace)
            buffer = buffer.replace("[[concat2]]", concat2)
            buffer = buffer.replace("[[stringify]]", stringify)
            concat += buffer
        else:
            buffer = """
#define [[scenario]]Inst() \\
  TEST([[namespace]], [[scenario]] ## Impl) \\
  { \\
    [[scenario]](); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            buffer = buffer.replace("[[namespace]]", namespace)
            concat += buffer
    return concat

def Generate(scenarios, feature, settings):
    namespace = settings["stub"]
    namespace, args, params = CamelCase('', namespace)
    
    featureName, featureDesc = Feature(feature)
    settings["feature"] = featureName

    buffer = """
// Other bespoke headers
#include "[[helpers]][[stub]].h"

// Third party headers
#include "gtest/gtest.h"

[[TestMethods]]namespace [[rootnamespace]][[namespace]]
{
[[Scenarios]]
[[ScenarioInsts]]
}
"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])
    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[TestMethods]]", TestMethods(scenarios, namespace))
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)
    buffer = buffer.replace("[[Scenarios]]", Scenarios(scenarios, featureDesc, settings))
    buffer = buffer.replace("[[ScenarioInsts]]", ScenarioInsts(scenarios))

    return buffer

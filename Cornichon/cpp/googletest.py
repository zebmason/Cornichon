import common

def Steps(scenarios):
    concat = ""
    steps = []
    # parse the sections
    for scenario in scenarios:
        for s in scenario.Steps():
            lines = s[1].split('\n')
            camelCase, args, params = common.CamelCase(s[0], lines[0])
            if 0 != steps.count(camelCase):
                continue
            steps.append(camelCase)

            arguments = common.Arguments(args, 'std::string ')
            buffer = """
    void [[camelCase]]([[arguments]])
    {
[[Description]]
    }

"""[1:]
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[Description]]", common.Description(s[0], lines, params, '      ', '      '))
            concat += buffer
    return concat

def TestMethods(scenarios, namespace):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = common.CamelCase('Scenario', lines[0])

        if s.examples != '':
            args = ''
            lines = s.examples.split('\n')
            for line in lines[1:]:
                args = line.strip()[1:-2].replace('|', ' ').upper()
                break
            arguments = common.Arguments(args.split(), '_')
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

def Settings():
    settings = common.Settings("cpp")
    settings["helpers"] = "../helpers/"
    return settings

def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    namespace = settings["stub"]
    namespace, args, params = common.CamelCase('', namespace)
    
    featureName, featureDesc = common.Feature(feature, '  ')
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
    buffer = buffer.replace("[[Scenarios]]", common.Scenarios(scenarios, featureDesc, settings, "  "))
    buffer = buffer.replace("[[ScenarioInsts]]", common.ScenarioInsts(scenarios, "  "))

    return buffer

import common
import cpputils

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
[[indent]]  std::clog << [[line]] << std::endl;"""
        buffer = buffer.replace("[[indent]]", lindent)
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]

def FeatureDesc(feature, indent):
    lines = feature.split('\n')
    return Description('Feature:', lines, [], '  ', indent)

def Documentation(scenario, feature, settings, indent):
    lines = scenario.lines.split('\n')
    return feature + "\n" + Description('Scenario:', lines, [], '    ', indent)

def Steps(scenarios, settings):
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

            arguments = common.ArgumentList(args, scenario.examples.types, settings["types"], common.AsSymbol)
            buffer = """
    void [[camelCase]]([[arguments]])
    {
[[Description]]
    }

"""[1:]
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[Description]]", Description(s[0], lines, params, '      ', '    '))
            concat += buffer
    return concat.rstrip()

def Settings():
    settings = cpputils.Settings()
    return settings

def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = cpputils.FeatureName(feature)
    featureDesc = FeatureDesc(feature, '    ')

    concat = """
#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace [[rootnamespace]]Helpers
{
"""[1:]
    concat = concat.replace("[[rootnamespace]]", settings["rootnamespace"])

    for scenario in scenarios:
        buffer = """
  class [[featureName]]
  {
  public:
    [[featureName]]()
    {
[[documentation]]
    }

[[steps]]
  };

"""[1:]

        buffer = buffer.replace("[[featureName]]", common.Camel(scenario.lines))
        documentation = Documentation(scenario, featureDesc, settings, "    ")
        buffer = buffer.replace("[[documentation]]", documentation)
        buffer = buffer.replace("[[steps]]", Steps(scenarios, settings))
        concat += buffer
    
    concat = concat[:-2] + """
}
"""
    return concat
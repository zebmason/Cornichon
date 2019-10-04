import common
import cpputils
import gherkin


def Description(lines, indent):
    des = ''
    for line in lines.split('\n'):
        if line.strip() == '':
            continue
        line = '"%s"' % line
        line = line.replace(' << ""', '')
        line = line.replace(' "" << ', ' ')
        buffer = """
[[indent]]  std::clog << [[line]] << std::endl;"""
        buffer = buffer.replace("[[indent]]", indent)
        buffer = buffer.replace("[[line]]", line)
        des += buffer
    return des[1:]


def FeatureDesc(feature, indent):
    lines = feature.split('\n')
    lines = "%s%s %s" % ('  ', 'Feature:', feature)
    return Description(lines, indent)


def Documentation(scenario, feature, settings, indent):
    lines = scenario.lines.split('\n')
    lines = "%s%s %s" % ('    ', 'Scenario:', scenario.lines)
    description = Description(lines, indent)
    return feature + "\n" + description


def Steps(scenarios, settings):
    concat = ""
    steps = []
    # parse the sections
    for scenario in scenarios:
        for s in scenario.Steps():
            lines = s[1].split('\n')
            step = gherkin.Step(s[0], s[1])
            camelCase = step.Tokenise(settings["cases"]["step"])
            if 0 != steps.count(camelCase):
                continue
            steps.append(camelCase)

            arguments = step.ArgumentList(scenario.examples.types, settings["types"])
            buffer = """
    /// Gherkin DSL step
    void [[camelCase]]([[arguments]])
    {
[[Description]]
    }

"""[1:]
            buffer = buffer.replace("[[camelCase]]", camelCase)
            buffer = buffer.replace("[[arguments]]", arguments)
            lines = "%s%s %s" % ('      ', s[0], s[1])
            description = Description(step.Sub(lines, '" << %s << "'), '    ')
            buffer = buffer.replace("[[Description]]", description)
            concat += buffer
    return concat.rstrip()


def Settings():
    settings = cpputils.Settings()
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = cpputils.FeatureName(feature, settings["cases"]["namespace"])
    featureDesc = FeatureDesc(feature, '    ')

    concat = """
#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace [[rootnamespace]][[namespace]]::Scenarios
{
"""[1:]

    namespace = common.Tokenise(featureName, settings["cases"]["namespace"])
    concat = concat.replace("[[rootnamespace]]", settings["rootnamespace"])
    concat = concat.replace("[[namespace]]", namespace)

    for scenario in scenarios:
        buffer = """
  /// Test class scenario
  class [[featureName]]
  {
  public:
    /// Constructor
    [[featureName]]()
    {
[[documentation]]
    }

[[steps]]
  };

"""[1:]

        buffer = buffer.replace("[[featureName]]", common.Tokenise(scenario.lines, settings["cases"]["class"]))
        documentation = Documentation(scenario, featureDesc, settings, "    ")
        buffer = buffer.replace("[[documentation]]", documentation)
        buffer = buffer.replace("[[steps]]", Steps(scenarios, settings))
        concat += buffer

    concat = concat[:-2] + """
}
"""
    return concat

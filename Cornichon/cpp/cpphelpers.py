import common
import cpputils

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
            buffer = buffer.replace("[[Description]]", cpputils.Description(s[0], lines, params, '      ', '    '))
            concat += buffer
    return concat.rstrip()

def Settings():
    settings = cpputils.Settings()
    return settings

def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName, featureDesc = cpputils.Feature(feature, '  ')

    buffer = """
#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace [[rootnamespace]]Helpers
{
  class [[featureName]]
  {
  public:

[[steps]]
  };
}
"""[1:]

    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[steps]]", Steps(scenarios, settings))
    return buffer
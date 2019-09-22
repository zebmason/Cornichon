from common import *

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
            buffer = buffer.replace("[[Description]]", Description(s[0], lines, params, '      ', '    '))
            concat += buffer
    return concat.rstrip()

def Generate(scenarios, feature, settings):
    featureName, featureDesc = Feature(feature, '  ')

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
    buffer = buffer.replace("[[steps]]", Steps(scenarios))
    return buffer
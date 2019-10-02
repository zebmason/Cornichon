import common
import cpputils


def TestMethods(scenarios, namespace):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = common.CamelCase('Scenario', lines[0])

        if s.examples.Exists():
            header = s.examples.Header()
            arguments = cpputils.Arguments(s.examples, header)
            concat2 = cpputils.Concat(s.examples, header)
            stringify = cpputils.Stringify(s.examples, header)

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
    settings = cpputils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    settings["helpers"] = "../helpers/"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    namespace = settings["stub"]
    namespace, args, params = common.CamelCase('', namespace)

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
    buffer = buffer.replace("[[Scenarios]]", cpputils.Scenarios(namespace, scenarios, settings, "  "))
    buffer = buffer.replace("[[ScenarioInsts]]", cpputils.ScenarioInsts(scenarios, settings, "  "))

    return buffer

import common
import cpputils


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
    namespace = common.Tokenise(namespace, settings["cases"]["namespace"])

    buffer = """
// Other bespoke headers
#include "[[helpers]][[stub]].h"

// Third party headers
#include "gtest/gtest.h"

namespace [[rootnamespace]][[namespace]]
{
[[Scenarios]]
[[ScenarioInsts]]
}
"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])
    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)
    buffer = buffer.replace("[[Scenarios]]", cpputils.Scenarios(namespace, scenarios, settings, "  "))
    stub = "TEST(%s, " % namespace
    insts = cpputils.ScenarioInsts(scenarios, settings, stub, "  ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

import common
import cpputils


def Settings():
    settings = cpputils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    settings["scenarios file"] = "../scenarios/scenarios.h"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = cpputils.FeatureName(feature, settings["cases"]["namespace"])
    namespace = common.Tokenise(featureName, settings["cases"]["namespace"])

    buffer = """
// Other bespoke headers
#include "[[scenarios file]]"

// Third party headers
#include "gtest/gtest.h"

namespace [[rootnamespace]][[namespace]]
{
[[Scenarios]]
[[ScenarioInsts]]
}
"""[1:]

    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)
    buffer = buffer.replace("[[Scenarios]]", cpputils.Scenarios(namespace, scenarios, settings, "  "))
    stub = "TEST(%s, " % namespace
    insts = cpputils.ScenarioInsts(scenarios, settings, stub, "  ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

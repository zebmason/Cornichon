import common
import cpputils


def Settings():
    settings = cpputils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    settings["scenarios file"] = "../scenarios/scenarios.h"
    return settings


def HelpSettings():
    settings = cpputils.HelpSettings()
    settings["scenarios file"] = "The path to the generated scenarios to include"
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
[[TestBody]]
}
"""[1:]

    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    decl = "  static void {0}({1})\n"
    altdecl = "  TEST(%s, {0})\n" % namespace
    cpp = cpputils.Cpp(settings, decl, altdecl, "  ")
    testBody = common.TestBody(scenarios, settings, cpp)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

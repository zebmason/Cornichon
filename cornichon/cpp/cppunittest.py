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
    buffer = """
// Other bespoke headers
#include "[[scenarios file]]"

// Third party headers
#include "CppUnitTest.h"

namespace [[fullnamespace]]
{
  TEST_CLASS([[className]])
  {
[[TestBody]]
  };
[[endnamespace]]
"""[1:]

    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])

    namespace = common.FeatureName(feature, settings["cases"]["namespace"])
    namespace = cpputils.NameSpace(settings, namespace)
    buffer = buffer.replace("[[fullnamespace]]", namespace.Begin())
    buffer = buffer.replace("[[endnamespace]]", namespace.End())

    # Print the class
    featureName = common.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[featureName]]", featureName)
    className = common.Tokenise("Feature", settings["cases"]["class"])
    buffer = buffer.replace("[[className]]", className)

    decl = "    static void {0}({1})\n"
    testdecl = "    TEST_METHOD({0})\n"
    cpp = cpputils.Cpp(settings, decl, testdecl, "    ")
    testBody = cpp.TestBody(scenarios, settings)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

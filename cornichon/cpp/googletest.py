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
    featureName = common.FeatureName(feature, settings["cases"]["namespace"])
    namespace = common.Tokenise(featureName, settings["cases"]["namespace"])

    buffer = """
// Other bespoke headers
#include "[[scenarios file]]"

// Third party headers
#include "gtest/gtest.h"

namespace [[fullnamespace]]
{
[[TestBody]]
[[endnamespace]]
"""[1:]

    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])

    ns = cpputils.NameSpace(settings, namespace)
    buffer = buffer.replace("[[fullnamespace]]", ns.Begin())
    buffer = buffer.replace("[[endnamespace]]", ns.End())

    decl = "  static void {0}({1})\n"
    testdecl = "  TEST(%s, {0})\n" % namespace
    cpp = cpputils.Cpp(settings, decl, testdecl, "  ")
    testBody = cpp.TestBody(scenarios, settings)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

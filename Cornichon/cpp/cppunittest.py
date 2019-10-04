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
    buffer = """
// Local headers
#include "stdafx.h"

// Other bespoke headers
#include "[[scenarios file]]"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace [[rootnamespace]][[namespace]]
{
  TEST_CLASS([[featureName]])
  {
[[Scenarios]]


    TEST_CLASS_INITIALIZE(ClassInitialize)
    {
      std::clog << "Entering [[stub]]" << std::endl;
    }

    TEST_CLASS_CLEANUP(ClassCleanup)
    {
      std::clog << "Exiting [[stub]]" << std::endl;
    }

  public:
[[ScenarioInsts]]
  };
}
"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])
    buffer = buffer.replace("[[scenarios file]]", settings["scenarios file"])

    namespace = settings["stub"]
    namespace = common.Tokenise(namespace, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    featureName = cpputils.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[Scenarios]]", cpputils.Scenarios(namespace, scenarios, settings, "    "))
    insts = cpputils.ScenarioInsts(scenarios, settings, "TEST_METHOD(", "    ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

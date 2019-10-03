import common
import cpputils


def TestMethods(scenarios, settings):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario = common.Tokenise(lines[0], settings["cases"]["scenario"])

        if s.examples.Exists():
            header = s.examples.Header()
            arguments = cpputils.Arguments(s.examples, header)
            concat2 = cpputils.Concat(s.examples, header)
            stringify = cpputils.Stringify(s.examples, header)
            buffer = """
#define [[scenario]]Inst([[arguments]]) \\
  TEST_METHOD([[scenario]] ## [[concat2]]) \\
  { \\
    [[scenario]]([[stringify]]); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[concat2]]", concat2)
            buffer = buffer.replace("[[stringify]]", stringify)
            concat += buffer
        else:
            buffer = """
#define [[scenario]]Inst() \\
  TEST_METHOD([[scenario]] ## Impl) \\
  { \\
    [[scenario]](); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()


def Settings():
    settings = cpputils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    settings["helpers"] = "../helpers/"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    buffer = """
// Local headers
#include "stdafx.h"

// Other bespoke headers
#include "[[helpers]][[stub]].h"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

[[TestMethods]]


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
    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[TestMethods]]", TestMethods(scenarios, settings))

    namespace = settings["stub"]
    namespace = common.Tokenise(namespace, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    featureName = cpputils.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[Scenarios]]", cpputils.Scenarios(namespace, scenarios, settings, "    "))
    buffer = buffer.replace("[[ScenarioInsts]]", cpputils.ScenarioInsts(scenarios, settings, "    "))

    return buffer

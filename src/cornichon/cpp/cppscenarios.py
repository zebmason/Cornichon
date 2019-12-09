import common
import cpputils
import gherkin


def Settings():
    settings = cpputils.Settings()
    return settings


def HelpSettings():
    settings = cpputils.HelpSettings()
    return settings


class PrintScenario(common.PrintScenario):
    def __init__(self):
        super().__init__()
        self.line = "\n      std::clog << %s << std::endl;"
        self.contractions = {' << ""': '', ' "" << ': ' '}
        self.sub = '" << %s << "'
        self.step = """
    /// Gherkin DSL step
    void [[stepName]]([[arguments]])
    {
[[description]]
    }

"""[1:]


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = common.FeatureName(feature, settings["cases"]["namespace"])

    printer = PrintScenario()
    featureDesc = printer.FeatureDesc(feature)

    concat = """
#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace [[fullnamespace]]
{
"""[1:]

    namespace = common.Tokenise(featureName, settings["cases"]["namespace"])
    namespace = cpputils.NameSpace(settings, namespace + "::Scenarios")
    concat = concat.replace("[[fullnamespace]]", namespace.Begin())

    for scenario in scenarios:
        buffer = """
  /// Test class scenario
  class [[featureName]]
  {
  public:
    /// Constructor
    [[featureName]]()
    {
[[documentation]]
    }

[[steps]]
  };

"""[1:]

        buffer = buffer.replace("[[featureName]]", common.Tokenise(scenario.lines, settings["cases"]["class"]))
        documentation = printer.Documentation(scenario, featureDesc, settings)
        buffer = buffer.replace("[[documentation]]", documentation)
        buffer = buffer.replace("[[steps]]", printer.Steps(scenario, settings))
        concat += buffer

    concat = concat[:-2] + """
[[endnamespace]]
""".replace("[[endnamespace]]", namespace.End())
    return concat

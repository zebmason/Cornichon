import common
import csutils
import gherkin


def Settings():
    settings = csutils.Settings()
    return settings


def HelpSettings():
    settings = csutils.HelpSettings()
    return settings


class PrintScenario(common.PrintScenario):
    def __init__(self):
        super().__init__()
        self.line = "\n      System.Console.WriteLine(%s);"
        self.step = """
    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void [[stepName]]([[arguments]])
    {
[[description]]
    }

"""[1:]


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = common.FeatureName(feature, settings["cases"]["class"])

    printer = PrintScenario()
    featureDesc = printer.FeatureDesc(feature)

    concat = """
namespace [[rootnamespace]][[namespace]].Scenarios
{
"""[1:]

    namespace = common.FeatureName(feature, settings["cases"]["namespace"])
    concat = concat.replace("[[rootnamespace]]", settings["rootnamespace"])
    concat = concat.replace("[[namespace]]", namespace)

    for scenario in scenarios:
        buffer = """
  /// <summary>
  /// Test class scenario
  /// </summary>
  public class [[featureName]]
  {
    /// <summary>
    /// Constructor
    /// </summary>
    public [[featureName]]()
    {
[[documentation]]
    }

[[steps]]
  }

"""[1:]

        buffer = buffer.replace("[[featureName]]", common.Tokenise(scenario.lines, settings["cases"]["class"]))
        documentation = printer.Documentation(scenario, featureDesc, settings)
        buffer = buffer.replace("[[documentation]]", documentation)
        buffer = buffer.replace("[[steps]]", printer.Steps(scenario, settings))
        concat += buffer

    concat = concat[:-2] + """
}
"""
    return concat

import common
import csutils


def Settings():
    settings = csutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    return settings


def HelpSettings():
    settings = csutils.HelpSettings()
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    buffer = """
namespace [[rootnamespace]][[namespace]]
{
  using NUnit.Framework;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestFixture]
  public class [[className]]
  {
[[Scenarios]]
[[ScenarioInsts]]
  }
}
"""[1:]

    namespace = csutils.FeatureName(feature, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    className = common.Tokenise("Feature", settings["cases"]["class"])
    buffer = buffer.replace("[[className]]", className)
    buffer = buffer.replace("[[Scenarios]]", csutils.Scenarios(namespace, scenarios, settings, "    "))
    insts = csutils.ScenarioInsts(scenarios, settings, "Test", "    ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

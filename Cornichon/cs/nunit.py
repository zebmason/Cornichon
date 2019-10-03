import common
import csutils


def Settings():
    settings = csutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    settings["helpers"] = "../helpers/"
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
  public class [[featureName]]
  {
[[Scenarios]]
[[ScenarioInsts]]
  }
}
"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])
    buffer = buffer.replace("[[helpers]]", settings["helpers"])

    namespace = settings["stub"]
    namespace = common.Tokenise(namespace, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    featureName = csutils.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[Scenarios]]", csutils.Scenarios(namespace, scenarios, settings, "    "))
    insts = csutils.ScenarioInsts(scenarios, settings, "Test", "    ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

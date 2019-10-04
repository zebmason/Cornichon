import common
import csutils


def Settings():
    settings = csutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    buffer = """
namespace [[rootnamespace]][[namespace]]
{
  using Microsoft.VisualStudio.TestTools.UnitTesting;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestClass]
  public class [[featureName]]
  {
[[Scenarios]]
[[ScenarioInsts]]
  }
}
"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])

    namespace = settings["stub"]
    namespace = common.Tokenise(namespace, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    featureName = csutils.FeatureName(feature, settings["cases"]["class"])
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[Scenarios]]", csutils.Scenarios(namespace, scenarios, settings, "    "))
    insts = csutils.ScenarioInsts(scenarios, settings, "TestMethod", "    ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

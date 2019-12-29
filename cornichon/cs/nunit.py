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
[[TestBody]]
  }
}
"""[1:]

    namespace = common.FeatureName(feature, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    className = common.Tokenise("Feature", settings["cases"]["class"])
    buffer = buffer.replace("[[className]]", className)

    cs = csutils.CSharp(settings, "Test")
    testBody = cs.TestBody(scenarios, settings)
    buffer = buffer.replace("[[TestBody]]", testBody)

    return buffer

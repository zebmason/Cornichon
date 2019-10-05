import common
import vbutils


def Settings():
    settings = vbutils.Settings()
    settings["cases"]["scenario"] = "Camel"
    settings["cases"]["test"] = "Camel"
    return settings


def HelpSettings():
    settings = vbutils.HelpSettings()
    return settings


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    buffer = """
Imports NUnit.Framework

Namespace [[rootnamespace]][[namespace]]

  ' <summary>
  ' Gherkin DSL feature
  ' </summary>
  <TestFixture>
  Public Class [[className]]
[[Scenarios]]
[[ScenarioInsts]]
  End Class
End Namespace
"""[1:]

    namespace = vbutils.FeatureName(feature, settings["cases"]["namespace"])
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    className = common.Tokenise("Feature", settings["cases"]["class"])
    buffer = buffer.replace("[[className]]", className)
    buffer = buffer.replace("[[Scenarios]]", vbutils.Scenarios(namespace, scenarios, settings, "    "))
    insts = vbutils.ScenarioInsts(scenarios, settings, "Test", "    ")
    buffer = buffer.replace("[[ScenarioInsts]]", insts)

    return buffer

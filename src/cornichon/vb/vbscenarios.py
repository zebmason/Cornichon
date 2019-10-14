import common
import vbutils
import gherkin


def Settings():
    settings = vbutils.Settings()
    return settings


def HelpSettings():
    settings = vbutils.HelpSettings()
    return settings


class PrintScenario(common.PrintScenario):
    def __init__(self):
        super().__init__()
        self.line = "\n      System.Console.WriteLine(%s)"
        self.sub = '" + %s.ToString() + "'
        self.step = """
    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub [[stepName]]([[arguments]])
[[description]]
    End Sub

"""[1:]


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    featureName = common.FeatureName(feature, settings["cases"]["class"])

    printer = PrintScenario()
    featureDesc = printer.FeatureDesc(feature)

    concat = """
Namespace [[rootnamespace]][[namespace]].Scenarios
"""[1:]

    namespace = common.FeatureName(feature, settings["cases"]["namespace"])
    concat = concat.replace("[[rootnamespace]]", settings["rootnamespace"])
    concat = concat.replace("[[namespace]]", namespace)

    for scenario in scenarios:
        buffer = """
  ' <summary>
  ' Test class scenario
  ' </summary>
  Public Class [[featureName]]
    ' <summary>
    ' Constructor
    ' </summary>
    Public Sub New()
[[documentation]]
    End Sub

[[steps]]
  End Class

"""[1:]

        buffer = buffer.replace("[[featureName]]", common.Tokenise(scenario.lines, settings["cases"]["class"]))
        documentation = printer.Documentation(scenario, featureDesc, settings)
        buffer = buffer.replace("[[documentation]]", documentation)
        buffer = buffer.replace("[[steps]]", printer.Steps(scenario, settings))
        concat += buffer

    concat = concat[:-2] + """
End Namespace
"""
    return concat

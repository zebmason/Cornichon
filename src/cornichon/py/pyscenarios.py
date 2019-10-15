import common
import pyutils
import gherkin


def Settings():
    settings = pyutils.Settings()
    return settings


def HelpSettings():
    settings = pyutils.HelpSettings()
    return settings


class PrintScenario(common.PrintScenario):
    def __init__(self):
        super().__init__()
        self.line = "\n            print(%s)"
        self.sub = '" + str(%s) + "'
        self.step = """
        def [[stepName]](self, [[arguments]]):
            %s
[[description]]

"""[1:] % ('"""Gherkin DSL step"""')


def Generate(parsed, settings):
    scenarios = parsed[0]
    feature = parsed[1]
    lines = "%s%s %s" % ('  ', 'Feature:', feature)

    printer = PrintScenario()
    featureDesc = printer.Description(lines)
    concat = """
class Scenarios:
"""[1:]

    for scenario in scenarios:
        buffer = """
    class [[Scenario]]:
        [[comment1]]
        def __init__(self):
            [[comment2]]
[[documentation]]

[[steps]]
"""

        buffer = buffer.replace("[[comment1]]", '"""Test class scenario"""')
        buffer = buffer.replace("[[comment2]]", '"""Initialiser"""')
        buffer = buffer.replace("[[steps]]", printer.Steps(scenario, settings))
        scenarioName = common.Tokenise(scenario.lines, settings["cases"]["class"])
        buffer = buffer.replace("[[Scenario]]", scenarioName)
        lines = "%s%s %s" % ('    ', 'Scenario:', scenario.lines)
        desc = printer.Description(lines)
        documentation = featureDesc + "\n" + desc
        buffer = buffer.replace("[[documentation]]", documentation)
        concat += buffer

    return concat.replace("(self, )", "(self)")

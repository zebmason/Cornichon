import gherkin


def ExtractParams(line, delim1, delim2):
    params = []
    while True:
        i = line.find(delim1)
        if -1 == i:
            break
        j = line.find(delim2, i + 1)
        if -1 == j:
            break
        params.append(line[i:j + 1])
        line = line[:i] + line[j + 1:]
    return line, params


def Argument(arg, type, templates):
    return templates[type].format(arg)


def Tokenise(line, case=""):
    line = ''.join([i for i in line if (i.isalnum() or i in [" ", "_"])])
    while line.find("  ") != -1:
        line = line.replace("  ", " ")

    if case == "Camel":
        return ''.join([Upper(i) for i in line.split()])
    elif case == "camel":
        return Lower(''.join([Upper(i) for i in line.split()]))
    elif case == "snake":
        return '_'.join([Lower(i) for i in line.split()])
    elif case == "Snake":
        return Upper('_'.join([Lower(i) for i in line.split()]))

    return line.replace(" ", "")


def FeatureName(feature, case):
    lines = feature.split('\n')
    return Tokenise(lines[0], case)


def Upper(word):
    return word[0].upper() + word[1:]


def Lower(word):
    return word[0].lower() + word[1:]


def Settings():
    settings = {}
    settings["cases"] = {}
    settings["types"] = {}
    settings["values"] = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings["types"][type] = "{}"
        settings["values"][type] = "{}"

    settings["values"]["string"] = "\"{}\""
    return settings


def HelpSettings():
    settings = {}
    settings["cases"] = {}
    settings["types"] = {}
    settings["values"] = {}
    for type in ["bool", "int", "uint", "float", "string"]:
        settings["types"][type] = "The template used to specify the type of a parameter"
        settings["values"][type] = "The template used to wrap the value of a parameter"
    for case in ["class", "param", "step", "scenario", "test"]:
        settings["cases"][case] = "When tokenising some text use one of camel, Camel, snake or Snake case"
    return settings


def UnmodifiedArg(val, type):
    return val


def ArgumentList(args, types, formats, argModifier, sep=", "):
    if len(args) == 0:
        return ""

    line = ""
    for i in range(len(args)):
        type = types[i]
        bit = formats[type].format(argModifier(args[i], type))
        if len(bit.strip()) == 0:
            continue
        line = "{}{}{}".format(line, sep, bit)

    return line[len(sep):]


def TestBody(scenarios, settings, framework):
    concat = ""
    # Create the scenarios
    for scenario in scenarios:
        lines = scenario.lines.split('\n')
        if scenario.examples.Exists():
            fullArgs = scenario.examples.ArgumentsList(settings["types"])
            concat += framework.ScenarioDecl(lines[0], fullArgs)
        else:
            scenarioName = Tokenise(lines[0], settings["cases"]["test"])
            concat += framework.TestDecl(lines[0])
        steps = ""
        template = framework.StepTemplate()
        for step in scenario.Steps():
            lines = step[1].split('\n')
            st = gherkin.Step(step[0], step[1])
            method = st.Tokenise(settings["cases"]["step"])
            arguments = st.ParameterList(scenario.examples.types)
            buffer = template
            buffer = buffer.replace("[[method]]", method)
            buffer = buffer.replace("[[arguments]]", arguments)
            steps += buffer
        concat += framework.Body(scenario, steps)
    concat = concat.rstrip() + "\n"
    # Create any examples
    for scenario in scenarios:
        lines = scenario.lines.split('\n')
        sc = lines[0]
        if scenario.examples.Exists():
            lines = scenario.examples.lines.split('\n')
            for line in lines[2:]:
                if len(line.strip()) == 0:
                    continue
                arguments = scenario.examples.ArgumentsInstance(settings["values"], line, framework.argModifier)
                if "" == arguments:
                    continue
                concat += framework.Example(sc, arguments)
    return concat.rstrip()


class PrintScenario:
    def __init__(self):
        self.stringify = '"%s"'
        self.contractions = {' + ""': '', ' "" + ': ' '}
        self.line = "\n      %s;"
        self.sub = '" + %s + "'
        self.step = ""

    def Description(self, lines):
        des = ''
        for line in lines.split('\n'):
            if line.strip() == '':
                continue
            line = self.stringify % line
            for contraction in self.contractions:
                line = line.replace(contraction, self.contractions[contraction])
            des += self.line % line
        return des[1:]

    def FeatureDesc(self, feature):
        lines = feature.split('\n')
        lines = "%s%s %s" % ('  ', 'Feature:', feature)
        return self.Description(lines)

    def Documentation(self, scenario, feature, settings):
        lines = scenario.lines.split('\n')
        lines = "%s%s %s" % ('    ', 'Scenario:', scenario.lines)
        description = self.Description(lines)
        return feature + "\n" + description

    def Steps(self, scenario, settings):
        concat = ""
        steps = []
        # parse the sections
        for s in scenario.Steps():
            lines = s[1].split('\n')
            step = gherkin.Step(s[0], s[1])
            stepName = step.Tokenise(settings["cases"]["step"])
            if 0 != steps.count(stepName):
                continue
            steps.append(stepName)
            arguments = step.ArgumentList(scenario.examples.types, settings["types"])
            buffer = self.step
            buffer = buffer.replace("[[stepName]]", stepName)
            buffer = buffer.replace("[[arguments]]", arguments)
            lines = "      %s %s" % (s[0], s[1])
            description = self.Description(step.Sub(lines, self.sub))
            buffer = buffer.replace("[[description]]", description)
            concat += buffer
        return concat.rstrip()

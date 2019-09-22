from common import *

def PrintScenario(scenario, arguments, feature, steps, documentation, settings):
    buffer = """
    static void [[scenario]]([[arguments]])
    {
[[documentation]]
      [[rootnamespace]]Helpers::[[feature]] instance;
[[steps]]
    }
"""[1:]
    buffer = buffer.replace("[[scenario]]", scenario)
    buffer = buffer.replace("[[arguments]]", arguments)
    buffer = buffer.replace("[[documentation]]", documentation)
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[feature]]", feature)
    
    concat = ""
    for step in steps:
        concat += step + "\n"
    buffer = buffer.replace("[[steps]]", concat.rstrip())
    return buffer

def Description(section, lines, params, indent):
    des = ''
    first = True
    for line in lines:
        if line.strip() == '':
            continue
        if first:
            first = False
            line = "%s%s %s" % (indent, section, line)
        line = '"%s"' % line
        for i in range(len(params)):
            if params[i][0] == '<':
                line = line.replace(params[i], '" << %s << "' % params[i][1:-1])
                continue
            line = line.replace(params[i], '" << arg%d << "' % (i+1))
        line = line.replace(' << ""', '')
        line = line.replace(' "" << ', ' ')
        des += """
      std::clog << %s << std::endl;""" % line
    return des[1:]

def Feature(feature):
    lines = feature.split('\n')
    camelCase, args, params = CamelCase('Feature:', lines[0])
    return camelCase, Description('Feature:', lines, [], '  ')

def Scenarios(scenarios, featureName, feature, settings):
    concat = ""
    # parse the scenarios
    for s in scenarios:
        fullArgs = ''
        if s.examples != '':
            args = ''
            lines = s.examples.split('\n')
            for line in lines[1:]:
                args = line.strip()[1:-2].replace('|', ' ')
                break
            fullArgs = Arguments(args.split(), 'std::string ')
        steps = []
        for step in s.Steps():
            lines = step[1].split('\n')
            camelCase, args, params = CamelCase(step[0], lines[0])
            for i in range(len(params)):
                args[i] = params[i]
            arguments = Arguments(args, '').replace('<', '').replace('>', '')
            steps.append('      instance.%s(%s);' % (camelCase, arguments))
            continue
        lines = s.lines.split('\n')
        scenarioName, args, params = CamelCase('Scenario:', lines[0])
        scenario = feature + "\n" + Description('Scenario:', lines, [], '    ')
        concat += PrintScenario(scenarioName, fullArgs, featureName, steps, scenario, settings)
        concat += "\n"
    return concat

def ScenarioInsts(scenarios):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = CamelCase('Scenario:', lines[0])
        if s.examples != '':
            lines = s.examples.split('\n')
            for line in lines[2:]:
                args = line.strip()[1:-2].replace('|', ' ')
                if '' == args:
                    continue
                arguments = Arguments(args.split(), '')
                buffer = """
    [[scenario]]Inst([[arguments]]);
"""
                buffer = buffer.replace("[[scenario]]", scenario)
                buffer = buffer.replace("[[arguments]]", arguments)
                concat += buffer
        else:
            buffer = """
    [[scenario]]Inst();
"""
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()

def TestMethods(scenarios):
    concat = ""
    # parse the sections
    for s in scenarios:
        lines = s.lines.split('\n')
        scenario, args, params = CamelCase('Scenario', lines[0])

        if s.examples != '':
            args = ''
            lines = s.examples.split('\n')
            for line in lines[1:]:
                args = line.strip()[1:-2].replace('|', ' ').upper()
                break
            arguments = Arguments(args.split(), '_')
            concat2 = arguments.replace(', _', ' ## _')
            stringify = arguments.replace('_', '#_')
            buffer = """
#define [[scenario]]Inst([[arguments]]) \\
  TEST_METHOD([[scenario]] ## [[concat2]]) \\
  { \\
    [[scenario]]([[stringify]]); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            buffer = buffer.replace("[[arguments]]", arguments)
            buffer = buffer.replace("[[concat2]]", concat2)
            buffer = buffer.replace("[[stringify]]", stringify)
            concat += buffer
        else:
            buffer = """
#define [[scenario]]Inst() \\
  TEST_METHOD([[scenario]] ## Impl) \\
  { \\
    [[scenario]](); \\
  }

"""[1:]
            buffer = buffer.replace("[[scenario]]", scenario)
            concat += buffer
    return concat.rstrip()

def Generate(scenarios, feature, settings):
    buffer = """
#include "stdafx.h"

// Other bespoke headers
#include "[[helpers]][[stub]].h"
#include "[[helpers]]LogStream.h"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

[[TestMethods]]


namespace [[rootnamespace]][[namespace]]
{
  TEST_CLASS([[featureName]])
  {
    static std::streambuf* oldBuffer;
    static std::shared_ptr<std::streambuf> newBuffer;

[[Scenarios]]
    TEST_CLASS_INITIALIZE(ClassInitialize)
    {
      newBuffer = std::make_shared<TestUtils::LogStream>();
      oldBuffer = std::clog.rdbuf(newBuffer.get());
      std::clog << "Entering [[stub]]" << std::endl;
    }

    TEST_CLASS_CLEANUP(ClassCleanup)
    {
      std::clog << "Exiting [[stub]]" << std::endl;
      std::clog.rdbuf(oldBuffer);
      newBuffer = nullptr;
    }

  public:
[[ScenarioInsts]]
  };

  std::streambuf* [[featureName]]::oldBuffer = nullptr;
  std::shared_ptr<std::streambuf> [[featureName]]::newBuffer = nullptr;
}

"""[1:]

    buffer = buffer.replace("[[stub]]", settings["stub"])
    buffer = buffer.replace("[[helpers]]", settings["helpers"])
    buffer = buffer.replace("[[TestMethods]]", TestMethods(scenarios))
    
    namespace = settings["stub"]
    namespace, args, params = CamelCase('', namespace)
    buffer = buffer.replace("[[rootnamespace]]", settings["rootnamespace"])
    buffer = buffer.replace("[[namespace]]", namespace)

    # Print the class
    featureName, featureDesc = Feature(feature)
    buffer = buffer.replace("[[featureName]]", featureName)
    buffer = buffer.replace("[[Scenarios]]", Scenarios(scenarios, featureName, featureDesc, settings))
    buffer = buffer.replace("[[ScenarioInsts]]", ScenarioInsts(scenarios))

    return buffer

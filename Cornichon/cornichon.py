import importlib
import os
import os.path
import sys
import gherkin


def Import(output):
    bits = output.split("/")
    subdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), bits[0])
    if subdir not in sys.path:
        sys.path.insert(0, subdir)
    return importlib.import_module(bits[1])


def Settings(output):
    mod = Import(output)
    return mod.Settings()


def Generate(settings, output):
    parsed = gherkin.Parse(settings)
    mod = Import(output)
    return mod.Generate(parsed, settings)

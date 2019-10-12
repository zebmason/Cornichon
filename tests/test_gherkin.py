import unittest
from scenarios_gherkin import *


class Gherkin(unittest.TestCase):
    """Gherkin DSL feature"""

    def Types(self, type, value):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Types()
        scenario.GivenAnInput(value)
        scenario.ThenItHasCorresponding(type)

    def Worst(self, type, first, second):
        """Gherkin DSL scenario"""
        scenario = Scenarios.Worst()
        scenario.GivenAFirstType(first)
        scenario.GivenASecondType(second)
        scenario.ThenItHasCorresponding(type)

    def test_types_uint_78(self):
        """Gherkin DSL test"""
        self.Types("uint", "78")

    def test_types_bool_true(self):
        """Gherkin DSL test"""
        self.Types("bool", "true")

    def test_types_int_90(self):
        """Gherkin DSL test"""
        self.Types("int", "-90")

    def test_types_float_145(self):
        """Gherkin DSL test"""
        self.Types("float", "1.45")

    def test_types_string_is_so(self):
        """Gherkin DSL test"""
        self.Types("string", "is so")

    def test_worst_int_int_uint(self):
        """Gherkin DSL test"""
        self.Worst("int", "int", "uint")

    def test_worst_float_float_uint(self):
        """Gherkin DSL test"""
        self.Worst("float", "float", "uint")

    def test_worst_float_float_int(self):
        """Gherkin DSL test"""
        self.Worst("float", "float", "int")

    def test_worst_string_string_uint(self):
        """Gherkin DSL test"""
        self.Worst("string", "string", "uint")

    def test_worst_string_string_int(self):
        """Gherkin DSL test"""
        self.Worst("string", "string", "int")

    def test_worst_string_string_float(self):
        """Gherkin DSL test"""
        self.Worst("string", "string", "float")


if __name__ == '__main__':
    unittest.main()

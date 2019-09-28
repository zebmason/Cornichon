import unittest
from helpers_units import *

class Cornichon(unittest.TestCase):

    def Types(self, type,  value):
        helpers = TypesHelper()
        helpers.GivenAnInput(value);
        helpers.ThenItHasCorresponding(type);

    def Worst(self, type,  first,  second):
        helpers = WorstHelper()
        helpers.GivenAFirstType(first);
        helpers.GivenASecondType(second);
        helpers.ThenItHasCorresponding(type);

    def Templated(self, arg,  type,  template,  output):
        helpers = TemplatedHelper()
        helpers.GivenAnArgument(arg);
        helpers.GivenAType(type);
        helpers.GivenATemplate(template);
        helpers.ThenItHasCorresponding(output);

    def test_types_symbol_sym(self):
        self.Types("symbol", "sym")

    def test_types_uint_78(self):
        self.Types("uint", "78")

    def test_types_bool_true(self):
        self.Types("bool", "true")

    def test_types_int_90(self):
        self.Types("int", "-90")

    def test_types_float_145(self):
        self.Types("float", "1.45")

    def test_types_string_is_so(self):
        self.Types("string", "is so")

    def test_worst_symbol_symbol_symbol(self):
        self.Worst("symbol", "symbol", "symbol")

    def test_worst_symbol_uint_symbol(self):
        self.Worst("symbol", "uint", "symbol")

    def test_worst_symbol_symbol_uint(self):
        self.Worst("symbol", "symbol", "uint")

    def test_worst_int_int_uint(self):
        self.Worst("int", "int", "uint")

    def test_worst_float_float_uint(self):
        self.Worst("float", "float", "uint")

    def test_worst_float_float_int(self):
        self.Worst("float", "float", "int")

    def test_worst_string_symbol_int(self):
        self.Worst("string", "symbol", "int")

    def test_worst_string_string_symbol(self):
        self.Worst("string", "string", "symbol")

    def test_worst_string_string_uint(self):
        self.Worst("string", "string", "uint")

    def test_worst_string_string_int(self):
        self.Worst("string", "string", "int")

    def test_worst_string_string_float(self):
        self.Worst("string", "string", "float")

    def test_worst_string_string_symbol(self):
        self.Worst("string", "string", "symbol")

    def test_worst_string_string_symbol(self):
        self.Worst("string", "string", "symbol")

    def test_worst_symbol_symbol_none(self):
        self.Worst("symbol", "symbol", "none")

    def test_worst_symbol_none_symbol(self):
        self.Worst("symbol", "none", "symbol")

    def test_templated_one_int_int_int_one(self):
        self.Templated("one", "int", "int {}", "int one")

    def test_templated_two_string_two(self):
        self.Templated("two", "string", "\"{}\"", "\"two\"")

if __name__ == '__main__':
    unittest.main()

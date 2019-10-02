import unittest
from helpers_units import *


class Units(unittest.TestCase):
    """Gherkin DSL feature"""

    def Templated(self, arg, type, template, output):
        """Gherkin DSL scenario"""
        helpers = TemplatedHelper()
        helpers.GivenAnArgument(arg)
        helpers.GivenAType(type)
        helpers.GivenATemplate(template)
        helpers.ThenItHasCorresponding(output)

    def Tokenized(self, arg, output):
        """Gherkin DSL scenario"""
        helpers = TokenizedHelper()
        helpers.GivenAnArgument(arg)
        helpers.ThenItHasCorresponding(output)

    def Snaked(self, arg, output):
        """Gherkin DSL scenario"""
        helpers = SnakedHelper()
        helpers.GivenAnArgument(arg)
        helpers.ThenItHasCorresponding(output)

    def Argumental(self, args, types, language, declaration, output):
        """Gherkin DSL scenario"""
        helpers = ArgumentalHelper()
        helpers.GivenArguments(args)
        helpers.GivenTypes(types)
        helpers.GivenALanguage(language)
        helpers.GivenItIsADeclaration(declaration)
        helpers.ThenItHasCorresponding(output)

    def test_templated_one_int_int_int_one(self):
        """Gherkin DSL test"""
        self.Templated("one", "int", "int {}", "int one")

    def test_templated_two_string_two(self):
        """Gherkin DSL test"""
        self.Templated("two", "string", "\"{}\"", "\"two\"")

    def test_tokenized_int_int(self):
        """Gherkin DSL test"""
        self.Tokenized("int {}", "int")

    def test_tokenized_19_19(self):
        """Gherkin DSL test"""
        self.Tokenized("1.9", "19")

    def test_snaked_int_int(self):
        """Gherkin DSL test"""
        self.Snaked("int {}", "int")

    def test_snaked_19_19(self):
        """Gherkin DSL test"""
        self.Snaked("1.9", "19")

    def test_snaked_1_9_1_9(self):
        """Gherkin DSL test"""
        self.Snaked("1 9", "1_9")

    def test_argumental_abcdef_intsymbolstringuintfloatbool_cpp_True_int_a_const_stdstring_b_const_stdstring_c_unsigned_int_d_double_e_bool_f(self):
        """Gherkin DSL test"""
        self.Argumental("a,b,c,d,e,f", "int,symbol,string,uint,float,bool", "cpp", True, "int a, const std::string& b, const std::string& c, unsigned int d, double e, bool f")

    def test_argumental_9symbolas_is10175False_intsymbolstringuintfloatbool_cpp_False_9_symbol_as_is_10_175_false(self):
        """Gherkin DSL test"""
        self.Argumental("-9,symbol,as is,10,1.75,False", "int,symbol,string,uint,float,bool", "cpp", False, "-9, \"symbol\", \"as is\", 10, 1.75, false")

    def test_argumental_trueTruefalseFalse_boolboolboolbool_cpp_False_true_true_false_false(self):
        """Gherkin DSL test"""
        self.Argumental("true,True,false,False", "bool,bool,bool,bool", "cpp", False, "true, true, false, false")

    def test_argumental_falseFalsetrueTrue_boolboolboolbool_python_False_False_False_True_True(self):
        """Gherkin DSL test"""
        self.Argumental("false,False,true,True", "bool,bool,bool,bool", "python", False, "False, False, True, True")


if __name__ == '__main__':
    unittest.main()

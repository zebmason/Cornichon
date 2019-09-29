Feature: Units

Scenario Outline: types
  Given an input <value>
  Then it has corresponding <type>
  Examples:
    | type   | value |
    | symbol | sym   |
    | uint   | 78    |
    | bool   | true  |
    | int    | -90   |
    | float  | 1.45  |
    | string | is so |

Scenario Outline: worst
  Given a first type <first>
  Given a second type <second>
  Then it has corresponding <type>
  Examples:
    | type   | first  | second |
    | symbol | symbol | symbol |
    | symbol | uint   | symbol |
    | symbol | symbol | uint   |
    | int    | int    | uint   |
    | float  | float  | uint   |
    | float  | float  | int    |
    | string | symbol | int    |
    | string | string | symbol |
    | string | string | uint   |
    | string | string | int    |
    | string | string | float  |
    | string | string | symbol |
    | string | string | symbol |
    | symbol | symbol | none   |
    | symbol | none   | symbol |

Scenario Outline: templated
  Given an argument <arg>
  Given a type <type>
  Given a template <template>
  Then it has corresponding <output>
  Examples:
    | arg | type   | template | output  |
    | one | int    | int {}   | int one |
    | two | string | "{}"     | "two"   |

Scenario Outline: tokenized
  Given an argument <arg>
  Then it has corresponding <output>
  Examples:
    | arg    | output |
    | int {} | int    |
    | 1.9    | 19     |

Scenario Outline: snaked
  Given an argument <arg>
  Then it has corresponding <output>
  Examples:
    | arg    | output |
    | int {} | int    |
    | 1.9    | 19     |
    | 1 9    | 1_9    |

Scenario Outline: argumental
  Given arguments <args>
  And types <types>
  And a language <language>
  And it is a declaration <declaration>
  Then it has corresponding <output>
  Examples:
    | args | types | language | declaration | output |
    | a,b,c,d,e,f | int,symbol,string,uint,float,bool | cpp | True | int a, const std::string& b, const std::string& c, unsigned int d, double e, bool f |
    | -9,symbol,as is,10,1.75,False | int,symbol,string,uint,float,bool | cpp | False | -9, "symbol", "as is", 10, 1.75, false |
    | true,True,false,False | bool,bool,bool,bool | cpp | False | true, true, false, false |
    | false,False,true,True | bool,bool,bool,bool | python | False | False, False, True, True |

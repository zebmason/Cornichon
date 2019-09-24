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

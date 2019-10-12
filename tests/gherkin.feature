Feature: Gherkin

Scenario Outline: types
  Given an input <value>
  Then it has corresponding <type>
  Examples:
    | type   | value |
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
    | int    | int    | uint   |
    | float  | float  | uint   |
    | float  | float  | int    |
    | string | string | uint   |
    | string | string | int    |
    | string | string | float  |

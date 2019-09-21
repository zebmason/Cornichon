Feature: Accumulator

Background:
  Given an initial <value>

Scenario Outline: Add one other
  When you add a <second>
  Then the result is <sum>
  Examples:
    | value | second | sum |
    | 1     | 2      | 3   |
    | 2     | 2      | 4   |

Scenario Outline: Add two others
  When you add a <second>
  And you add a <third>
  Then the result is <sum>
  Examples:
    | value | second | third  | sum |
    | 1     | 2      | 3      | 6   |
    | 2     | 3      | 4      | 9   |

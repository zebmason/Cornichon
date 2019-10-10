Feature: Accumulator2

Background:
  Given an initial 6

Scenario Outline: Add one other
  When you add a 5
  Then the result is 11

Scenario Outline: Add two others
  When you add a 8
  And you add a 4
  Then the result is 18

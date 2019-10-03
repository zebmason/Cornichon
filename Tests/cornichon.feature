Feature: Cornichon

Background:
  Given a feature file called <name>

Scenario Outline: cppunittest
  When the generator is cppunittest
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: cpphelpers
  When the generator is cpphelpers
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: googletest
  When the generator is googletest
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: pyunit_tests
  When the generator is pyunit_tests
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: pyhelpers
  When the generator is pyhelpers
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: unittesting
  When the generator is unittesting
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: nunit
  When the generator is nunit
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: cshelpers
  When the generator is cshelpers
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

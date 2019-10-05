Feature: Cornichon

Background:
  Given a feature file called <name>

Scenario Outline: cppunittest
  When the generator is cppunittest
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: cppscenarios
  When the generator is cppscenarios
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

Scenario Outline: pyscenarios
  When the generator is pyscenarios
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

Scenario Outline: csscenarios
  When the generator is csscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: vbunittesting
  When the generator is unittesting
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: vbnunit
  When the generator is nunit
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

Scenario Outline: vbscenarios
  When the generator is vbscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |

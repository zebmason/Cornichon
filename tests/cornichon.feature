Feature: Cornichon

Background:
  Given a feature file called <name>

Scenario Outline: cppunittest
  When the generator is cppunittest
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: cppscenarios
  When the generator is cppscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: unnested
  When the generator is cppscenarios
  Then the generated test is the same as <namespace>
  Examples:
    | name | namespace |
    | example2 | namespace2 |

Scenario Outline: googletest
  When the generator is googletest
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: pyunit_tests
  When the generator is pyunit_tests
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: pyscenarios
  When the generator is pyscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: pytests
  When the generator is pytests
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: pytestscenarios
  When the generator is pyscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: unittesting
  When the generator is unittesting
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: nunit
  When the generator is nunit
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: csscenarios
  When the generator is csscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: vbunittesting
  When the generator is unittesting
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: vbnunit
  When the generator is nunit
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

Scenario Outline: vbscenarios
  When the generator is vbscenarios
  Then the generated test is the same as the saved
  Examples:
    | name |
    | example |
    | example2 |

class Scenarios:

    class AddOneOther:
        """Test class scenario"""
        def __init__(self):
            """Initialiser"""
            print("  Feature: Accumulator2")
            print("    Scenario: Add one other")

        def GivenAnInitial6(self):
            """Gherkin DSL step"""
            print("      Given an initial 6")

        def WhenYouAddA5(self):
            """Gherkin DSL step"""
            print("      When you add a 5")

        def ThenTheResultIs11(self):
            """Gherkin DSL step"""
            print("      Then the result is 11")

    class AddTwoOthers:
        """Test class scenario"""
        def __init__(self):
            """Initialiser"""
            print("  Feature: Accumulator2")
            print("    Scenario: Add two others")

        def GivenAnInitial6(self):
            """Gherkin DSL step"""
            print("      Given an initial 6")

        def WhenYouAddA8(self):
            """Gherkin DSL step"""
            print("      When you add a 8")

        def WhenYouAddA4(self):
            """Gherkin DSL step"""
            print("      When you add a 4")

        def ThenTheResultIs18(self):
            """Gherkin DSL step"""
            print("      Then the result is 18")

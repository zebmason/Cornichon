Namespace Cornichon.Accumulator2.Scenarios
  ' <summary>
  ' Test class scenario
  ' </summary>
  Public Class AddOneOther
    ' <summary>
    ' Constructor
    ' </summary>
    Public Sub New()
      System.Console.WriteLine("  Feature: Accumulator2")
      System.Console.WriteLine("    Scenario: Add one other")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub GivenAnInitial6()
      System.Console.WriteLine("      Given an initial 6")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub WhenYouAddA5()
      System.Console.WriteLine("      When you add a 5")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub ThenTheResultIs11()
      System.Console.WriteLine("      Then the result is 11")
    End Sub
  End Class

  ' <summary>
  ' Test class scenario
  ' </summary>
  Public Class AddTwoOthers
    ' <summary>
    ' Constructor
    ' </summary>
    Public Sub New()
      System.Console.WriteLine("  Feature: Accumulator2")
      System.Console.WriteLine("    Scenario: Add two others")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub GivenAnInitial6()
      System.Console.WriteLine("      Given an initial 6")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub WhenYouAddA8()
      System.Console.WriteLine("      When you add a 8")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub WhenYouAddA4()
      System.Console.WriteLine("      When you add a 4")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub ThenTheResultIs18()
      System.Console.WriteLine("      Then the result is 18")
    End Sub
  End Class
End Namespace

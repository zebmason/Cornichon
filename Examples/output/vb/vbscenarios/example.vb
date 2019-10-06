Namespace Cornichon.Accumulator.Scenarios
  ' <summary>
  ' Test class scenario
  ' </summary>
  Public Class AddOneOther
    ' <summary>
    ' Constructor
    ' </summary>
    Public Sub New()
      System.Console.WriteLine("  Feature: Accumulator")
      System.Console.WriteLine("    Scenario: Add one other")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub GivenAnInitial(value As UInteger)
      System.Console.WriteLine("      Given an initial " + value.ToString())
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub WhenYouAddA(second As UInteger)
      System.Console.WriteLine("      When you add a " + second.ToString())
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub ThenTheResultIs(sum As UInteger)
      System.Console.WriteLine("      Then the result is " + sum.ToString())
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
      System.Console.WriteLine("  Feature: Accumulator")
      System.Console.WriteLine("    Scenario: Add two others")
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub GivenAnInitial(value As UInteger)
      System.Console.WriteLine("      Given an initial " + value.ToString())
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub WhenYouAddA(second As UInteger)
      System.Console.WriteLine("      When you add a " + second.ToString())
    End Sub

    ' <summary>
    ' Gherkin DSL step
    ' </summary>
    Public Sub ThenTheResultIs(sum As UInteger)
      System.Console.WriteLine("      Then the result is " + sum.ToString())
    End Sub
  End Class
End Namespace

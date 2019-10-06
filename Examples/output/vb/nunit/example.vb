Imports NUnit.Framework

Namespace Cornichon.Accumulator

  ' <summary>
  ' Gherkin DSL feature
  ' </summary>
  <TestFixture>
  Public Class Feature
    ' <summary>
    ' Gherkin DSL scenario
    ' </summary>
    Private Shared Sub AddOneOther(value As UInteger, second As UInteger, sum As UInteger)
      Dim scenario As Scenarios.AddOneOther = New Scenarios.AddOneOther()
      scenario.GivenAnInitial(value)
      scenario.WhenYouAddA(second)
      scenario.ThenTheResultIs(sum)
    End Sub

    ' <summary>
    ' Gherkin DSL scenario
    ' </summary>
    Private Shared Sub AddTwoOthers(value As UInteger, second As UInteger, third As UInteger, sum As UInteger)
      Dim scenario As Scenarios.AddTwoOthers = New Scenarios.AddTwoOthers()
      scenario.GivenAnInitial(value)
      scenario.WhenYouAddA(second)
      scenario.WhenYouAddA(third)
      scenario.ThenTheResultIs(sum)
    End Sub

    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <Test>
    Public Sub AddOneOther123()
      AddOneOther(1, 2, 3)
    End Sub

    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <Test>
    Public Sub AddOneOther224()
      AddOneOther(2, 2, 4)
    End Sub

    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <Test>
    Public Sub AddTwoOthers1236()
      AddTwoOthers(1, 2, 3, 6)
    End Sub

    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <Test>
    Public Sub AddTwoOthers2349()
      AddTwoOthers(2, 3, 4, 9)
    End Sub
  End Class
End Namespace

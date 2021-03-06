Imports Microsoft.VisualStudio.TestTools.UnitTesting

Namespace Cornichon.Accumulator2

  ' <summary>
  ' Gherkin DSL feature
  ' </summary>
  <TestClass>
  Public Class Feature
    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <TestMethod>
    Public Sub AddOneOther()
      Dim scenario As Scenarios.AddOneOther = New Scenarios.AddOneOther()
      scenario.GivenAnInitial6()
      scenario.WhenYouAddA5()
      scenario.ThenTheResultIs11()
    End Sub

    ' <summary>
    ' Gherkin DSL test
    ' </summary>
    <TestMethod>
    Public Sub AddTwoOthers()
      Dim scenario As Scenarios.AddTwoOthers = New Scenarios.AddTwoOthers()
      scenario.GivenAnInitial6()
      scenario.WhenYouAddA8()
      scenario.WhenYouAddA4()
      scenario.ThenTheResultIs18()
    End Sub
  End Class
End Namespace

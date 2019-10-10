namespace Cornichon.Accumulator2
{
  using Microsoft.VisualStudio.TestTools.UnitTesting;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestClass]
  public class Feature
  {
    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddOneOther()
    {
      var scenario = new Scenarios.AddOneOther();
      scenario.GivenAnInitial6();
      scenario.WhenYouAddA5();
      scenario.ThenTheResultIs11();
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddTwoOthers()
    {
      var scenario = new Scenarios.AddTwoOthers();
      scenario.GivenAnInitial6();
      scenario.WhenYouAddA8();
      scenario.WhenYouAddA4();
      scenario.ThenTheResultIs18();
    }
  }
}

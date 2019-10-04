namespace Cornichon.Accumulator
{
  using Microsoft.VisualStudio.TestTools.UnitTesting;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestClass]
  public class Feature
  {
    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddOneOther(uint value, uint second, uint sum)
    {
      var instance = new Cornichon.Accumulator.Scenarios.AddOneOther();
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddTwoOthers(uint value, uint second, uint third, uint sum)
    {
      var instance = new Cornichon.Accumulator.Scenarios.AddTwoOthers();
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.WhenYouAddA(third);
      instance.ThenTheResultIs(sum);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddOneOther123()
    {
      AddOneOther(1, 2, 3);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddOneOther224()
    {
      AddOneOther(2, 2, 4);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddTwoOthers1236()
    {
      AddTwoOthers(1, 2, 3, 6);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [TestMethod]
    public void AddTwoOthers2349()
    {
      AddTwoOthers(2, 3, 4, 9);
    }
  }
}

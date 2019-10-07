namespace Cornichon.Accumulator
{
  using NUnit.Framework;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestFixture]
  public class Feature
  {
    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddOneOther(uint value, uint second, uint sum)
    {
      var scenario = new Scenarios.AddOneOther();
      scenario.GivenAnInitial(value);
      scenario.WhenYouAddA(second);
      scenario.ThenTheResultIs(sum);
    }

    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddTwoOthers(uint value, uint second, uint third, uint sum)
    {
      var scenario = new Scenarios.AddTwoOthers();
      scenario.GivenAnInitial(value);
      scenario.WhenYouAddA(second);
      scenario.WhenYouAddA(third);
      scenario.ThenTheResultIs(sum);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [Test]
    public void AddOneOther123()
    {
      AddOneOther(1, 2, 3);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [Test]
    public void AddOneOther224()
    {
      AddOneOther(2, 2, 4);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [Test]
    public void AddTwoOthers1236()
    {
      AddTwoOthers(1, 2, 3, 6);
    }

    /// <summary>
    /// Gherkin DSL test
    /// </summary>
    [Test]
    public void AddTwoOthers2349()
    {
      AddTwoOthers(2, 3, 4, 9);
    }
  }
}

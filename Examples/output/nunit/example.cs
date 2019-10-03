namespace Cornichon.Example
{
  using NUnit.Framework;

  /// <summary>
  /// Gherkin DSL feature
  /// </summary>
  [TestFixture]
  public class Accumulator
  {
    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddOneOther(uint value, uint second, uint sum)
    {
      var instance = new Cornichon.Example.Helpers.AddOneOther();
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    /// <summary>
    /// Gherkin DSL scenario
    /// </summary>
    private static void AddTwoOthers(uint value, uint second, uint third, uint sum)
    {
      var instance = new Cornichon.Example.Helpers.AddTwoOthers();
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.WhenYouAddA(third);
      instance.ThenTheResultIs(sum);
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

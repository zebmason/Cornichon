namespace Cornichon.Accumulator2.Scenarios
{
  /// <summary>
  /// Test class scenario
  /// </summary>
  public class AddOneOther
  {
    /// <summary>
    /// Constructor
    /// </summary>
    public AddOneOther()
    {
      System.Console.WriteLine("  Feature: Accumulator2");
      System.Console.WriteLine("    Scenario: Add one other");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void GivenAnInitial6()
    {
      System.Console.WriteLine("      Given an initial 6");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void WhenYouAddA5()
    {
      System.Console.WriteLine("      When you add a 5");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void ThenTheResultIs11()
    {
      System.Console.WriteLine("      Then the result is 11");
    }
  }

  /// <summary>
  /// Test class scenario
  /// </summary>
  public class AddTwoOthers
  {
    /// <summary>
    /// Constructor
    /// </summary>
    public AddTwoOthers()
    {
      System.Console.WriteLine("  Feature: Accumulator2");
      System.Console.WriteLine("    Scenario: Add two others");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void GivenAnInitial6()
    {
      System.Console.WriteLine("      Given an initial 6");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void WhenYouAddA8()
    {
      System.Console.WriteLine("      When you add a 8");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void WhenYouAddA4()
    {
      System.Console.WriteLine("      When you add a 4");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void ThenTheResultIs18()
    {
      System.Console.WriteLine("      Then the result is 18");
    }
  }
}

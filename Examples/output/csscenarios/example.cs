namespace Cornichon.Accumulator.Scenarios
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
      System.Console.WriteLine("  Feature: Accumulator");
      System.Console.WriteLine("    Scenario: Add one other");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void GivenAnInitial(uint value)
    {
      System.Console.WriteLine("      Given an initial " + value);
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void WhenYouAddA(uint second)
    {
      System.Console.WriteLine("      When you add a " + second);
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void ThenTheResultIs(uint sum)
    {
      System.Console.WriteLine("      Then the result is " + sum);
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
      System.Console.WriteLine("  Feature: Accumulator");
      System.Console.WriteLine("    Scenario: Add two others");
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void GivenAnInitial(uint value)
    {
      System.Console.WriteLine("      Given an initial " + value);
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void WhenYouAddA(uint second)
    {
      System.Console.WriteLine("      When you add a " + second);
    }

    /// <summary>
    /// Gherkin DSL step
    /// </summary>
    public void ThenTheResultIs(uint sum)
    {
      System.Console.WriteLine("      Then the result is " + sum);
    }
  }
}

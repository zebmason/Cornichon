// Copyright (c) 2019 ...

#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace Cornichon::Accumulator::Scenarios
{
  /// Test class scenario
  class AddOneOther
  {
  public:
    /// Constructor
    AddOneOther()
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add one other" << std::endl;
    }

    /// Gherkin DSL step
    void GivenAnInitial(unsigned int value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    /// Gherkin DSL step
    void WhenYouAddA(unsigned int second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    /// Gherkin DSL step
    void ThenTheResultIs(unsigned int sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }
  };

  /// Test class scenario
  class AddTwoOthers
  {
  public:
    /// Constructor
    AddTwoOthers()
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add two others" << std::endl;
    }

    /// Gherkin DSL step
    void GivenAnInitial(unsigned int value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    /// Gherkin DSL step
    void WhenYouAddA(unsigned int second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    /// Gherkin DSL step
    void ThenTheResultIs(unsigned int sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }
  };
}

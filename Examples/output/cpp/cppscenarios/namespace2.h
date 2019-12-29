// Copyright (c) 2019 ...

#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace Cornichon { namespace Accumulator2 { namespace Scenarios
{
  /// Test class scenario
  class AddOneOther
  {
  public:
    /// Constructor
    AddOneOther()
    {
      std::clog << "  Feature: Accumulator2" << std::endl;
      std::clog << "    Scenario: Add one other" << std::endl;
    }

    /// Gherkin DSL step
    void GivenAnInitial6()
    {
      std::clog << "      Given an initial 6" << std::endl;
    }

    /// Gherkin DSL step
    void WhenYouAddA5()
    {
      std::clog << "      When you add a 5" << std::endl;
    }

    /// Gherkin DSL step
    void ThenTheResultIs11()
    {
      std::clog << "      Then the result is 11" << std::endl;
    }
  };

  /// Test class scenario
  class AddTwoOthers
  {
  public:
    /// Constructor
    AddTwoOthers()
    {
      std::clog << "  Feature: Accumulator2" << std::endl;
      std::clog << "    Scenario: Add two others" << std::endl;
    }

    /// Gherkin DSL step
    void GivenAnInitial6()
    {
      std::clog << "      Given an initial 6" << std::endl;
    }

    /// Gherkin DSL step
    void WhenYouAddA8()
    {
      std::clog << "      When you add a 8" << std::endl;
    }

    /// Gherkin DSL step
    void WhenYouAddA4()
    {
      std::clog << "      When you add a 4" << std::endl;
    }

    /// Gherkin DSL step
    void ThenTheResultIs18()
    {
      std::clog << "      Then the result is 18" << std::endl;
    }
  };
} } }

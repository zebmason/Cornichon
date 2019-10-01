// Copyright (c) 2019 ...

#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace Cornichon::Helpers
{
  class AddOneOther
  {
  public:
    AddOneOther()
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add one other" << std::endl;
    }

    void GivenAnInitial(unsigned int value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    void WhenYouAddA(unsigned int second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    void ThenTheResultIs(unsigned int sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }
  };

  class AddTwoOthers
  {
  public:
    AddTwoOthers()
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add two others" << std::endl;
    }

    void GivenAnInitial(unsigned int value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    void WhenYouAddA(unsigned int second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    void ThenTheResultIs(unsigned int sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }
  };
}

// Copyright (c) 2019 ...

#pragma once

// Local headers

// Third party headers

// Standard library headers
#include <iostream>
#include <string>

namespace Cornichon::Helpers
{
  class Accumulator
  {
  public:

    void GivenAnInitial(std::string value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    void WhenYouAddA(std::string second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    void ThenTheResultIs(std::string sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }
  };
}

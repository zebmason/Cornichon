// Copyright (c) 2019 ...

// Other bespoke headers
#include "../helpers/example.h"

// Third party headers
#include "gtest/gtest.h"

namespace Cornichon::Example
{
  static void AddOneOther(unsigned int value, unsigned int second, unsigned int sum)
  {
    Cornichon::Example::Helpers::AddOneOther instance;
    instance.GivenAnInitial(value);
    instance.WhenYouAddA(second);
    instance.ThenTheResultIs(sum);
  }

  static void AddTwoOthers(unsigned int value, unsigned int second, unsigned int third, unsigned int sum)
  {
    Cornichon::Example::Helpers::AddTwoOthers instance;
    instance.GivenAnInitial(value);
    instance.WhenYouAddA(second);
    instance.WhenYouAddA(third);
    instance.ThenTheResultIs(sum);
  }

  TEST(Example, AddOneOther123)
  {
    AddOneOther(1, 2, 3);
  }

  TEST(Example, AddOneOther224)
  {
    AddOneOther(2, 2, 4);
  }

  TEST(Example, AddTwoOthers1236)
  {
    AddTwoOthers(1, 2, 3, 6);
  }

  TEST(Example, AddTwoOthers2349)
  {
    AddTwoOthers(2, 3, 4, 9);
  }
}

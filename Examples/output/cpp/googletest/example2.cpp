// Copyright (c) 2019 ...

// Other bespoke headers
#include "../cppscenarios/example2.h"

// Third party headers
#include "gtest/gtest.h"

namespace Cornichon::Accumulator2
{
  TEST(Accumulator2, AddOneOther)
  {
    Scenarios::AddOneOther scenario;
    scenario.GivenAnInitial6();
    scenario.WhenYouAddA5();
    scenario.ThenTheResultIs11();
  }

  TEST(Accumulator2, AddTwoOthers)
  {
    Scenarios::AddTwoOthers scenario;
    scenario.GivenAnInitial6();
    scenario.WhenYouAddA8();
    scenario.WhenYouAddA4();
    scenario.ThenTheResultIs18();
  }
}

// Copyright (c) 2019 ...

// Other bespoke headers
#include "../cppscenarios/example2.h"

// Third party headers
#include "gtest/gtest.h"

namespace Cornichon::Accumulator2
{
  class TestFixture : public ::testing::Test
  {
  protected:
    void SetUp() override
    {
    }

    void TearDown() override
    {
    }
  };

  TEST_F(TestFixture, AddOneOther)
  {
    Scenarios::AddOneOther scenario;
    scenario.GivenAnInitial6();
    scenario.WhenYouAddA5();
    scenario.ThenTheResultIs11();
  }

  TEST_F(TestFixture, AddTwoOthers)
  {
    Scenarios::AddTwoOthers scenario;
    scenario.GivenAnInitial6();
    scenario.WhenYouAddA8();
    scenario.WhenYouAddA4();
    scenario.ThenTheResultIs18();
  }
}

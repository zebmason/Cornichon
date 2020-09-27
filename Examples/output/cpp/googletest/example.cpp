// Copyright (c) 2019 ...

// Other bespoke headers
#include "../cppscenarios/example.h"

// Third party headers
#include "gtest/gtest.h"

namespace Cornichon::Accumulator
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

  static void AddOneOther(unsigned int value, unsigned int second, unsigned int sum)
  {
    Scenarios::AddOneOther scenario;
    scenario.GivenAnInitial(value);
    scenario.WhenYouAddA(second);
    scenario.ThenTheResultIs(sum);
  }

  static void AddTwoOthers(unsigned int value, unsigned int second, unsigned int third, unsigned int sum)
  {
    Scenarios::AddTwoOthers scenario;
    scenario.GivenAnInitial(value);
    scenario.WhenYouAddA(second);
    scenario.WhenYouAddA(third);
    scenario.ThenTheResultIs(sum);
  }

  TEST_F(TestFixture, AddOneOther123)
  {
    AddOneOther(1, 2, 3);
  }

  TEST_F(TestFixture, AddOneOther224)
  {
    AddOneOther(2, 2, 4);
  }

  TEST_F(TestFixture, AddTwoOthers1236)
  {
    AddTwoOthers(1, 2, 3, 6);
  }

  TEST_F(TestFixture, AddTwoOthers2349)
  {
    AddTwoOthers(2, 3, 4, 9);
  }
}

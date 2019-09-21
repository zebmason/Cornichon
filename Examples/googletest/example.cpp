// Copyright (c) 2019 ...

// Other bespoke headers
#include "../helpers/example.h"

// Third party headers
#include "gtest/gtest.h"

#define AddOneOtherInst(_VALUE, _SECOND, _SUM) \
  TEST(Example, AddOneOther ## _VALUE ## _SECOND ## _SUM) \
  { \
    AddOneOther(#_VALUE, #_SECOND, #_SUM); \
  }

#define AddTwoOthersInst(_VALUE, _SECOND, _THIRD, _SUM) \
  TEST(Example, AddTwoOthers ## _VALUE ## _SECOND ## _THIRD ## _SUM) \
  { \
    AddTwoOthers(#_VALUE, #_SECOND, #_THIRD, #_SUM); \
  }

namespace Cornichon::Example
{
  static void AddOneOther(std::string value, std::string second, std::string sum)
  {
    std::clog << "  Feature: Accumulator" << std::endl;
    std::clog << "    Scenario: Add one other" << std::endl;
    Cornichon::Helpers::Accumulator instance;
    instance.GivenAnInitial(value);
    instance.WhenYouAddA(second);
    instance.ThenTheResultIs(sum);
  }

  static void AddTwoOthers(std::string value, std::string second, std::string third, std::string sum)
  {
    std::clog << "  Feature: Accumulator" << std::endl;
    std::clog << "    Scenario: Add two others" << std::endl;
    Cornichon::Helpers::Accumulator instance;
    instance.GivenAnInitial(value);
    instance.WhenYouAddA(second);
    instance.WhenYouAddA(third);
    instance.ThenTheResultIs(sum);
  }

  AddOneOtherInst(1, 2, 3);

  AddOneOtherInst(2, 2, 4);

  AddTwoOthersInst(1, 2, 3, 6);

  AddTwoOthersInst(2, 3, 4, 9);
}

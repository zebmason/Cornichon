// Copyright (c) 2019 ...

// Other bespoke headers
#include "../helpers/example.h"

// Third party headers
#include "gtest/gtest.h"

#define AddOneOtherInst(_VALUE, _SECOND, _SUM) \
  TEST(Example, AddOneOther ## _VALUE ## _SECOND ## _SUM) \
  { \
    AddOneOther(_VALUE, _SECOND, _SUM); \
  }

#define AddTwoOthersInst(_VALUE, _SECOND, _THIRD, _SUM) \
  TEST(Example, AddTwoOthers ## _VALUE ## _SECOND ## _THIRD ## _SUM) \
  { \
    AddTwoOthers(_VALUE, _SECOND, _THIRD, _SUM); \
  }

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

  AddOneOtherInst(1, 2, 3);

  AddOneOtherInst(2, 2, 4);

  AddTwoOthersInst(1, 2, 3, 6);

  AddTwoOthersInst(2, 3, 4, 9);
}

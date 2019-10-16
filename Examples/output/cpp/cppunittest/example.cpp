// Other bespoke headers
#include "../cppscenarios/example.h"

// Third party headers
#include "CppUnitTest.h"

namespace Cornichon::Accumulator
{
  TEST_CLASS(Feature)
  {
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

    TEST_METHOD(AddOneOther123)
    {
      AddOneOther(1, 2, 3);
    }

    TEST_METHOD(AddOneOther224)
    {
      AddOneOther(2, 2, 4);
    }

    TEST_METHOD(AddTwoOthers1236)
    {
      AddTwoOthers(1, 2, 3, 6);
    }

    TEST_METHOD(AddTwoOthers2349)
    {
      AddTwoOthers(2, 3, 4, 9);
    }
  };
}

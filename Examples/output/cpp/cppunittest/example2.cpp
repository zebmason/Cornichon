// Other bespoke headers
#include "../cppscenarios/example2.h"

// Third party headers
#include "CppUnitTest.h"

namespace Cornichon::Accumulator2
{
  TEST_CLASS(Feature)
  {
    TEST_METHOD(AddOneOther)
    {
      Scenarios::AddOneOther scenario;
      scenario.GivenAnInitial6();
      scenario.WhenYouAddA5();
      scenario.ThenTheResultIs11();
    }

    TEST_METHOD(AddTwoOthers)
    {
      Scenarios::AddTwoOthers scenario;
      scenario.GivenAnInitial6();
      scenario.WhenYouAddA8();
      scenario.WhenYouAddA4();
      scenario.ThenTheResultIs18();
    }
  };
}

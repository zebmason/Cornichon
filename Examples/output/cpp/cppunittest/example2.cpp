// Other bespoke headers
#include "../cppscenarios/example2.h"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

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

    TEST_CLASS_INITIALIZE(ClassInitialize)
    {
      std::clog << "Entering Accumulator2" << std::endl;
    }

    TEST_CLASS_CLEANUP(ClassCleanup)
    {
      std::clog << "Exiting Accumulator2" << std::endl;
    }
  };
}

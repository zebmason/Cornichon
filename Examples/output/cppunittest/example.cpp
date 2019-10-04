// Local headers
#include "stdafx.h"

// Other bespoke headers
#include "../cppscenarios/example.h"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Cornichon::Example
{
  TEST_CLASS(Accumulator)
  {
    static void AddOneOther(unsigned int value, unsigned int second, unsigned int sum)
    {
      Cornichon::Example::Scenarios::AddOneOther instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    static void AddTwoOthers(unsigned int value, unsigned int second, unsigned int third, unsigned int sum)
    {
      Cornichon::Example::Scenarios::AddTwoOthers instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.WhenYouAddA(third);
      instance.ThenTheResultIs(sum);
    }


    TEST_CLASS_INITIALIZE(ClassInitialize)
    {
      std::clog << "Entering example" << std::endl;
    }

    TEST_CLASS_CLEANUP(ClassCleanup)
    {
      std::clog << "Exiting example" << std::endl;
    }

  public:

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

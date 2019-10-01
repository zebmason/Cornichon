// Local headers
#include "stdafx.h"

// Other bespoke headers
#include "../helpers/example.h"

// Third party headers
#include "CppUnitTest.h"

// Standard library headers
#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

#define AddOneOtherInst(_VALUE, _SECOND, _SUM) \
  TEST_METHOD(AddOneOther ## _VALUE ## _SECOND ## _SUM) \
  { \
    AddOneOther(_VALUE, _SECOND, _SUM); \
  }

#define AddTwoOthersInst(_VALUE, _SECOND, _THIRD, _SUM) \
  TEST_METHOD(AddTwoOthers ## _VALUE ## _SECOND ## _THIRD ## _SUM) \
  { \
    AddTwoOthers(_VALUE, _SECOND, _THIRD, _SUM); \
  }


namespace Cornichon::Example
{
  TEST_CLASS(Accumulator)
  {
    static void AddOneOther(unsigned int value, unsigned int second, unsigned int sum)
    {
      Cornichon::Helpers::AddOneOther instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    static void AddTwoOthers(unsigned int value, unsigned int second, unsigned int third, unsigned int sum)
    {
      Cornichon::Helpers::AddTwoOthers instance;
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

    AddOneOtherInst(1, 2, 3);

    AddOneOtherInst(2, 2, 4);

    AddTwoOthersInst(1, 2, 3, 6);

    AddTwoOthersInst(2, 3, 4, 9);
  };
}

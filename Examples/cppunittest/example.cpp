#include "stdafx.h"

// Other bespoke headers
#include "../helpers/example.h"
#include "../helpers/LogStream.h"

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
    static std::streambuf* oldBuffer;
    static std::shared_ptr<std::streambuf> newBuffer;

    static void AddOneOther(unsigned int value, unsigned int second, unsigned int sum)
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add one other" << std::endl;
      Cornichon::Helpers::Accumulator instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    static void AddTwoOthers(unsigned int value, unsigned int second, unsigned int third, unsigned int sum)
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add two others" << std::endl;
      Cornichon::Helpers::Accumulator instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.WhenYouAddA(third);
      instance.ThenTheResultIs(sum);
    }


    TEST_CLASS_INITIALIZE(ClassInitialize)
    {
      newBuffer = std::make_shared<TestUtils::LogStream>();
      oldBuffer = std::clog.rdbuf(newBuffer.get());
      std::clog << "Entering example" << std::endl;
    }

    TEST_CLASS_CLEANUP(ClassCleanup)
    {
      std::clog << "Exiting example" << std::endl;
      std::clog.rdbuf(oldBuffer);
      newBuffer = nullptr;
    }

  public:

    AddOneOtherInst(1, 2, 3);

    AddOneOtherInst(2, 2, 4);

    AddTwoOthersInst(1, 2, 3, 6);

    AddTwoOthersInst(2, 3, 4, 9);
  };

  std::streambuf* Accumulator::oldBuffer = nullptr;
  std::shared_ptr<std::streambuf> Accumulator::newBuffer = nullptr;
}


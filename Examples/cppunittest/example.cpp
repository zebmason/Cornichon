#include "stdafx.h"
#include "CppUnitTest.h"

#include "TestUtils/LogStream.h"

#include <iostream>
#include <memory>

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

#define AddOneOtherInst(_VALUE, _SECOND, _SUM) \
  TEST_METHOD(AddOneOther ## _VALUE ## _SECOND ## _SUM) \
  { \
    AddOneOther(#_VALUE, #_SECOND, #_SUM); \
  }

#define AddTwoOthersInst(_VALUE, _SECOND, _THIRD, _SUM) \
  TEST_METHOD(AddTwoOthers ## _VALUE ## _SECOND ## _THIRD ## _SUM) \
  { \
    AddTwoOthers(#_VALUE, #_SECOND, #_THIRD, #_SUM); \
  }


namespace Cornichon::Example
{
  TEST_CLASS(Accumulator)
  {
    static std::streambuf* oldBuffer;
    static std::shared_ptr<std::streambuf> newBuffer;

    void GivenAnInitial(std::string value)
    {
      std::clog << "      Given an initial " << value << std::endl;
    }

    void WhenYouAddA(std::string second)
    {
      std::clog << "      When you add a " << second << std::endl;
    }

    void ThenTheResultIs(std::string sum)
    {
      std::clog << "      Then the result is " << sum << std::endl;
    }

    static void AddOneOther(std::string value, std::string second, std::string sum)
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add one other" << std::endl;
      Accumulator instance;
      instance.GivenAnInitial(value);
      instance.WhenYouAddA(second);
      instance.ThenTheResultIs(sum);
    }

    static void AddTwoOthers(std::string value, std::string second, std::string third, std::string sum)
    {
      std::clog << "  Feature: Accumulator" << std::endl;
      std::clog << "    Scenario: Add two others" << std::endl;
      Accumulator instance;
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


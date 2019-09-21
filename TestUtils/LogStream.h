#pragma once

#include "stdafx.h"
#include "CppUnitTest.h"

#include <vector>

namespace TestUtils
{
	class LogStream : public std::streambuf
	{
		std::vector<char> buffer;

		int_type overflow(int_type ch)
		{
			if (ch != traits_type::eof())
				buffer.push_back(ch);
			return ch;
		}

		int sync()
		{
			if (buffer.back() == '\n')
				buffer.pop_back();
			buffer.emplace_back('\0');
			Microsoft::VisualStudio::CppUnitTestFramework::Logger::WriteMessage(&buffer[0]);
			buffer.clear();
			return 0;
		}

	};
}


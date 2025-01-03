﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CPP
{
    public class ConcurrencyWithModernCPP : QNABase
    {
        public ConcurrencyWithModernCPP()
        : base(title: "Concurrency with Modern C++ by Rainer Grimm", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "ConcurrencyWithModernCPP";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>()
        {
            {1, new Dictionary<string, string>() // Chapter 1 - Concurrency with Modern C++
                {
                    { "q", @"
State the STL functionality that you should consider if you want to ensure that a Callable object `f`
is called exactly once, even if call concurrently from several threads.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::once_flag in combination with std::call_once - see snippet
"
                    },
                    {"snippetA", @"
#include <mutex>
#include <print>

std::once_flag g_flag1, g_flag2;

void simple_do_once()
{
	std::call_once(g_flag1, []() {std::println(""Simple example: called once""); });
}

void may_throw_function(bool do_throw)
{
	if (do_throw)
	{
		std::println(""Throw: call_once will retry"");
		throw std::exception{};
	}
	std::println(""Did not throw, call_once will not attempt again"");
}

void do_once(bool do_throw)
{
	try
	{
		std::call_once(g_flag2, may_throw_function, do_throw);
	}
	catch(...) {}
}

void for_main()
{
	std::thread t1{ simple_do_once };
	std::thread t2{ simple_do_once };
	std::thread t3{ simple_do_once };
	std::thread t4{ simple_do_once };

	t1.join();
	t2.join();
	t3.join();
	t4.join();

	std::thread do_once_thread1{ do_once, true };
	std::thread do_once_thread2{ do_once, true };
	std::thread do_once_thread3{ do_once, false };
	std::thread do_once_thread4{ do_once, true };

	do_once_thread1.join();
	do_once_thread2.join();
	do_once_thread3.join();
	do_once_thread4.join();
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {2, new Dictionary<string, string>()
                {
                    { "q", @"
What problem does std::condition_variable solve compared to a standard mutex synchronization
primitive?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
A std::condition_variable allows threads to wait for a notification without actively 
consuming CPU resources.

Instead of continuously checking (busy waiting) to acquire a mutex, waiting threads
are put to sleep and only wake up when notified, making synchronization more efficient.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {3, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {4, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {5, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {6, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {7, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {8, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {9, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {10, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {11, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {12, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {13, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {14, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {15, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {16, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {17, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {18, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {19, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {20, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {21, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {22, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {23, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {24, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {25, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {26, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {27, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {28, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {29, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {30, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {31, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {32, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {33, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {34, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {35, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {36, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {37, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {38, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {39, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {40, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {41, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {42, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {43, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {44, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {45, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {46, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {47, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {48, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {49, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {50, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {51, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {52, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {53, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {54, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {55, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {56, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {57, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {58, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {59, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {60, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {61, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {62, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {63, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {64, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {65, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {66, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {67, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {68, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {69, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {70, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {71, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {72, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {73, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {74, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {75, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {76, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {77, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {78, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {79, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {80, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {81, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {82, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {83, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {84, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {85, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {86, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {87, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {88, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {89, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {90, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {91, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {92, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {93, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {94, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {95, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {96, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {97, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {98, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {99, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {100, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {101, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {102, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {103, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {104, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {105, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {106, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {107, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {108, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {109, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {110, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {111, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {112, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {113, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {114, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {115, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {116, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {117, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {118, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {119, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {120, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {121, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {122, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {123, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {124, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {125, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {126, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {127, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {128, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {129, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {130, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {131, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {132, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {133, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {134, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {135, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {136, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {137, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {138, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {139, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {140, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {141, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {142, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {143, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {144, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {145, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {146, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {147, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {148, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {149, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {150, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {151, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {152, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {153, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {154, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {155, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {156, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {157, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {158, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {159, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {160, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {161, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {162, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {163, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {164, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {165, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {166, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {167, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {168, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {169, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {170, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {171, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {172, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {173, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {174, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {175, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {176, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {177, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {178, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {179, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {180, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {181, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {182, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {183, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {184, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {185, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {186, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {187, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {188, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {189, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {190, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {191, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {192, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {193, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {194, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {195, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {196, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {197, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {198, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {199, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {200, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },

        };

    }
}

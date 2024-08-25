using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.Test
{
    public class TestLatexSnippetLogic : QNABase
    {
        public TestLatexSnippetLogic()
        : base(title: "TestLatexSnippetLogic", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "TestLatexSnippetLogic";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>()
        {
            {1, new Dictionary<string, string>()
                {
                    { "q", @"
i) What is an initializer-list constructor?
ii) Let EvenSquence be a proposed class. Write the sequence for an
EvenSequence initializer-list constructor for arguments of type double." },
                    { "a", @"
i) An initializer-list constructor is a construct with only std::initializer_list<T> as first parameter." },
                    {"snippetA", @"
#include <initializer_list>
class EvenSequence
{
public:
	EvenSequence(std::initializer_list<double> args)
	{
	}
};"                 
                    }
                }
            },
            {2, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet (assume Simple is a defined class):
Example what's happening in:
		i) line (1)
		ii) line (2)
"                   },
                    {"snippetQ",@"
(1)	p_unq_simple.reset();
(2)	p_unq_simple.reset(new Simple());" },
                    { "a", @"
i) Free the resource and set to nullptr.
ii) Free the resource and set to a new simple instance."
                    },
                }
            }
        };
    }
}

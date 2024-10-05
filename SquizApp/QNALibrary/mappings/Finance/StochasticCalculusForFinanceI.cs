using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.Finance
{
    public class StochasticCalculusForFinanceI : QNABase
    {

        public StochasticCalculusForFinanceI()
        : base(title: "Stephen Shreves's Stochastic Calculus For Finance I", category: QNACategory.Finance, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "StochasticCalculusForFinanceI";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>()
        {
            {1, new Dictionary<string, string>() // Chapter1: The Binomial No-Arbitrage Pricing Model
                {
                    { "q", @"
                    a) How does this book define arbitrage?
                    b) True or false:
                            A mathematical model that admits arbitrage cannot be used for analysis.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
                    a) As a trading strategy that:
                        - begins with no money
                        - has zero probability of losing money
                        - has positive probability of making money

                    b) True.
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
            {2, new Dictionary<string, string>()
                {
                    { "q", @"
                    d be a down factor
                    u be the up factor
                    r be the risk-free rate of interest
            
                    In the one-period binomial model, to rule out arbitrage we must assume:
                        0 < d < 1 + r < u
                    explain what would happen if any of the following hold:
                        a) d <= 0
                        b) d >= 1 + r
                        c) u <= 1 + r
        
"                   },
                    {"snippetQ", @"
                    
"},
                    { "a", @"
                    a) d > 0 follows from the positivity of stock prices. If we have S_0 at time 0 and d_0*s_0 at time 1
                    such that:
                        S_0 > d * S_1 > 0
                    then we have:
                        (S_0 / S_1) > d > 0

                    b) If d >= 1 + r  - we can employ the strategy:
                    Time t=0:
                        - start off with zero wealth
                        - borrow from the money market in order to buy S (at S_0)
                    Time t=1:
                        - Worse can scenario the value of S (S_1) would be equal to your debt 1+r
                        - in the alternative scenario S_1 is worth more than your debt - yield a profit

                    The inequality d >= 1 + r thus presents an arbitrage opportunity.

                    c) If u <= 1 + r  - we can employ the strategy:
                    Time t=0:
                            - Sell the stock short (for S_0)
                            - Invest the proceeds in the money market at r
                    Time t=1:
                        - In the 'up' case, the case of covering the short position will be equal
                            to the return earned on the money market investment at r.
                        - There is a positive probability that the cost of covering the short position will be less
                            than the money market investment (the 'down' case) - since d < u <= 1+r in this world.

                    The inequality u <= 1 + r thus presents an arbitrage opportunity.
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

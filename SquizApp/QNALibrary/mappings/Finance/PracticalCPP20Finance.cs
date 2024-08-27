using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.Finance
{
    public partial class PracticalCPP20Finance : QNABase
    {
        public PracticalCPP20Finance()
        : base(title: "Bob Steiner's Key Financial Markets Concepts", category: QNACategory.Finance, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "PracticalCPP20Finance";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"Why do conservative money managers view the fixed income market as
		a safer investment option compared to stocks and more exotic derivatives?"},
        {"a", @"Because fixed income has a predictable income stream."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"In a fixed income investment, a contractually defined exchange
		occurs between two parties. What do the two parties agree to exchange?"},
        {"a", @"The two parties agree to exchange cash flows that are assigned based
		on interest rates and the time of cash exchanges."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"State three well-known types of fixed income investment vehicles?"},
        {"a", @"1) Money market funds
		2) Bonds
		3) Certificates of deposit"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"What is a mutual fund?"},
        {"a", @"A mutual fund:

			- a type of investment vehicle consisting of a portfolio of stocks,
				bonds, or other securities.
			- gives small or individual investors access to diversified, professionally
				managed portfolios at a low price.
			- are operated by professional money managers, who allocate the fund's 
				assets and attempt to produce capital gains or income for the fund's
				investors."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"What does NAVPS stand for?"},
        {"a", @"Net asset value per shared, it is used to refer to the price of a mutual
		fund."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"i) What does LIBOR stand for?
		ii) Given your answer to (i), what is LIBOR?
		iii) a) When will LIBOR be phased out in the UK?
		     b) What will be replacing LIBOR?"},
        {"a", @"i) London Interbank Offered Rate
		ii)
			- LIBOR serves as a globally accepted key benchmark interest rate
				that indicates borrowing costs between banks.
			- the average interest rate at which major global banks borrow from
				one another.
		iii) a) June 20, 2023
			 b) SOFR (Secured Overnight Financing Rate)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"What does term `tenor` refer to?"},
        {"a", @"Tenor:
			- refers to the length of time remaining before a financial contract
			 expires.
			- tenor is used in relation to bank loans, insurance contracts, and
				derivative products."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"The term `tenor` is often used interchangeably with the term `maturity`,
		despite having distinct meanings.
		Outline the distinction between the two terms."},
        {"a", @"Tenor:
			- describes the length of time remaining in a financial contract.
			- often used when describing bank loans and insurance contracts
		Maturity:
			- refers to the initial length of a contract upon its inception.
			- often used when describing government bonds and corporate bonds."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"What do the following acronyms stand for:

			i) ICE
			ii) IBA"},
        {"a", @"i) Intercontinental exchange
			ii) ICE Benchmark Administration - constitutes a designated panel
				of global banks for each currency and tenor pair."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"i) What are basis points (BPS)?
		ii) What is the relationship between BPS and percentages?
		iii) What are other abbreviations for basis points other than BPS?"},
        {"a", @"i) Basis points (BPS) refers to a common unit of measure for
			interest rates and other percentages in finance.

		ii) 100 BPS = 1% i.e 0.01% = 1 BPS 

		iii) Bp, bps, bips."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"i) What is a credit event?
		ii) State the five most common credit events"},
        {"a", @"i) A credit event is a sudden and tangible (negative) change in a 
			borrower's capacity to meet its payment obligations, which triggers
			a settlement under a credit default swap (CDS) contract.
		ii) 
			1) bankruptcy
			2) payment default
			3) debt restructuring
			4) repudiation
			5) moratorium"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"What is a credit default swap (CDS)?"},
        {"a", @"A credit default swap (CDS) refers to:
			- a financial derivative that allows a bond/IOU investor (protection buyer)
			  to swap or offset their credit risk with that of another investor (protection seller).
			- is triggered by a 'credit event'"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"What is the difference between payment default and bankruptcy?"},
        {"a", @"Bankruptcy:
			- is a legal process
			- tells your creditors that you will not be able to pay them in full
		Payment default:
			- is a specific event
			- tells your creditors that you will not be able to pay them when
				coupons for example are due."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"True or false:
			Credit default swaps are exactly like insurance."},
        {"a", @"False. Although CDS's appear similar to insurance, they are not.
		They are more like options because they bet on whether the credit
		event will or will not occur."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"What is a strike price?"},
        {"a", @"A strike price is a set price at which a derivative contract
		can be bought or sold when it is exercised.

		NB: The terms 'strike price' and 'excercise price' are interchangeable."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"What is the difference between European style options
		and American style options?"},
        {"a", @"European style options:
			- less flexible
			- can only be exercised at expiration
		American style options:
			- more flexible
			- can be exercised at any time prior to expiration"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"i) What is a repo?
		ii) Given your answer to (i), what is a repo rate?"},
        {"a", @"i) A repurchase agreements, or 'repo' is a short-term agreement
			to sell securities in order to buy them back at a slightly
			highter price.

		ii) The repo rate is the implicit interest on these agreements."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"What is meant by liquidity?"},
        {"a", @"Liquidity:
			- refers to the efficiency or ease with which an asset or
				security can be converted into ready cash without
				affecting its market price.
			- of course, the most liquid asset of all is cash itself"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"What is meant by a domestic bond?"},
        {"a", @"A domestic bond is a bond issued by a company based in country A
		in A's currency, to investors/institutions based in A.

		E.g A UK company issuing a bond in GBP to UK-based investors."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"What is a:

		1) yankee bond
		2) bulldog bond
		3) samurai bond
		4) matilda/kangaroo bond
		5) panda bond"},
        {"a", @"1) yankee bonds - USD denominated issues by foreign borrowers
			in the US bond market.

		2) bulldog bonds - sterling denominated foreign bonds which are
			raised in the UK domenstic securities market.

		3) samurai bonds - bonds issued by non-japanese borrowers in
			the domestic Japanese markets.

		4) matilda/kangaroo - non-Australian issues of Australian dollar-denominated
			bonds in the Australian market.

		5) panda bonds - non-Chinese issues of Remnimbi-denominated bonds sold in the
			People's republic of China."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"What is a foreign bond?"},
        {"a", @"A foreign bond is a bond issued in a domestic market
		by a foreign entity in the domestic market's currency
		as a means of raising capital."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"i) What is eurocurrency?

		ii) Give a concrete example of eurocurrency?"},
        {"a", @"i) Eurocurrency is currency held on deposit by governments
			or corporations operating outside of their home market.

		ii) For example, a deposit of USD held in a British bank would be
			considered eurocurrency.
			
			A deposit of GBP made in the United States would be considered
			eurocurrency."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"What is legal tender?"},
        {"a", @"Legal tender is anything recognized by law as a means to settle a public or
		private debt or meet a financial obligation.

		The national currency is legal tender in practically every country."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"What is maturity transformation?"},
        {"a", @"Maturity transformation is when banks take short-term sources of finance,
		such as deposits from savers, and turn them into long-term borrowings, such
		as mortgages."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"What is insolvency?"},
        {"a", @"Insolvency is a term for when an individual or company can no
		longer meet their financial obligations to lenders as debts become
		due."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"i) What is a depository institution?
		ii) Give two examples of depository institutions.
		iii) Give an example of a non-depository institution."},
        {"a", @"i) A depository institution is a financial institution
				in the United States that is legally allowed to accept
				monetary deposits from consumers.

		ii) Acceptable answers include:
			1) savings banks
			2) commercial bank
			3) savings and loan associations
			4) credit unions

		iii) An example of a non-depository institution is a mortgange bank.
			While licensed to lend, they cannot accept deposits."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"What is a reserve requirement?"},
        {"a", @"A reserve requirement is a central bank regulation that sets
		the minimum amount that a commercial bank must hold in liquid
		assets."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"i) What is goodwill?

		ii) What sorts of items are included in goodwill?"},
        {"a", @"i) Goodwill is:
			- an intangible asset
			- the portion of the purchase price that is higher than
				the sum of the net fair value of all of the assets
				purchased in the acquisition and the liabilities assumed in the process.
			
		ii) - items included in goodwill are:
				1) proprietary or intellectual property
				2) brand recognition"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {29, new Dictionary<string, string>() {
        {"q", @"What is negative goodwill?"},
        {"a", @"Negative goodwill (NGW) is a term that refers to the bargain purchase
		amount of money paid, when a company acquires another company or its asset
		for significantly less than the fair market value."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {30, new Dictionary<string, string>() {
        {"q", @"i) What is accounts receivable (AR)
		ii) What is accounts payables (AP)"},
        {"a", @"i) Accounts receivable (AR) is the balance of money due to a firm
			for goods or services delivered or used but not yet paid for by
			customers. 

		ii) Accounts payable (AP) refers to an account within the general
			ledger that represents a company's obligation to pay off a short-term
			debt to its creditors or suppliers."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {31, new Dictionary<string, string>() {
        {"q", @"What is working capital (also new working capital or NWC)?"},
        {"a", @"NWC is the difference between a company's current assets, e.g:
			1) cash
			2) accounts receivable/customers' unpaid bills
			4) inventory of raw and finished goods

		And its current liabilities, such as:
			1) accounts payable
			2) debts"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {32, new Dictionary<string, string>() {
        {"q", @"i) How is gross profit calculated?
		ii) How is gross profit margin calculated?
		iii) How is the markup calculated"},
        {"a", @"Legend:
			COGS = Cost of Goods Sold

		i) Gross profit = Revenue - COGS

		ii) Gross profit margin = Gross profit / Revenue
								= (Revenue - COGS) / Revenue

		iii) Markup = Gross profit / COGS
					= (Revenue - COGS) / COGS"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {33, new Dictionary<string, string>() {
        {"q", @"Let:
			Revenue = 100
			COGS = 80

		Calculate:
			i) the gross profit
			ii) the gross profit margin
			iii) the markup"},
        {"a", @"i) gross profit = revenue - COGS = 100 - 80 = 20
			
			ii) gross profit margin = (revenue - COGS) / revenue
									= (100 - 80) / 100
									= 20%

			iii) markup  = (revenue - COGS) / COGS
						= (100 - 80) / 80
						= 25%"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {34, new Dictionary<string, string>() {
        {"q", @"What is the federal funds rate?"},
        {"a", @"The term 'federal funds rate' refers to the target interest rate
		set by the Federal Reserve.

		This target is the rate at which commercial banks borrow and lend
		their excess reserves to each other overnight on an uncollateralized basis."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {35, new Dictionary<string, string>() {
        {"q", @"i)   What is impairment?
		ii)  What is depreciation?
		iii) What is the difference between depreciation and impairment?"},
        {"a", @"i) Impairment:
				- is a permanent reduction in the value of a company asset.
				- the asset in question may be fixed or intangible


		ii) Depreciation:
				- refers to an accounting method used to allocate the cost
				  of a tangible or physical asset over its useful life.
				- represents how much of an asset's value has been used.
        
        iii) 
            Impairment is unexpected damage to the asset while depreciation is expected wear and tear"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {36, new Dictionary<string, string>() {
        {"q", @"i) What is a nonperforming asset (NPA)?

		ii) What criteria do banks usually have to classify
			assets as nonperforming?"},
        {"a", @"i)	A nonperforming asset (NPA) is a debt instrument where the borrower has
			not made any previously agreed upon interest and principal repayments to
			the designated lender for an extended period of time.

		ii) Either:

			1) 90 days of nonpayment of interest or principal; OR
			2) Failure to pay principal due at maturity."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {37, new Dictionary<string, string>() {
        {"q", @"i) What is a eurobond?

		ii) What are eurobonds also called?

		iii) What are they not to be confused with?

		iv) Give a concrete example of a eurobond, given your answer to (i)"},
        {"a", @"i) A eurobond is an international bond that is denominated in a currency
		not native to the country where it is issued.

		ii) External bonds

		iii) They are not to be confused with eurozone eurobonds, which are
			issued by eurozone states.

		iv) An Australian company issues a bond in USD and sells it in Japan."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {38, new Dictionary<string, string>() {
        {"q", @"i) What is underwriting?
		ii) Where does underwriting fit into the context of IPOs?"},
        {"a", @"i) Underwriting is the process through which an individual or
			institution takes on financial risk for a fee.

		ii) In the context of IPOs, a financial institution may underwrite
			the remaining shared in an IPO to ensure the issuing company
			meets capital requirements."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {39, new Dictionary<string, string>() {
        {"q", @"Consider the statement:

			Interest can be calculated either as a discrete or a continuous compounding process.

		Let:

			- R be the interest rate
			- V be the future value
			- P be the present value
			- N be the number of periods

		i)  Give the formula for discretely compounded interest rate
		ii) Give the formula for continuously compounded interest rate"},
        {"a", @"i)  V = P * ((1 + R)**N)
		ii) V = P * (e**(R * N)) ; where e is Euler's number."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {40, new Dictionary<string, string>() {
        {"q", @"Let:

			- PV be the present value
			- FV be the future that value we want to discount
			- R be the interest rate
			- N be the number of periods between PV and FV

		Give the formula for calculating the present value of a future payment."},
        {"a", @"PV  = FV / ((1 + R) ** N)
				= FV * ((1 + R) ** -N)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {41, new Dictionary<string, string>() {
        {"q", @"What is an exchange-traded fund (ETF)?"},
        {"a", @"An exchange-traded fund is:

			- is a basket of securities that trades on an exchange just like a stock
			- ETFs will track a particular index, sector commodity, or other asset.
			- can be purchased or sold on a stock exchange the same way a regular stock can"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {42, new Dictionary<string, string>() {
        {"q", @"What is sell-side?"},
        {"a", @"Sell-side refers to the part of the financial industry that is 
		involved in the creation, promotion, and sale of:
			- stocks,
			- bonds,
			- foreign exchange
			- other financial instruments"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {43, new Dictionary<string, string>() {
        {"q", @"What is the International Accounting Standards (IAS) definition
		of a financial instrument?"},
        {"a", @"A financial instrument is any contract that gives rise to a financial
		asset of one entity and a financial liability or equity instrument
		of another entity."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {44, new Dictionary<string, string>() {
        {"q", @"What is the buy-side?"},
        {"a", @"The buy-side is a segment of financial markets made up of investing
		institutions that buy securities for money-management purposes."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {45, new Dictionary<string, string>() {
        {"q", @"In the context of technical analysis, what is meant by the:

			1) support
			2) resistance"},
        {"a", @"1) support:
			- occurs where a downtrend is expected to pause due to a concentration
			  of demand.
			- i.e the lowest price an instrument is expected to reach


		2) resistance:
			- occurs where an uptrend is expected to pause temporarily, due to
				a concentraion of supply
			- i.e the highest price an instrument is expected to reach."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {46, new Dictionary<string, string>() {
        {"q", @"i) What does EPS stand for?
		ii) What is the basic version of the formula for calculating
			EPS?"},
        {"a", @"i) Earnings per share
		ii) profit_after_tax_for_year / number_of_shares_in_issue"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {47, new Dictionary<string, string>() {
        {"q", @"What is vesting?"},
        {"a", @"Vesting is a legal term that means to give or earn
		a right to a present or future payment, asset, or benefit.

		The rights are usually earned through time spent in employment.

		'To vest' is the act of exercises such rights/options."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {48, new Dictionary<string, string>() {
        {"q", @"What is a restricted stock unit (RSU)?"},
        {"a", @"An RSU refers to a form of compensation issued by an employer to
		an employee in the form of company shares.

		RSUs are issued to employees after either:
			- achieving required performance milestones; OR
			- upon remaining with their employer for a particular length of time."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {49, new Dictionary<string, string>() {
        {"q", @"What is diluted earnings per share (EPS)?"},
        {"a", @"Diluted EPS considers the:
			profit_after_tax_for_year / number_of_shares_outstanding

		where `number_of_shares_outstanding` includes the hypothetical
		exercise of a company's stock options, warrants and RSUs.

		This consideration would increases the denominators, hence the 
		qualification of 'diluted' EPS."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {50, new Dictionary<string, string>() {
        {"q", @"i) What is a warrant?

		ii) What are two key difference between a warrant and an option?"},
        {"a", @"i) Warrants are a derivative that give the right, but not the obligation
			to buy or sell a security - most commonly an equity - at a certain
			price before expiration.

		ii) Differences:

			1) Warrants are issued by the company itself, not a third part.
			2) Warrants are dilutive - when an investor exercises their warrant
				they receive newly issued stock, rather than already-outstanding stock."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {51, new Dictionary<string, string>() {
        {"q", @"What are the two types of equity/ownership in a firm?"},
        {"a", @"1) Common stock
		2) Preferred stock"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {52, new Dictionary<string, string>() {
        {"q", @"Outline some differences between common stock and preferred stock."},
        {"a", @"Differences:
			- Preferred stockholders have a higher claim on distributions (dividends)
				than common stockholders.
			- Preferred stockholders usually have no or limited voting rights in
				corporate governance.
			- Unlike common stock, preferred stock pay set dividends at regular intervals."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {53, new Dictionary<string, string>() {
        {"q", @"In the event of a liquidation, give the descending order of claim
		on assets for the three categories:

			1) bond holders
			2) common stock holders
			3) preferred stock holders"},
        {"a", @"bond holders > preferred stock holders > common stock holders"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {54, new Dictionary<string, string>() {
        {"q", @"What are callable stock?"},
        {"a", @"Callable stock is shared in a company that the issue can buy back."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {55, new Dictionary<string, string>() {
        {"q", @"i)  What is the book value?
		ii) How is the book value calculated?"},
        {"a", @"i) Book value - corresponds to the amouunt of assets currently on
			the company balance sheet.

		ii) Book value = assets - (liabilities + intangibles)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {56, new Dictionary<string, string>() {
        {"q", @"Give the formula for the price-to-book ratio (P/B)?"},
        {"a", @"price-to-book ratio = stock_price / book_value
							= stock_price / (assets - (liabilities + intangibles))"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {57, new Dictionary<string, string>() {
        {"q", @"What does EBITDA stand for?"},
        {"a", @"EBITDA - Earnings before interest, tax, depreciation and amortization"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {58, new Dictionary<string, string>() {
        {"q", @"What is the American term for 'profit after tax'?"},
        {"a", @"Net income."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {59, new Dictionary<string, string>() {
        {"q", @"Give the i) British and ii) American formulas for 
		return on equity (ROE)."},
        {"a", @"i)  British:
				ROE = profit_after_tax / equity_capital_employed
		ii) American:
				ROE = net_income / shareholders_equity"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {60, new Dictionary<string, string>() {
        {"q", @"What are toxic assets?"},
        {"a", @"Toxic assets are investments that are difficult or impossible to sell
		at any price because the demand for them has collapsed."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {61, new Dictionary<string, string>() {
        {"q", @"What is the difference between a forward and futures contract?"},
        {"a", @"Forward:
			- is a private and customizable agreement
			- settles at the end of the agreement
			- is traded over the counter

		Futures:
			- has standardized terms
			- is traded over an exchange
			- prices are settled on a daily basis until the end of the contract"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {62, new Dictionary<string, string>() {
        {"q", @"What is the:

			1) spot price
			2) futures price
			3) The term for the difference between the spot price and the futures price."},
        {"a", @"1) spot price (of an asset) - is the current cash cost of it for immediate
				purchase and delivery.

			2) futures price (of an asset) - locks in the cost of the asset that will
				be delivered at some point other than the present.

			3) The basis"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {63, new Dictionary<string, string>() {
        {"q", @"i) What is a clearinghouse?

		ii) What do clearinghouses act as third parties for?"},
        {"a", @"i) A clearinghouse:
			- is a designated intermediary between a buyer and a seller in a financial market
			- validates and finalizes the transation, ensuring that both the buyer and 
				seller honour their contractual obligations.

		ii) Clearninghouses act as third parties for futures and options contracts."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {64, new Dictionary<string, string>() {
        {"q", @"In the context of futures markets, what is:

			i) Contango
			ii) Backwardation"},
        {"a", @"i) Contango is a situation where the spot price of an asset
				is lower than the futures price.
			
			ii) Backwardation is a situation where the spot price of an
				asset is higher than the futures price."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}

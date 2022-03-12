# Notes taken in a Q & A style format from Carlos Oliveira's Practical C++20 Financial Programming
qna = {
    1: { # Chapter 1: The Fixed Income Market
		'q':  """
		Why do conservative money managers view the fixed income market as
		a safer investment option compared to stocks and more exotic derivatives?
		""",
		'a': """
		Because fixed income has a predictable income stream.
		""",
	},
    2: {
		'q':  """
		In a fixed income investment, a contractually defined exchange
		occurs between two parties. What do the two parties agree to exchange?
		""",
		'a': """
		The two parties agree to exchange cash flows that are assigned based
		on interest rates and the time of cash exchanges.
		""",
	},
	3: {
		'q':  """
		State three well-known types of fixed income investment vehicles?
		""",
		'a': """
		1) Money market funds
		2) Bonds
		3) Certificates of deposit
		""",
	},
    4: {
		'q':  """
		What is a mutual fund?
		""",
		'a': """
		A mutual fund:

			- a type of investment vehicle consisting of a portfolio of stocks,
				bonds, or other securities.
			- gives small or individual investors access to diversified, professionally
				managed portfolios at a low price.
			- are operated by professional money managers, who allocate the fund's 
				assets and attempt to produce capital gains or income for the fund's
				investors.
		""",
	},
    5: {
		'q':  """
		What does NAVPS stand for?
		""",
		'a': """
		Net asset value per shared, it is used to refer to the price of a mutual
		fund.
		""",
	},
	6: {
		'q':  """
		i) What does LIBOR stand for?
		ii) Given your answer to (i), what is LIBOR?
		iii) a) When will LIBOR be phased out in the UK?
		     b) What will be replacing LIBOR?		
		""",
		'a': """
		i) London Interbank Offered Rate
		ii)
			- LIBOR serves as a globally accepted key benchmark interest rate
				that indicates borrowing costs between banks.
			- the average interest rate at which major global banks borrow from
				one another.
		iii) a) June 20, 2023
			 b) SOFR (Secured Overnight Financing Rate) 
		""",
	},
    7: {
		'q':  """
		What does term `tenor` refer to?
		""",
		'a': """
		Tenor:
			- refers to the length of time remaining before a financial contract
			 expires.
			- tenor is used in relation to bank loans, insurance contracts, and
				derivative products.
		""",
	},
	8: {
		'q':  """
		The term `tenor` is often used interchangeably with the term `maturity`,
		despite having distinct meanings.
		Outline the distinction between the two terms.
		""",
		'a': """
		Tenor:
			- describes the length of time remaining in a financial contract.
			- often used when describing bank loans and insurance contracts
		Maturity:
			- refers to the initial length of a contract upon its inception.
			- often used when describing government bonds and corporate bonds.
		""",
	},
	9: {
		'q':  """
		What do the following acronyms stand for:

			i) ICE
			ii) IBA
		""",
		'a': """
			i) Intercontinental exchange
			ii) ICE Benchmark Administration - constitutes a designated panel
				of global banks for each currency and tenor pair.
		""",
	},
    10: {
		'q':  """
		i) What are basis points (BPS)?
		ii) What is the relationship between BPS and percentages?
		iii) What are other abbreviations for basis points other than BPS?
		""",
		'a': """
		i) Basis points (BPS) refers to a common unit of measure for
			interest rates and other percentages in finance.

		ii) 100 BPS = 1% i.e 0.01% = 1 BPS 

		iii) Bp, bps, bips.
		""",
	},
	11: {
		'q':  """
		i) What is a credit event?
		ii) State the five most common credit events
		""",
		'a': """
		i) A credit event is a sudden and tangible (negative) change in a 
			borrower's capacity to meet its payment obligations, which triggers
			a settlement under a credit default swap (CDS) contract.
		ii) 
			1) bankruptcy
			2) payment default
			3) debt restructuring
			4) repudiation
			5) moratorium
		""",
	},
	12: {
		'q':  """
		What is a credit default swap (CDS)?
		""",
		'a': """
		A credit default swap (CDS) refers to:
			- a financial derivative that allows a bond/IOU investor (protection buyer)
			  to swap or offset their credit risk with that of another investor (protection seller).
			- is triggered by a 'credit event' 
		""",
	},
    13: {
		'q':  """
		What is the difference between payment default and bankruptcy?
		""",
		'a': """
		Bankruptcy:
			- is a legal process
			- tells your creditors that you will not be able to pay them in full
		Payment default:
			- is a specific event
			- tells your creditors that you will not be able to pay them when
				coupons for example are due.
		""",
	},
	14: {
		'q':  """
		True or false:
			Credit default swaps are exactly like insurance.
		""",
		'a': """
		False. Although CDS's appear similar to insurance, they are not.
		They are more like options because they bet on whether the credit
		event will or will not occur.
		""",
	},
	15: {
		'q':  """
		What is a strike price?
		""",
		'a': """
		A strike price is a set price at which a derivative contract
		can be bought or sold when it is exercised.

		NB: The terms 'strike price' and 'excercise price' are interchangeable.
		""",
	},
    16: {
		'q':  """
		What is the difference between European style options
		and American style options?
		""",
		'a': """
		European style options:
			- less flexible
			- can only be exercised at expiration
		American style options:
			- more flexible
			- can be exercised at any time prior to expiration
		""",
	},
	17: {
		'q':  """
		i) What is a repo?
		ii) Given your answer to (i), what is a repo rate?
		""",
		'a': """
		i) A repurchase agreements, or 'repo' is a short-term agreement
			to sell securities in order to buy them back at a slightly
			highter price.

		ii) The repo rate is the implicit interest on these agreements.
		""",
	},
    18: {
		'q':  """
		What is meant by liquidity?
		""",
		'a': """
		Liquidity:
			- refers to the efficiency or ease with which an asset or
				security can be converted into ready cash without
				affecting its market price.
			- of course, the most liquid asset of all is cash itself
		""",
	},
    19: {
		'q':  """
		What is meant by a domestic bond?
		""",
		'a': """
		A domestic bond is a bond issued by a company based in country A
		in A's currency, to investors/institutions based in A.

		E.g A UK company issuing a bond in GBP to UK-based investors.
		""",
	},
    20: {
		'q':  """
		What is a:

		1) yankee bond
		2) bulldog bond
		3) samurai bond
		4) matilda/kangaroo bond
		5) panda bond
		""",
		'a': """
		1) yankee bonds - USD denominated issues by foreign borrowers
			in the US bond market.

		2) bulldog bonds - sterling denominated foreign bonds which are
			raised in the UK domenstic securities market.

		3) samurai bonds - bonds issued by non-japanese borrowers in
			the domestic Japanese markets.

		4) matilda/kangaroo - non-Australian issues of Australian dollar-denominated
			bonds in the Australian market.

		5) panda bonds - non-Chinese issues of Remnimbi-denominated bonds sold in the
			People's republic of China.
		""",
	},
	21: {
		'q':  """
		What is a foreign bond?
		""",
		'a': """
		A foreign bond is a bond issued in a domestic market
		by a foreign entity in the domestic market's currency
		as a means of raising capital.
		""",
	},
    22: {
		'q':  """
		i) What is eurocurrency?

		ii) Give a concrete example of eurocurrency?
		""",
		'a': """
		i) Eurocurrency is currency held on deposit by governments
			or corporations operating outside of their home market.

		ii) For example, a deposit of USD held in a British bank would be
			considered eurocurrency.
			
			A deposit of GBP made in the United States would be considered
			eurocurrency.
		""",
	},
	23: {
		'q':  """
		What is legal tender?
		""",
		'a': """
		Legal tender is anything recognized by law as a means to settle a public or
		private debt or meet a financial obligation.

		The national currency is legal tender in practically every country.
		""",
	},
    24: {
		'q':  """
		What is maturity transformation?
		""",
		'a': """
		Maturity transformation is when banks take short-term sources of finance,
		such as deposits from savers, and turn them into long-term borrowings, such
		as mortgages.
		""",
	},
	25: {
		'q':  """
		What is insolvency?
		""",
		'a': """
		Insolvency is a term for when an individual or company can no
		longer meet their financial obligations to lenders as debts become
		due.
		""",
	},
    26: {
		'q':  """
		i) What is a depository institution?
		ii) Give two examples of depository institutions.
		iii) Give an example of a non-depository institution.
		""",
		'a': """
		i) A depository institution is a financial institution
				in the United States that is legally allowed to accept
				monetary deposits from consumers.

		ii) Acceptable answers include:
			1) savings banks
			2) commercial bank
			3) savings and loan associations
			4) credit unions

		iii) An example of a non-depository institution is a mortgange bank.
			While licensed to lend, they cannot accept deposits.
		""",
	},
	27: {
		'q':  """
		What is a reserve requirement?
		""",
		'a': """
		A reserve requirement is a central bank regulation that sets
		the minimum amount that a commercial bank must hold in liquid
		assets.
		""",
	},
    28: {
		'q':  """
		i) What is goodwill?

		ii) What sorts of items are included in goodwill?
		""",
		'a': """
		i) Goodwill is:
			- an intangible asset
			- the portion of the purchase price that is higher than
				the sum of the net fair value of all of the assets
				purchased in the acquisition and the liabilities assumed in the process.
			
		ii) - items included in goodwill are:
				1) proprietary or intellectual property
				2) brand recognition
		""",
	},
	29: {
		'q':  """
		What is negative goodwill?
		""",
		'a': """
		Negative goodwill (NGW) is a term that refers to the bargain purchase
		amount of money paid, when a company acquires another company or its asset
		for significantly less than the fair market value.
		""",
	},
    30: {
		'q':  """
		i) What is accounts receivable (AR)
		ii) What is accounts payables (AP)
		""",
		'a': """
		i) Accounts receivable (AR) is the balance of money due to a firm
			for goods or services delivered or used but not yet paid for by
			customers. 

		ii) Accounts payable (AP) refers to an account within the general
			ledger that represents a company's obligation to pay off a short-term
			debt to its creditors or suppliers.
		""",
	},
	31: {
		'q':  """
		What is working capital (also new working capital or NWC)?
		""",
		'a': """
		NWC is the difference between a company's current assets, e.g:
			1) cash
			2) accounts receivable/customers' unpaid bills
			4) inventory of raw and finished goods

		And its current liabilities, such as:
			1) accounts payable
			2) debts
		""",
	},
	32: {
		'q':  """
		i) How is gross profit calculated?
		ii) How is gross profit margin calculated?
		iii) How is the markup calculated
		""",
		'a': """
		Legend:
			COGS = Cost of Goods Sold

		i) Gross profit = Revenue - COGS

		ii) Gross profit margin = Gross profit / Revenue
								= (Revenue - COGS) / Revenue

		iii) Markup = Gross profit / COGS
					= (Revenue - COGS) / COGS
		""",
	},
	33: {
		'q':  """
		Let:
			Revenue = 100
			COGS = 80

		Calculate:
			i) the gross profit
			ii) the gross profit margin
			iii) the markup
		""",
		'a': """
			i) gross profit = revenue - COGS = 100 - 80 = 20
			
			ii) gross profit margin = (revenue - COGS) / revenue
									= (100 - 80) / 100
									= 20%

			iii) markup  = (revenue - COGS) / COGS
						= (100 - 80) / 80
						= 25%
		""",
	},
	34: {
		'q':  """
		What is the federal funds rate?
		""",
		'a': """
		The term 'federal funds rate' refers to the target interest rate
		set by the Federal Reserve.

		This target is the rate at which commercial banks borrow and lend
		their excess reserves to each other overnight on an uncollateralized basis.
		""",
	},
	35: {
		'q':  """
		i)   What is impairment?
		ii)  What is depreciation?
		iii) What is the difference between depreciation and impairment?
		""",
		'a': """
		i) Impairment:
				- is a permanent reduction in the value of a company asset.
				- the asset in question may be fixed or intangible


		ii) Depreciation:
				- refers to an accounting method used to allocate the cost
				  of a tangible or physical asset over its useful life.
				- represents how much of an asset's value has been used.
        
        iii) 
            Impairment is unexpected damage to the asset while depreciation is expected wear and tear
		""",
	},
}
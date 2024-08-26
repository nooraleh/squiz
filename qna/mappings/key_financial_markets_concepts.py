# Notes taken in a QNA style from Bob Steiner's 'Key Financial Markets Concepts'

qna = { # Section 1: Time Value of Money
    1: {
		'q':  """
		Give the assumption upon which each of the following calculations
		are made?
			1) Simple interest
			2) Compound interest 
		""",
		'a': """
		Simple interest assumption:	
			There is no opportunity to re-invest the interest payments
			during the life of an investment and thereby earn extra income.

		Compound interest assumption:
			Interest amounts can be received periodically and can be re-invested
			(usually assumed to be at the same rate).
		""",
	},
    2: {
		'q':  """
		Consider the following problem:
			- an investor places £73 on deposit for 92 days
			- the interest rate payment is 8%
		
		Assume the day count convention is 365 days, what is the
		investor's total return?
		""",
		'a': """
		ANS = 73 * (1 + (0.08 * Fraction(92, 365)))
			= ans = 73 * (1 + (0.08 * 92/365))
			= 74.472
		""",
	},
    3: {
		'q':  """
		What is the 're-investment rate'?
		""",
		'a': """
		The re-investment rate is the rate at which interim interest
		cashflows from a fixed income asset can be re-invested -
		which may or may not be the same as the original investment rate. 
		""",
	},
    4: {
		'q':  """
		Which major currency-denominated deposites are associated
		with the following days in year convention?
			1) 365
			2) 360
		""",
		'a': """
			1) 365 - sterling deposit
			2) 360 - US dollar deposit
		""",
	},
    5: {
		'q':  """
		Consider the following formula which assumes:
			- compound interest (i.e with re-investment at the original interest rate)
			- interest payments made annually

		interest_accumulated_after_N_years = principal * (( 1 + interest_rate) ^N  - 1)

		Give the formula for interest accumulation for a fixed income asset which pays f
		installments per year as a Python function.
		""",
		'a': """
		Something along the lines of the following:

			def interest_accumulated(principal, n_years, rate, installments_per_year = 1):
				__base = 1 + (rate / installments_per_year)
				__exponent = installments_per_year * n_years

				return principal * (pow(__base, __exponent) - 1)
		""",
	},
    6: {
		'q':  """
		What is a nominal interest rate?
		""",
		'a': """
		A nominal interest rate is an interest rate which does not take inflation into account.

		E.g. if a lender lends $100 at 8pct for a year and inflation for that year
			was 10pct, the lender would have received a 2pct loss in real-terms purchasing power. 
		""",
	},
    7: {
		'q':  """
		a) What is an equivalent interest rate?

		b) Given your answer to (a), what is an effective interest rate?
		""",
		'a': """
		a)	An equivalent interest rate is the rate which achieves the same total proceeds
			as another given interest rate (the nominal rate), but assuming different
			frequencies of compounding.

		b) An effective interest rate is an equivalent interest rate, where the frequency
			of compounding is annual.
		""",
	},
    8: {
		'q':  """
		a) Compare money-market basis with bond basis?

		b) Give some examples of instruments where each basis is used.
		""",
		'a': """
		a)
			Money-market basis:
				Refers to the calculation of interest on the basis that there are
				exactly 360 days in each year.
				N.B: This is the market convention in the majority of money markets.

			Bond-basis:
				Refers to the calculation of interest on the basis of a 'bond' year.
				
				N.B:
					- there is more than one way of calculating a year in the bond markets
					- in general, bond basis assumes that there is exactly 365 days in each year.

		b)
		Money-market basis is used for certain long-term instruments such as:
			- floating rate notes
			- medium term CDs.

		Bond basis is used for:
			- Fixed-rate bonds
			- some money markets instruments
		""",
	},
    9: {
		'q':  """
		What is a:
			a) Rate of discount
			b) Discount factor
		""",
		'a': """
		a) A rate of discount is the interest rate which has been chosen for
			calculating a present value from a future amount.

		b) A discount factor is the number by which you need to multiply a future cashflow
			, in order to calculate its present value.
		""",
	},
    10: {
		'q':  """
		What is the 'net present value' (NPV)?
		""",
		'a': """
		The net present value is the net total of several present values (arising from
		cashflows at different future dates) added together.
		""",
	},
	11: {
		'q':  """
		What is the internal rate of return (IRR)?
		""",
		'a': """
		There are two definitions for the IRR:
			1) The IRR is the one single rate of discount which is necessary to use when
				discounting a series of future values to achieve a given net present value.

			2) The discount rate which is necessary to use when discounting a series of future
				values including an initial cashflow now, to achieve a zero net present value. 
		""",
	},
	12: {
		'q':  """
		a) What is a time deposit?
		b) State a common type of time deposit?
		""",
		'a': """
		a) A time deposit is an interest-bearing bank deposit that has a specific
			maturity date.

		b) Certificates of deposit, also savings account.
		""",
	},
	13: {
		'q':  """
		a) Define the discount rate as it refers to the US Treasury bill.

		b) Calculate the discount rate for a treasury bill given:
			- face value $100
			- 58 days of maturity
			- amount of the discount from the face value is $1.586
		""",
		'a': """
		a)
		The discount rate in the context of a T-Bill is the amount expressed
		as an annualised percentage of the face value, as opposed to an annualised
		percentage of the original amount paid.

		b)
			Given the information we have that:

				$100 * discount_rate * (days_to_maturity / us_year_convention) = $1.586

			Simple algebraic rearrangement should give: 9.8441%
		""",
	},
	14: {
		'q':  """
		Give examples of instruments quoted in:
			1) Discount rate basis
			2) Yield basis
		""",
		'a': """
		1) Example of discount rate basis:
			a) US T-Bills
			b) US Domestic trade bills or banker's acceptances
			c) US domestic commercial paper

		2) Examples of yield basis:
			a) loans
			b) deposits and CDs
			c) Eurocommercial paper
		""",
	},
	15: {
		'q':  """
		What is a discount instrument?
		""",
		'a': """
		A discount instrument is any one where the coupon is zero (assuming positive interest rates
		the market value will always be less than face value).
		""",
	},
	16: {
		'q':  """
		Explain what is meant by the value date (of a money market transaction).
		""",
		'a': """
		Also known as the settlement date, the value date of a money market transaction is the
		date on which the transaction is consummated i.e. delivery takes place.
		""",
	},
	17: {
		'q':  """
		a) What is the standard value date for most currencies in the international foreign
			exchange and money markets?

		b) Given your answer to (a) are value dates for forward settlements based on:
			1) the transaction date, or;
			2) the value date
		""",
		'a': """
		a) The standard value date (i.e spot value date) is two working days after the transaction
			date (a.k.a "T+2").

		b) Forward settlements are based on the value date (2)
		""",
	},
	18: {
		'q':  """
		Explain what is meant by dealing 'end-end'.
		""",
		'a': """
		If the spot value date is the last working day of the month,
		the forward value date will be the last working day of the corresponding
		forward month.
		""",
	},
	19: {
		'q':  """
		Explain what the 'modified following' convention is.
		""",
		'a': """
		Suppose that:
			- The spot value date is earlier than the last working day of the month.
			- The forward value date would fall on a weekend or holiday
		
		Under these circumstances, the forward value date is brought back to the nearest
		previous business day in order to stay in the same calendar month, rather than moved
		forward to the beginning of the next month. This is modified following convention.
		""",
	},
	20: {
		'q':  """
		a) What is a zero-coupon yield?

		b) What does the spot yield curve show?

		c) What is bootstrapping?
		""",
		'a': """
		a) A zero-coupon yield is the actual or theoretical yield earned on an instrument
			where there are no cashflows other than at the start and at maturity.

		b) The spot yield curve shows zero-coupon yields against time to maturity.

		c) Bootstrapping is a process of building up a theoretical spot yield curve
			by calculating zero-coupon yields for successively longer maturities derived
			from short maturities.
		""",
	},
	21: {
		'q':  """
		What is the spot yield curve also known as?
		""",
		'a': """
		The zero-coupon yield curve.
		""",
	},
	22: {
		'q':  """
		What is the key difference between the 'money-weighted rate of return (MWRR)' and
		the 'time-weighted return (TWR)'?
		""",
		'a': """
		The MWRR considers the effects of cash in- and outflows, while the TWR excludes deposits/withdrawals
		in its calculation.
		""",
	},
	23: {
		'q':  """
		How is the money-weighted rate of return calculated?
		""",
		'a': """
		The MWRR is calculated by finding the rate of return that will set the present
		values of all cash flows (in and out) equal to the value of the initial investment.
		""",
	},
	24: {
		'q':  """
		Consider the following statement:
			The time-weighted rate of return is the rate earned by a fund calculated by
			compounding the absolute returns achieved over each consecutive period.

		How are the consecutive periods marked?
		""",
		'a': """
		The consecutive periods are marked by the withdrawal of money from the fund
		or the addition of new money to it.
		""",
	},
	25: {
		'q':  """
		What is the difference between a deferred annuity and an annuity due?
		""",
		'a': """
		Deferred annuity:
			- Payments are made at the end of each period.

		Annuity due:
			- Payments are made at the beginning of each period.
		""",
	},
	26: {
		'q':  """
		What is an annuity?
		""",
		'a': """
		An annuity can be defined as either:
			1) A regular stream of future cash receipts which can be purchased by an initial cash payment
			2) A regular stream of cash payments to repay an initial borrowing
		""",
	},
	27: {
		'q':  """
		In the context of financial markets, what is the mathematical definition
		of volatility?
		""",
		'a': """
		Volatility is the standard deviation, generally annuallised (i.e n_trading_days for year)
		of the continuously compounded rate of return on an instrument.
		""",
	},
	28: {
		'q':  """
		What is value at risk (VaR)?
		""",
		'a': """
		VaR is the maximum potential loss which a bank expects to suffer on its
		positions over a given time period, estimated with a given confidence level.
		""",
	},
	29: {
		'q':  """
		Consider the following statement:
			Bank A had a VaR of $10m with a time horizon of 30 days and a confidence level of
			95%.

		Breakdown what this statement means.
		""",
		'a': """
		This means that if Bank A's position remains unchanged, there is a 95%
		probability that the total losses will not exceed $10m over the next 30 days.

		This could also be translated as:
			\"during 1 month (30 days for argument's sake) out of every 20 months (i.e 5pct of the time)
			we expect that Bank A's loss will exceed the $10m level\"
		""",
	},
	30: {
		'q':  """
		In the context of VaR, what is the 'observation period'?
		""",
		'a': """
		The observation period is the past period chosen to calculate the VaR,
		and the returns in this period are assumed to show a normal probability
		distribution.
		""",
	},
	31: {
		'q':  """
		a) In the context of FX trading, what is a pip?
		b) What does pip stand for?
		""",
		'a': """
		a) Pip:
			The smallest whole unit price move that an exchange rate can make,
			based on forex market convention.

			It equals 1/100th of 1pct , or 0.0001

		b) Either:
			1) Percentage in point
			2) Price interest point
		""",
	},
	32: {
		'q':  """
		Consider the following currency pair:
			USD/CAD

		Q: Which of the two is:
			1) the base currency?
			2) the quote (also known as 'variable') currency?
		""",
		'a': """
		The base current is the first currency stated in the pair so in this
		case the base currency is USD.

		CAD, being the second of the two, is the quote currency.
		""",
	},
	33: {
		'q':  """
		a) In the context of FX markets, what is meant by the term 'outrights'?
		b) What are outrights also known as in the context of FX markets?
		""",
		'a': """
		a) The term outrights is used to describe a type of transaction where
			two parties agree to buy or sell a given amount of currency at a predertermined
			rate at some point in the future.

		b) Forward outright, FX forward, currency forward.
		""",
	},
	34: {
		'q':  """
		As you know, the standard value date (i.e. spot value date) is two
		working days after the transaction date (T+2).

		a) Give an example of currency pair is an exception to this rule?
		b) And in what way does it differ?
		c) Why does it differ in this way?
		""",
		'a': """
		a) USD/CAD pair
		b) USD/CAD settles in one business day
		c) Because the currency pair is commonly traded and its financial
			centres are in the same time zone.
		""",
	},
	35: {
		'q':  """
		What is the difference between a 'short date forward' and
		a 'long-dated forward'?
		""",
		'a': """
		Short date forward:
			A forward contract that expires in less than or equal to one year

		Long-dated forward:
			Forward contract with a settlement date longer than one
			year and as far as 10 or more years.
		""",
	},
	36: {
		'q':  """
		What is a Spot Transaction?
		""",
		'a': """
		A spot transaction refers to an exchange of currencies at the prevailing market rate.
		""",
	},
	37: {
		'q':  """
		Fill in the blank:

			Imagine a trader decides to execute an FX transaction using Japanese Yen to
			buy New Zealand Dollars.

			This would constitute opening a _____ position in the currency pair NZD/JPY.
			
		""",
		'a': """
		BLANK: Long position

		Remember when you go long a currency pair, you are buying the base currency via
		selling the quote currency.
		""",
	},
	38: {
		'q':  """
		What is Spot Next (S/N)?
		""",
		'a': """
		A term used in foreign currency trading, it denotes the delivery of
		purchased currency on a day after the spot date (the spot date being the day
		that the funds of the foreign currency or instrument transaction are transferred - usually T+2)..

		""",
	},
	39: {
		'q':  """
		In the foreign currency markets, state three interchangeable terms for the 
		'spot rate'.
		""",
		'a': """
		1) Benchmark rate
		2) Straightforward rate
		3) Outright rate
		""",
	},
	40: {
		'q':  """
		What do we call the difference between the spot rate and the forward rate?
		""",
		'a': """
		The basis.
		""",
	},
	41: {
		'q':  """
		What is a cross currency?
		""",
		'a': """
		A cross currency refers to a currency pair or transaction that doesn't involve the US dollar.
		A cross currency transactoin, for example, doesn't use the U.S. dollar as a contract settlement
		currency.
		""",
	},
	42: {
		'q':  """
		What is meant by a high/low yield currency?
		""",
		'a': """
		A high yield currency is a currency where the home country of said currency
		has high prevailing interest rates.

		Likewise, a low yield currency is the legal tender of a country where the
		prevailing interest rates are low.
		""",
	},
	43: {
		'q':  """
		What is market depth?
		""",
		'a': """
		Market depth refers to a market's ability to absorb relatively large market orders
		without significantly impacting the price of the security.
		""",
	},
	44: {
		'q':  """
		In a "vanilla" interest rate swap (i.e adjusted-rate for fixed-rate), who is the:
			1) receiver or seller
			2) payer
		""",
		'a': """
		
		1) The receiver or seller swaps the adjustable rate payments in exchange for fixed interest payments.
		2) The payer swaps the fixed interest payments in exchange for adjustable interest rate payments.
		""",
	},
	45: {
		'q':  """
		Consider a plain vanilla interest rate swap, in which there are two parties:
			party a) the fixed-rate payer (floating-rate receiver)
			party b) the floating-rate payer (fixed-rate receiver)

		Which of (a) or (b) is considered to as having:
			1) bought the swap/having a long position
			2) sold the swap/having a short position

		""",
		'a': """
		1) party a
		2) party b		
		""",
	},
	46: {
		'q':  """
		Let:
			USD/CAD = 1.0750
			EUR/USD = 1.3400

		Infer the EUR/CAD rate
		""",
		'a': """
		EUR/CAD = (1.0750USD / CAD) * (1.3400EUR / USD)
				= (1.0750 * 1.3400) * (EUR/CAD)
				= 1.4405EUR/CAD
		""",
	},
	47: {
		'q':  """
		Consider the following currency deal quote:

			EUR 1 = CAD 1.4000 / 1.4800

		a) How many Canadian dollars would you receive for selling one euro?
		b) How many Canadian dollars would be required to buy one euro?
		""",
		'a': """
		a) 1.40
		b) 1.48
		""",
	},
	48: {
		'q':  """
		In FOREX, what is meant by transaction risk?
		""",
		'a': """
		Transaction risk refers to the currency exchange risk associated with the time delay
		between entering into a trade or contract and then settling it.
		""",
	},
	49: {
		'q':  """
		How do currency swaps differ from interest rate swaps?
		""",
		'a': """
		They can also involve principal exchanges.
		""",
	},
	50: {
		'q':  """
		Choose A or B.

		Consider a one month currency forward contract.
			A) The one month forward contract will settle one month after the spot date
			B) The one month forward contract will settle one month after the transaction date
		""",
		'a': """
			A
		""",
	},
	51: {
		'q':  """
		What is an inflation swap?
		""",
		'a': """
		An inflation swap is a derivatives contract in which:
			Party A
				Pays a fixed rate cash flow on a notional principal amount
			Party B
				Pays a floating rate linked to an inflation index, such as the CPI.
				This party pays the inflation-adjusted rate multiplied by a notional principle
				amount.
		""",
	},
	52: {
		'q':  """
		What is a bullet repayment?
		""",
		'a': """
		A bullet repayment is a lump-sum repayment of the principal at maturity.
		This contrasts with a loan structures in a way such that payment of principal is
		amortized throughout the lifetime of the loan.
		""",
	},
	53: {
		'q':  """
		What is a swap spread?
		""",
		'a': """
		A swap spread is the difference between the fixed component (swap rate) of a given
		interest rate swap and the yield of a given sovereign debt security with a given maturity.

		In the U.S the given sovereign debt security would be a U.S Treasury security.
		""",
	},
	54: {
		'q':  """
		What is the swap rate?
		""",
		'a': """
		The swap rate is the rate of the fixed leg of a swap as determined by its
		particular market and the parties involved.

		Note that it is also the fixed rate portion of a currency swap as well as
		an interest rate swap.
		""",
	},
	55: {
		'q':  """
		What is a reset date (in the context of financial derivatives such as interest rate swaps)?
		""",
		'a': """
		A reset date is the date on which the floating leg of the swap is recalculated
		based on the agreed upon reference rate.

		E.g. Consider a swap with:
			- a floating leg is set to be SOFR + 200BP
			- period 1 SOFR was 2pct so the floating leg with 2.2pct
			- at the reset date SOFR is 2.5pct so the floating leg for period 2 
				is calculated at 2.7pct and 'reset' to 2.7pct for period 2. 
		""",
	},
	56: {
		'q':  """
		a) True or false:
			The federal funds rate is directly set by the federal reserve.
		""",
		'a': """
		a) False. However, the FOMC has tools at its deposal to influence to 
			influence the federal funds rate.
		""",
	},
	57: {
		'q':  """
		a) What is the Interest on Reserve Balances (IORB)?
		b) What are Overnight Reverse Repurchases?

		c) Which of (a) or (b) is the ceiling and which is the floor
			for the target range of the federal funds rate?
		""",
		'a': """
		a) The rate of interest a bank (depository institution) gets on deposits,
		known as reserves, that it keeps at the Federal Reserve.

		b) Overnight Reverse Repurchases are securities, like treasury bills, that
			the federal reserve lends to banks, usually for a day, while paying
			interest.

		c) IORB (a) is the ceiling, the Overnight Reverse Repo (b) is the floor
		""",
	},
	58: {
		'q':  """
		Choose A or B:

		A reverse repurchase agreement is from the perspective of:
			A) The buyer of securities side that agrees to sell them back.
			B) The seller of securities side that agrees to buy them back.
		""",
		'a': """
		A)
		""",
	},
	59: {
		'q':  """
		a) Provide a generally accepted definition for 'durable goods'
		b) Given your answer to (a), what are 'core durable good'?
		""",
		'a': """
		a) Durable goods are:
			1) Consumer goods with an expected useful life of 3 or more years, and;
			2) Are purchased infrequently.

		b) Core durable goods are durables goods excluding transportation 
			equipment.
		""",
	},
	60: {
		'q':  """
		a) What are capital goods?
		b) Give a few examples of capital goods.
		""",
		'a': """
		a) Capital goods are goods that:
			- companies use to make produces that they then sell to the public
			- are not finished goods but are used to make finished goods
			
		b) Examples include:
			- machinery, vehicles, processing tools
		""",
	},
	61: {
		'q':  """
		a) What is a credit spread (AKA yield spread)?
		b) Other than 'yield spreads', state two other terms that credit spreads
			are interchangeable with.
		""",
		'a': """
		a) A credit spread (ALKA yield spread) is the differece in yield between
		two debt securities of the same maturity but different credit quality.
		b) Bond spread, default spread.
		""",
	},
	62: {
		'q':  """
		What is the difference between subordinated debt (a.k.a junior debt)
		and senior debt?
		""",
		'a': """
		They differ in priority in the event of bankruptcy or liquidation.
		Senior debt is paid first and subordinated debt is repaid only after
		senior debt is paid off.
		""",
	},
	63: {
		'q':  """
		Define 'Eurodollar Business Day'
		""",
		'a': """
		A Eurodollar Business Day is any day on which commercial banks are
		open for international business (including dealings in dollar deposits) in the
		applicable Eurodollar interbank market. 
		""",
	},
	64: {
		'q':  """
		1) In a forward rate agreement (FRA) which of the long or short is:
			a) the borrower, agreeing to pay a fixed rate and receive a floating rate
			b) the lender, agreeing to pay a floating rate and receive a fixed rate

		2)
			a) What is the FRA borrower trying to hedge against (bet for)?
			b) What is the FRA lender trying to hedge against (bet for)?
		
		""",
		'a': """
		1)
			a) the FRA long is the borrower, and agrees to pay fixed, receive floating
			b) the FRA short is the lender, and agrees to pay floating, receive fixed

		2) a) the FRA long (borrower) is hedging against an increase in interest rates
		   b) the FRA short (lender) is hedging against a decline in interest rates 
		""",
	},
	65: {
		'q':  """
		a) For which type of bonds will NEITHER the Macaulay duration NOR the modified
		duration be appropriate as a measure of interest rate sensitivity?

		b) For your answer to (a), what would be an appropriate measure to compute in order
			to ascertain the inerest rate sensitivity?

		c) Provide the formula for your answer to (a)
		""",
		'a': """
		a) Bonds with embedded options (e.g. callable and putable bonds)
		b) The effective duration would be a more appropriate measure.
		
		b) effective_duration =
			(price_change_if_yield_decreases_by_delta_y - price_change_if_yield_increases_by_delta_y) /
				(2 * initial_bond_price * delta_y) 
		""",
	},
}
# Notes taken in a QNA style from Bob Steiner's 'Key Financial Markets Concepts'

qna = { # Section 1: Time Value of Money
    1: {
		'q':  """
		Give the assumption upon which each of the following calculations
		are made?
			1) Simple interest
			2) Compount interest 
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
		A nominal interest rate is a an interest rate which does not take inflation into account.

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

		b) A discount factor the number by which you need to multiply a future cashflow
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

		b) Given your answer to (a) are value dates for forward settlements base on:
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
		
		""",
		'a': """
		
		""",
	},
	32: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	33: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	34: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	35: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	36: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	37: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	38: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	39: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	40: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	41: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	42: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	43: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	44: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	45: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	46: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	47: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	48: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	49: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	50: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	51: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	52: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	53: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	54: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	55: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	56: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	57: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	58: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	59: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	60: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	61: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	62: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	63: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	64: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	65: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	66: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	67: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	68: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	69: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	70: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	71: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	72: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	73: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	74: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	75: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	76: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	77: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	78: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	79: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	80: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	81: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	82: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	83: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	84: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	85: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	86: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	87: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	88: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	89: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	90: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	91: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	92: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	93: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	94: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	95: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	96: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	97: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	98: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	99: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	100: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	101: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    102: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    103: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    104: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    105: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    106: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    107: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    108: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    109: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    110: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	111: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	112: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	113: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	114: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	115: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	116: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	117: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	118: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	119: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	120: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	121: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	122: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	123: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	124: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	125: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	126: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	127: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	128: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	129: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	130: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	131: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	132: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	133: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	134: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	135: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	136: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	137: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	138: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	139: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	140: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	141: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	142: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	143: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	144: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	145: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	146: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	147: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	148: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	149: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	150: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	151: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	152: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	153: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	154: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	155: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	156: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	157: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	158: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	159: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	160: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	161: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	162: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	163: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	164: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	165: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	166: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	167: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	168: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	169: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	170: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	171: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	172: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	173: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	174: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	175: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	176: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	177: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	178: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	179: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	180: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	181: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	182: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	183: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	184: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	185: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	186: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	187: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	188: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	189: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	190: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	191: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	192: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	193: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	194: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	195: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	196: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	197: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	198: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	199: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	200: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
}
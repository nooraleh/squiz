# Notes taken in a Q & A style format for miscellaneous Excel information

qna = {
    1: {
		'q':  """
		i) What is meant by a fully amortized loan?
		ii) Which function in excel can we use to calculate the monthly payments required to pay off a fully amortized loan?
		""",
		'a': """
		i) A fully amortized loan is a periodic loan payment according to an amortization schedule
			that ensures the loan will be paid off by the end of the loan's set term.
			
		ii) PMT	
		""",
	},
    2: {
		'q':  """
		Which function in excel:

			i) returns the payment on the principal
			ii) returns the interest payment
			
		for a given investment based on periodic, constant payments and a constant interest rate.
		""",
		'a': """
		
		i) PPMT
		II) IPMT
		""",
	},
    3: {
		'q':  """
		Which excel functions allow you to determine the:

			i)  cumulative interest
			ii) cumulative principal

		that you've paid on a loan so far?
		""",
		'a': """
		
		i)  CUMIPMT
		ii) CUMPRINC
		""",
	},
    4: {
		'q':  """
		Which excel function allows you to determine the exact interest paid during a specific, single period?
		""",
		'a': """
		ISPMT
		""",
	},
    5: {
		'q':  """
		What do:

			i) APR
			ii) APY

		Stand for?

		iii) What is the main difference between APR and APY?
		""",
		'a': """
			i)   Annual percentage rate
			ii)  Annual percentage yield
			iii) APY takes into account compound interest, with APR does not.
		""",
	},
    6: {
		'q':  """
		Which function can we use to calculate:

			i)  Annual percentage rate (APR)
			ii) Annual percentage yield (APY)

		In excel.
		""",
		'a': """
			i)  APR -> NOMINAL
			ii) APY -> EFFECT

		""",
	},
    7: {
		'q':  """
		Consider the two formats for interest payment scheduling:

			i)  interest is paid periodically over the duration of the security
			ii) interest is paid in a lump-sum when the security matures

		Give the excel functions for calculation (i) and (i)
		""",
		'a': """
			i)  ACCRINT
			ii) ACCRINTM
		""",
	},
    8: {
		'q':  """
		Let:

			- r be the stated interest rate
			- n be the number of compounding periods (times per year interest is paid)

		State the formula for the effective interest rate/annual equivalent rate/annual percentage yield
		""",
		'a': """
		Answer: ((1 + r/n)**n)- 1
		""",
	},
    9: {
		'q':  """
		Which excel function returns the number of periods required by an investment
		to reach a specified value:

			i)  Assuming no addition payments are made
			ii) Assuming additional payments are made as you go along
		""",
		'a': """
			i) PDURATION
			ii) NPER
		""",
	},
    10: {
		'q':  """
		In the context of depreciation calculation, what is meant by 'salvage value'?
		""",
		'a': """
		Salvage value is the estimated book value of an asset after depreciation is complete,
		based on what a company expects to receive in exchange for the asset at the end of
		its useful life.
		""",
	},
	11: {
		'q':  """
		Which excel function can you use to calculate straight line deprecation?
		""",
		'a': """
		ans: SLN
		""",
	},
	12: {
		'q':  """
		Which excel function can you use to calculate the:
		
			i)   declining balance depreciation method
			ii)  double-declining balance method
			iii) sum of years deprecation method
		""",
		'a': """
		i)   DB
		ii)  DDB
		iii) SYD
		""",
	},
	13: {
		'q':  """
		Which function would you use to calculate the future value of an investment?
		""",
		'a': """
		ANS: FV
		""",
	},
	14: {
		'q':  """
		Which function would you use to calculate the future value of an investment with
		variable returns?
		""",
		'a': """
		ANS: FVSCHEDULE
		""",
	},
	15: {
		'q':  """
		What is the question that excel's PV function answers?
		""",
		'a': """
		The question: how much is a proposed investment worth in today's dollars?
		""",
	},
	16: {
		'q':  """
		What is 'net present value' (NPV)?
		""",
		'a': """
		NPV is the difference between the present value of cash inflows and the present value
		of cash outflows over a period time.
		""",
	},
	17: {
		'q':  """
		Which functions would you use to calculate:

			i)  Net present value (assuming regular cash flows)
			ii) Net present value (assuming irregular cash flows)
		""",
		'a': """
			i)  NPV
			ii) XNPV
		""",
	},
	18: {
		'q':  """
		What is the 'internal rate of return' (IRR)?
		""",
		'a': """
		The internal rate of return is the discount rate at which you would break even
		on a given investment.

		I.e the interest rate at which your investment's future cash flows have a net present
		value of 0.
		""",
	},
	19: {
		'q':  """
		Which excel functions woud you use to calculate:

			i)   the internal rate of return (IRR) for regular cash flows
			ii)  the IRR for irregular cash flows
			iii) the IRR for mixed cash flows
			iv)  the interest rate for the growth of an investment
		""",
		'a': """
			i)   IRR
			ii)  XIRR
			iii) MIRR
			iv)  RRI
		""",
	},
	20: {
		'q':  """
		Which function returns the number of days from the beginning of a coupon period until its settlement?
		""",
		'a': """
		COUPDAYDBS
		""",
	},
	21: {
		'q':  """
		i)  In the context of bonds, what is meant by the 'coupon settlement period'?
		ii) Which function in excel can you use to calculate the coupon settlement period?
		""",
		'a': """
		i)  The number of days for which you have invested but are not receiving interest.
		ii) COUPDAYS
		""",
	},
	22: {
		'q':  """
		Which function calculates:
		
			i)  the number of days
			ii) the actual date
			
		from a coupon-bearing instrument's settlement date to the next coupon date?
		""",
		'a': """
			i)  COUPDAYSNC
			ii) COUPNCD
		""",
	},
	23: {
		'q':  """
		Which functions calculate:

			i)  the number of coupons between settlement and maturity
			ii) the coupon date immediately before settlement?
		""",
		'a': """
			i)  COUPNUM
			ii) COUPPCD
		""",
	},
	24: {
		'q':  """
		Which function calculates:

			i)  the annual duration of a security (NOT using the Macaulay method)
			ii) the duration of a security (using the Macaulay method)
		""",
		'a': """
			i)  DURATION
			ii) MDURATION
		""",
	},
	25: {
		'q':  """
		i)   What is a fully invested security?

		ii)  Which excel function would you use to calculate the interest rate of a fully invested
			 security?

		iii) Which excel function would you use to calculate the value of a fully invested security
			at maturity?
		""",
		'a': """
		i) A fully invested security is a security that:
		
			- does not pay periodic interest before maturity.
			- the interest income is the difference between the redemption value of the security and the original
				investment value.

		ii)  INTRATE
		
		iii) RECEIVED
		""",
	},
	26: {
		'q':  """
		Which excel functions calculate:

			i)   the break-even price of a security that pays periodic interest
			ii)  the discount rate of a security
			iii) the price per $100 face value of a discounted security
			iv)  the price of a security that pays interest at maturity
		""",
		'a': """
			i)   PRICE
			ii)  DISC
			iii) PRICEDISC
			iv)  PRICEMAT
		""",
	},
	27: {
		'q':  """
		i) What is the bond-equivalent yield (BEY)?

		Which excel function calculates:
			ii) the bond-equivalent yield for a Treasury bill
			iii) calculate the price of a treasury bill
			iv)) calculate the yield of a treasury bill
		""",
		'a': """
		i) The BEY is essentially the annual percentage yield (APY) for fixed income securities.
			Metric used for comparing performance across fixed income securities with different maturities,
			coupon frequencies etc.

		ii)  TBILLEQ
		iii) TBILLPRICE
		iv)  TBILLYIELD
		""",
	},
	28: {
		'q':  """
		Which excel functions calculate:

			i)   the yield of a security that pays periodic interest
			ii)  the annual yield of a discounted security
			iii) the annual yield of a security that pays interest at maturity
		""",
		'a': """
			i)   YIELD
			ii)  YIELDDISC
			iii) YIELDMAT
		""",
	},
	29: {
		'q':  """
		In the context of fixed-income security, what is meant by the 'discount rate'?
		""",
		'a': """
		The discount rate determines as a percentage how much of a discount you're getting
		over the face value of the fixed-income security.
		""",
	},
}
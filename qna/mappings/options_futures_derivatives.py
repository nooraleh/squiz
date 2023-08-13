qna = {
    1: {
		'q':  """
		What is a derivatives exchange?
		""",
		'a': """
		A market where individuals and companies trade standardized contracts
		that have been defined by the exchange.
		""",
	},
    2: {
		'q':  """
		i)  What is a leverage ratio?
		ii) State a few common leverage ratios
		""",
		'a': """
		i) A leverage ratio is any of the several financial
			measurements that assesses the ability of a company to meet
			its financial obligations.

		ii) Debt-equity, equity multiplier, degree of financial leverage
			consumer leverage ratio.
		""",
	},
    3: {
		'q':  """
		In the context of financial institutions, what is systematic risk?
		""",
		'a': """
		Systematic risk is the risk that a default by one financial institution
		will create a "ripple effect" that leads to defaults by other financial
		institutions and threatens the stability of the financial system.
		""",
	},
    4: {
		'q':  """
		In the context of the OTC market, what is compression? 
		""",
		'a': """
		Compression is a procedure where two or more counterparties restructure
		transactions with each other with the result that the underlying principal
		is reduced. The net risk is the same before and after restructuring.
		""",
	},
    5: {
		'q':  """
		What is a forward contract?
		""",
		'a': """
		It is an agreement to buy or sell an asset at a certain future time
		for a certain price.
		""",
	},
    6: {
		'q':  """
		What is a spot contract?
		""",
		'a': """
		A spot contract is an agreement to buy or sell an asset almost
		immediately.
		""",
	},
    7: {
		'q':  """
		Fill in the blank:

		One of the parties to a forward contract assumes a <_____> position and 
		agrees to buy the asset on a certain specified future date for
		a certain specified price.

		The other party assumes a <____> position and agrees to sell the asset
		on the same date for the same price.
		""",
		'a': """
		1) long
		2) short
		""",
	},
    8: {
		'q':  """
		Give the generalized formula for the payoff from:

			1) a long position in a forward contract on one unit of an asset
			2) a short position in a forward contract on one unit of an asset
		""",
		'a': """
			1) S_T - K
			2) K - S_T

		Where:
			- S_T is the spot price of the asset at maturity of the contract
			- K is the delivery price
		""",
	},
    9: {
		'q':  """
		What day is the precise expiration date for monthly options?
		""",
		'a': """
		The third Friday of the expiration month.
		""",
	},
    10: {
		'q':  """
		Explain how the strike price and time to maturity affect the price/value
		of call and put options respectively.
		""",
		'a': """
		Call options:
			- as the stike price increases, the price of the option decreased
			- as time to maturity increases, the price of the option increases

		Put options:
			- as the strike price incerases, the price of the option increases
			- as time to maturity increases, the price of the option increases
		""",
	},
	11: {
		'q':  """
		Selling an option is also know as?
		""",
		'a': """
		Writing the option.
		""",
	},
	12: {
		'q':  """
		What are the three categories of traders? Breifly describe why each categories
		generally use derivatives?
		""",
		'a': """
			1) Hedgers - use derivatives to reduce the risk that they face from
				potential future movements in a market variable.
			2) Speculators - use derivatives to bet on the future direction of a market
						variable
			3) Arbitrageurs - take offsetting positions in two or more instruments to
					lock in a profit.
		""",
	},
	13: {
		'q':  """
		Consider the hedge fund strategy 'long/short equities'. What does this entail?
		""",
		'a': """
		Purchase securities considered to be undervalued and short those considered
		to be overvalued in such a way that the exposure to the overall direction
		of the market is small.
		""",
	},
	14: {
		'q':  """
		Consider the hedge fund strategy 'convertible arbitrage'. What does this entail?
		""",
		'a': """
		Taking a long position in a thought-to-be-undervalued convertible bond combined
		with an actively managed short position in the underlying equity.
		""",
	},
	15: {
		'q':  """
		Consider the hedge fund strategy 'distressed securities'. What does this entail?
		""",
		'a': """
		Buying securities issue by companies in, or close to, bankruptcy.
		""",
	},
	16: {
		'q':  """
		Consider the hedge fund strategy 'emerging markets'. What does this entail?
		""",
		'a': """
		Invest in debt and equity of companies in developing or emerging countries
		and in the debt of the countries themselves.
		""",
	},
	17: {
		'q':  """
		Consider the hedge fund strategy 'global macro'. What does this entail?
		""",
		'a': """
		Carry out trades that reflect anticipated global macroeconomic trends.
		""",
	},
	18: {
		'q':  """
		Consider the hedge fund strategy 'merger arbitrage'. What does this entail?
		""",
		'a': """
		Trade after a possible merger or acquisition is announced so that a 
		profit is made if the announced deal takes place.
		""",
	},
	19: {
		'q':  """
		Explain carefully the difference between selling a call option and buying a put option
		Express the payoff mathematically in each case.
		""",
		'a': """
		Selling a call option involves giving someone else the right to buy an asset from you. It gives
		you a payoff of:

			-max(S_{T}-K, 0) = min(K-S_{T}, 0)

		Buying a put option involves buying an option from someone else. It gives a payoff of:

			max(K-S_{T}, 0)

		In both cases, the potential payoff is (K - S_{T}).
		
		When you write a call option, the payoff is negative or zero.
		(This is because the counterparty chooses whether to exercise.)

		When you buy a put option, the payoff is zero or positive.
		(This is because you choose whether to exercise.)
		""",
	},
	20: {
		'q':  """
		What is one way of differentiating the use of futures contracts for hedging
		vs. speculation?
		""",
		'a': """
		One key difference is when the party entering into the contract is exposed to
		the price of the underlying asset.

		Examples:
			A corn farmer is exposed to price movements of corn.
			An energy corporation is exposed to the price of oil etc.
		""",
	},
	21: {
		'q':  """
		True or false:

		A futures contract is referred to by its delivery month.
		""",
		'a': """
		True
		""",
	},
	22: {
		'q':  """
		i)  How are crude oil futures prices quoted?
		ii) How are treasury bond and treasury note futures prices quoted?
		""",
		'a': """
		i)  In dollars and cents.
		ii) In dollars and thirty-seconds of a dollar.
		""",
	},
	23: {
		'q':  """
		i)   What is meant by limit down?
		ii)  What is meant by limit up?
		iii) What is meant by limit move?

		iv) What normally happens in the event of a limit move?
		""",
		'a': """
		i) Limit down:
				If in a day, the price of a futures contract moves down from the
				previous day's close by an amount equal to the daily price limit
				(as defined by the exchange).

		ii) Limit up:
				If in a day, the price of a futures contract moves up from the
				previous day's close by an amount equal to the daily price limit
				(as defined by the exchange).
				
		iii) Limit move:
				Is a move in either direction equal to the daily price limit.

		iv) Trading normally ceases for a day. However, in some instances the exchange
			has the authority to step in and change the limits.
		""",
	},
	24: {
		'q':  """
		In the context of futures contracts,
		i)  What is meant by position limits?
		ii) What are the purpose of position limits?
		""",
		'a': """
		i)  Position limits are the maximum number of contracts that a speculator may hold.
		ii) The purpose of these limits is to prevent speculators from exercising undue
			influence on the market.
		""",
	},
	25: {
		'q':  """
		Fill in the blanks:

		A trader goes long in two December gold futures contracts. The trader has to keep
		funds in what is known as a <___1__> account. The amount that must be deposited
		at the time the contract is entered into is known as the <___2____> margin.

		At the end of each trading day, the <answer to 1> account is adjusted to reflect
		the trader's gain or loss. This practice is referred to as <___3___> settlement
		or <____4___>.

		The daily flow of funds between traders to reflect gains and losses is known
		as <____5____> margin.
		""",
		'a': """

		1) margin
		2) initial
		3) daily
		4) marking to market
		5) variation
		""",
	},
	26: {
		'q':  """
		Describe the role of the clearning house in futures markets.
		""",
		'a': """
		A clearing house:
			- acts as an intermediary in futures transactions.
			- guarantees the performance of the parties to each transaction.
			- keeps track of all the transactions that take place during a day,
				so that it can calculate the net position of each of its members.
		""",
	},
	27: {
		'q':  """
		Name two ideas borrowed from the exchange-traded markets by the OTC market
		to reduce counterparty credit risk?
		""",
		'a': """
			1) Central counterparties (CCP)
			2) Bilateral clearing
		""",
	},
	28: {
		'q':  """
		i)   What does CSA stand for?
		ii)  What is a CSA?
		iii) True or false:
				A master agreement is required to trade derivatives OTC, and the CSA
				is a mandatory part of the overall agreement.
		iv) CSA's are associate with which of the following:
				1) Central counterparties (CCP)
				2) Bilateral clearing
		""",
		'a': """
		i)  Credit support annex
		ii) A credit support annex is a document that defines the terms
			for the provision of collateral by the parties in derivatives transactions.
		iii) False
		iv)  (2) Bilateral clearing
		""",
	},
	29: {
		'q':  """
		Which of the following earns interest? Why? Why not?

			1) Daily variation margin provided by a clearing house member for futures
				contracts (on an exchange).
			2) Daily variation margin provided by a member of a CCP (central counterparty)
		""",
		'a': """
			1) Does not earn interest. This is because the variation margin constitues daily
				settlement.
			2) Does earn interest. This is because the transactions in the OTC are usually not
				settled daily.
		""",
	},
	30: {
		'q':  """
		In the context of marginning, what is meant by a 'haircut'?
		""",
		'a': """
		A haircut refers to the percentage difference between an asset's market value
		and the amount that can be used as collateral for a loan.
		""",
	},
	31: {
		'q':  """
		State what each of the following quotes represent on the futures market.
			1) open
			2) high
			3) low
			4) prior settlement
			5) last trade
			6) change
			7) volume
		""",
		'a': """
			1) open - representative of the prices at which contracts were trading immediately
					after the start of trading on a day.
			2) high - the highest price in trading so far during the day
			3) low - the lowest price in trading so far during the day
			4) prior settlement - the price at which the contract traded immediately before
					the end of day's trading session.
			5) last trade - most recent price at which a trade was executed
			6) change - equal to (prior_settle_price - last_trade_price)
			7) volume - the number of contracts traded in the day
		""",
	},
	32: {
		'q':  """
		Outline the difference between 'trading volume' and 'open interest'.

		""",
		'a': """
		Trading volume represents the number of derivative contracts traded on a given day.
		Open interest represents the number of outstanding (i.e not settled) long OR
		short derivative contracts.
		""",
	},
	33: {
		'q':  """
		i) Which party - the long or the short - decides on when to deliver the underlying
		asset of a futures contract?

		ii) Which party - the long or the short - is responsible for all warehousing cost?
		""",
		'a': """
		i) The short (seller).
		ii) The long
		""",
	},
	34: {
		'q':  """
		State the two main types of traders executing futures trades, briefly outline their role.
		""",
		'a': """
		1) FCM (Futures commission merchants) - follow the instructions of their clients
			and charge a commission for doing so.

		2) Locals - individuals trading on their own account.
		""",
	},
	35: {
		'q':  """
		Briefly explain the following sub-categories of speculators:

			1) Scalpers
			2) Day traders
			3) Position traders
		""",
		'a': """

			1) Scalpers - watch for very short-term trends and attempt to profit from small
					changes in the contract price. Usually hold their position for only a few
					minutes.
			2) Day traders - hold their position for less than one trading day. They
					are unwilling to take the risk that adverse new will occur overnight.
			3) Position traders - hold their positions for much longer periods of time.
					They hope to make significant profits from major movements in the markets.
		""",
	},
	36: {
		'q':  """
		What is a 'market order'?
		""",
		'a': """
		It is a request that a trade be carried out immediately at the best price
		available in the market.
		""",
	},
	37: {
		'q':  """
		What is a 'limit order'?
		""",
		'a': """
		A limit order specifies a particular price. The order can be executed only at this
		price or at one more favourable to the trader.

		Thus, if the limit price is $30 for a trader wanting to buy, the order will be
		executed only at a price of $30 or less.
		Conversely, if the limit price is $30 for a trader wanting to sell, the order will be
		executed only at a price of $30 or more.
		""",
	},
	38: {
		'q':  """
		What is a 'stop order' or 'stop-loss order'?
		""",
		'a': """
		This order is executed at the best available price once a bid or ask is made
		at that particular price or a less favourable price.

		Essentially a market order with the condition of the specified price being hit.
		Purpose is usually to close out a position if unfavourable price movements take
		place.
		""",
	},
	39: {
		'q':  """
		What is a 'stop-limit order'?
		""",
		'a': """
		In a stop-limit, the order becomes a limit order as soon as a bid or ask is made
		at a price equal to or less favourable than the stop price.

		Two prices must be specified in a stop-limit:
			1) the stop price 2) the limit price

		If the market price gaps from being more favourable than the stop to less
		favourable than the limit, the stop-limit will not be executed.
		""",
	},
	40: {
		'q':  """
		What is a:
			i)  Day order
			ii) GTC order
		""",
		'a': """
			i) Day order - an order which expires at the end of the current market session
						in which it was placed (i.e end of trading day)

			ii) Good-'til-canceled (GTC) orders - the order is carried over to future trading sessions.
						Different trading platforms and brokerages have varying expiries for GTC
						orders.
		""",
	},
	41: {
		'q':  """
		What is a 'stop-and-limit order'?
		""",
		'a': """
		It is a stop-limit order where the stop price and the limit price are the same.
		""",
	},
	42: {
		'q':  """
		What is a 'market-if-touched' (MIT) order?
		""",
		'a': """
		Also known as a board order, an MIT becomes a market order once the specified price
		has been hit.
		""",
	},
	43: {
		'q':  """
		Contrast the design of a stop order with a market-if-touched (MIT) order.
		""",
		'a': """
		A stop order is designed to place a limit on the loss that can occur in the
		event of unfavourable price movements.
		By contrast, a market-if-touched order is designed to ensure that profits are
		taken if sufficiently favourable price movements occur.
		""",
	},
	44: {
		'q':  """
		In the context of market orders, what is slippage?
		""",
		'a': """
		Slippage is getting a difference price than expected on an order.
		Since market orders seek the best available price - this doesn't guarantee
		that the best available price is the price that you want.
		""",
	},
	45: {
		'q':  """
		What is a 'time-of-day' order?
		""",
		'a': """
		A time-of-day order specified a particular period of time during the day when the
		order can be executed.
		""",
	},
	46: {
		'q':  """
		What is a 'fill-or-kill' order?
		""",
		'a': """
		A fill-or-kill order must be executed immediately on receipt or not at all.
		""",
	},
	47: {
		'q':  """
		Consider the following pairs of statement and determine, for each pair, whether
		the statement refers to a forward contract or a futures contract.

		1.
			a) traded on an exchange
			b) private contract between two parties

		2.
			a) standardized contract
			b) non-standardized contract

		3.
			a) usually one specified delivery date 
			b) range of delivery dates

		4.
			a) settled daily
			b) settled at end of contract

		5.
			a) delivery or final cash settlement usually takes place
			b) contract is usually closed out prior to maturity

		6.
			a) virtually no credit risk
			b) some credit risk
		""",
		'a': """
		1) a) futures b) forward
		2) a) futures b) forward
		3) a) forward a) futures
		4) a) futures b) forward
		5) a) forward b) futures
		6) a) futures b) forward
		""",
	},
	48: {
		'q':  """
		a) What is a short hedge?
		b) When is a short hedge appropriate?
		""",
		'a': """
		a) A short hedge involves shorting a derivative contract (such as a futures) that
		offsets potential losses in the underlying.

		b) A short hedge is appropriate when the prospective hedger already owns
		the underlying and expects to sell it in the future - e.g. a cattle farmer who expects
		to sell cattle in bulk.

		A short hedge is also appropriate for a market participant that expects to own some asset
		in the future, will be ready for sale - e.g. an exporter who expects to receive an amount
		of foreign currency. 
		""",
	},
	49: {
		'q':  """
		When is a long hedge (going long a derivative such as a futures contract) appropriate?
		""",
		'a': """
		A long hedge is appropriate when a party knows it will have to purchase some asset in
		the future, and wants to lock in a price now.
		""",
	},
	50: {
		'q':  """
		Give the formula for `basis` in a hedging situation?
		""",
		'a': """
		Basis = spot_price_of_asset_to_be_used - futures_price_of_contract_used

		Note that if the asset to be hedged and the asset underlying the futures contract are the same, the
		basis should be zero at the expiration of the futures contract. Prior to expiration, the basis
		may be positive or negative
		""",
	},
	51: {
		'q':  """
		a) What is meant by cross hedging?
		b) Give an example of a cross hedge?
		""",
		'a': """
		a) Cross hedging refers to the practice of hedging risk using two distinct
			assets with positively correlated price movements.
			
		b) A airline company that knows it has to buy X amount of jet fuel hedges the price
			of jet fuel by enterring a long futures contract on crude oil. Since jet fuel
			and crude oil are distinct asset with positive correlation - the airline company's
			decision would be identified as a cross hedge.
		""",
	},
	52: {
		'q':  """
		What is an anticipatory hedge?
		""",
		'a': """
		An anticipatory hedge is a futures position taken in advance of
		an upcoming (anticipated) buy and sell transaction.

		Examples include:
			An American exporter that knows they will receive £1,000,000
			and wants to lock in a price will enter in 16 CME GBP/USD contracts sell £1,000,000
			for fixed USD in the same month that they receive the pound sterling.

			A copper fabricator in Jan knows it will need 300,000lbs of copper in May.
			Anticipating this, the copper manufacturer goes long 12 25,000lb CME contracts
			to lock in the price of copper.

		In summary, for anticipatory hedges a long hedge is used to cover a cost, while
		a short hedge is used to lock in a sale price.
		""",
	},
	53: {
		'q':  """
		One key factor affecting basis risk is the choice of the futures contract to be used
		for hedging. This choice has two components. State them.
		""",
		'a': """
		1) The choice of the asset underlying the futures contract.
		2) The choice of the delivery month.
		""",
	},
	54: {
		'q':  """
		True or false:
			Basis risk increases as the time difference between the hedge expiration and
			the delivery month increases.
		""",
		'a': """
		True.
		""",
	},
	55: {
		'q':  """
		What is the 'hedge ratio'?
		""",
		'a': """
		The hedge ratio is the size of the position taken in futures contracts
		to the size of the exposure.

		For example, if a copper fabricator knows it will buy 200,000lbs of copper
		in the future and goes long on 4 CME copper futures contracts (25,000lbs each),
		then the copper fabricator has fixed the purchase cost for 100,000lbs of the
		200,000lbs it will buy in the future - leading to a hedge ratio of 0.5.
		""",
	},
	56: {
		'q':  """
		What is the difference between a:
			1) static hedge
			2) dynamic hedge
		""",
		'a': """
		Static hedge:
			- when the hedging position or the number of hedging contracts isn't changed over
				the period of the hedge - regardless of the movement in the price of the hedging
				instrument

		Dynamic hedge:
			- increasing number of hedging contracts are bought and sold over the time period of
				the hedge to bring the hedge ratio towards the target hedge ratio.
		""",
	},
	57: {
		'q':  """
		a) Define 'hedge effectiveness'
		b) Consider the equation:
			
				h_* = rho * (sigma_S / sigma_F)

			where:
				- h_* is the optimal hedge ratio
				- sigma_S is the standard deviation of the changes in spot price S over duration of the hedge
				- sigma_F is the standard deviation of the changes in futures price F over duration of the hedge
				- rho is the correlation coefficient between between S and F

			Use this equation to identify the 'hedge effectiveness'
		""",
		'a': """
		a) The 'hedge effectiveness' can be defined as the proportion of the variance that is eliminated
			by hedging.

		b) pow(rho, 2) [rho squared]
		""",
	},
	58: {
		'q':  """
		What is de-hedging?
		""",
		'a': """
		De-hedging refers to the process of closing out positions that were originally
		put in place to act as a hedge in a trade or portfolio.
		""",
	},
	59: {
		'q':  """
		a) What is the federal funds rate?
		b) What is the effective federal funds rate?
		""",
		'a': """
		a) The federal funds rate is the target interest rate set by the FOMC
		at which commercial banks borrow and lend their excess reseres to each other
		overnight.

		b) The EFFR is the volume-weighted median of overnight federal funds
			transactions.
		""",
	},
	60: {
		'q':  """
		True or false:
			The federal funds rate is directly set by the federal reserve.
		""",
		'a': """
		False, it is set indirectly via an upper limit and a lower limit.

		Upper limit = Interest on Reserve Balances (IORB):
			The rate of interest a commericial bank earns on reserves kept
			at the federal reserve.

		Lower limit = Overnight reverse repurchase
			Securities, like Treasury bills, that the federal reserve
			lends to banks, usually for a day, while paying interest.
		""",
	},
	61: {
		'q':  """
		Consider the following rates:
			1) SOFR
			2) SONIA
			3) TONAR
			4) ESTR

		Pick the odd one out, and explain your choice.
		""",
		'a': """
		1) SOFR - since it is a secured rate (using the repo rate on overnight 
			transactions). The others are unsecured, and based on transactions
			between commericals banks when managing excess/deficit reserves.
		""",
	},
	62: {
		'q':  """
		True or False:

			According to Hull, for most practical purposes continuous compounding
			can be thought of as equivalent to daily compounding.
		""",
		'a': """
		True.
		""",
	},
	63: {
		'q':  """
		What is the n-year zero rate?
		""",
		'a': """
		The n-year zero rate (also 'n-year zero coupon interest rate', 'n-year spot rate', 'n-year zero')
		is the rate of interest earned on a zero-coupon bond.
		""",
	},
	64: {
		'q':  """
		How can the theoretical price of a bond be calculated?
		""",
		'a': """
		The theoretical price of a bond can be calculated as the present value of
		all the futures cashflows that the owner of the bond will receive.
		""",
	},
	65: {
		'q':  """
		True or false:
			The most accurate way of pricing a bond is to use a single discount rate
			to get the present value of the future cashflows.
		""",
		'a': """
		False, a more accurate approach is to use a different zero rate for each cash flow.
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
}

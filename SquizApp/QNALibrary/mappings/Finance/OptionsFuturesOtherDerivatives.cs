using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.Finance
{
    public partial class OptionsFuturesOtherDerivatives : QNABase
    {
        public OptionsFuturesOtherDerivatives()
        : base(title: "John Hull's Options, Futures, and Other Derivates", category: QNACategory.Finance, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "OptionsFuturesOtherDerivatives";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"What is a derivatives exchange?"},
        {"a", @"A market where individuals and companies trade standardized contracts
		that have been defined by the exchange."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"i)  What is a leverage ratio?
		ii) State a few common leverage ratios"},
        {"a", @"i) A leverage ratio is any of the several financial
			measurements that assesses the ability of a company to meet
			its financial obligations.

		ii) Debt-equity, equity multiplier, degree of financial leverage
			consumer leverage ratio."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"In the context of financial institutions, what is systematic risk?"},
        {"a", @"Systematic risk is the risk that a default by one financial institution
		will create a ""ripple effect"" that leads to defaults by other financial
		institutions and threatens the stability of the financial system."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"In the context of the OTC market, what is compression?"},
        {"a", @"Compression is a procedure where two or more counterparties restructure
		transactions with each other with the result that the underlying principal
		is reduced. The net risk is the same before and after restructuring."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"What is a forward contract?"},
        {"a", @"It is an agreement to buy or sell an asset at a certain future time
		for a certain price."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"What is a spot contract?"},
        {"a", @"A spot contract is an agreement to buy or sell an asset almost
		immediately."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"Fill in the blank:

		One of the parties to a forward contract assumes a <_____> position and 
		agrees to buy the asset on a certain specified future date for
		a certain specified price.

		The other party assumes a <____> position and agrees to sell the asset
		on the same date for the same price."},
        {"a", @"1) long
		2) short"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"Give the generalized formula for the payoff from:

			1) a long position in a forward contract on one unit of an asset
			2) a short position in a forward contract on one unit of an asset"},
        {"a", @"1) S_T - K
			2) K - S_T

		Where:
			- S_T is the spot price of the asset at maturity of the contract
			- K is the delivery price"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"What day is the precise expiration date for monthly options?"},
        {"a", @"The third Friday of the expiration month."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"Explain how the strike price and time to maturity affect the price/value
		of call and put options respectively."},
        {"a", @"Call options:
			- as the stike price increases, the price of the option decreased
			- as time to maturity increases, the price of the option increases

		Put options:
			- as the strike price incerases, the price of the option increases
			- as time to maturity increases, the price of the option increases"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"Selling an option is also know as?"},
        {"a", @"Writing the option."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"What are the three categories of traders? Breifly describe why each categories
		generally use derivatives?"},
        {"a", @"1) Hedgers - use derivatives to reduce the risk that they face from
				potential future movements in a market variable.
			2) Speculators - use derivatives to bet on the future direction of a market
						variable
			3) Arbitrageurs - take offsetting positions in two or more instruments to
					lock in a profit."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'long/short equities'. What does this entail?"},
        {"a", @"Purchase securities considered to be undervalued and short those considered
		to be overvalued in such a way that the exposure to the overall direction
		of the market is small."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'convertible arbitrage'. What does this entail?"},
        {"a", @"Taking a long position in a thought-to-be-undervalued convertible bond combined
		with an actively managed short position in the underlying equity."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'distressed securities'. What does this entail?"},
        {"a", @"Buying securities issue by companies in, or close to, bankruptcy."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'emerging markets'. What does this entail?"},
        {"a", @"Invest in debt and equity of companies in developing or emerging countries
		and in the debt of the countries themselves."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'global macro'. What does this entail?"},
        {"a", @"Carry out trades that reflect anticipated global macroeconomic trends."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"Consider the hedge fund strategy 'merger arbitrage'. What does this entail?"},
        {"a", @"Trade after a possible merger or acquisition is announced so that a 
		profit is made if the announced deal takes place."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"Explain carefully the difference between selling a call option and buying a put option
		Express the payoff mathematically in each case."},
        {"a", @"Selling a call option involves giving someone else the right to buy an asset from you. It gives
		you a payoff of:

			-max(S_{T}-K, 0) = min(K-S_{T}, 0)

		Buying a put option involves buying an option from someone else. It gives a payoff of:

			max(K-S_{T}, 0)

		In both cases, the potential payoff is (K - S_{T}).
		
		When you write a call option, the payoff is negative or zero.
		(This is because the counterparty chooses whether to exercise.)

		When you buy a put option, the payoff is zero or positive.
		(This is because you choose whether to exercise.)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"What is one way of differentiating the use of futures contracts for hedging
		vs. speculation?"},
        {"a", @"One key difference is when the party entering into the contract is exposed to
		the price of the underlying asset.

		Examples:
			A corn farmer is exposed to price movements of corn.
			An energy corporation is exposed to the price of oil etc."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"True or false:

		A futures contract is referred to by its delivery month."},
        {"a", @"True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"i)  How are crude oil futures prices quoted?
		ii) How are treasury bond and treasury note futures prices quoted?"},
        {"a", @"i)  In dollars and cents.
		ii) In dollars and thirty-seconds of a dollar."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"i)   What is meant by limit down?
		ii)  What is meant by limit up?
		iii) What is meant by limit move?

		iv) What normally happens in the event of a limit move?"},
        {"a", @"i) Limit down:
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
			has the authority to step in and change the limits."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"In the context of futures contracts,
		i)  What is meant by position limits?
		ii) What are the purpose of position limits?"},
        {"a", @"i)  Position limits are the maximum number of contracts that a speculator may hold.
		ii) The purpose of these limits is to prevent speculators from exercising undue
			influence on the market."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"Fill in the blanks:

		A trader goes long in two December gold futures contracts. The trader has to keep
		funds in what is known as a <___1__> account. The amount that must be deposited
		at the time the contract is entered into is known as the <___2____> margin.

		At the end of each trading day, the <answer to 1> account is adjusted to reflect
		the trader's gain or loss. This practice is referred to as <___3___> settlement
		or <____4___>.

		The daily flow of funds between traders to reflect gains and losses is known
		as <____5____> margin."},
        {"a", @"1) margin
		2) initial
		3) daily
		4) marking to market
		5) variation"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"Describe the role of the clearning house in futures markets."},
        {"a", @"A clearing house:
			- acts as an intermediary in futures transactions.
			- guarantees the performance of the parties to each transaction.
			- keeps track of all the transactions that take place during a day,
				so that it can calculate the net position of each of its members."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"Name two ideas borrowed from the exchange-traded markets by the OTC market
		to reduce counterparty credit risk?"},
        {"a", @"1) Central counterparties (CCP)
			2) Bilateral clearing"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"i)   What does CSA stand for?
		ii)  What is a CSA?
		iii) True or false:
				A master agreement is required to trade derivatives OTC, and the CSA
				is a mandatory part of the overall agreement.
		iv) CSA's are associate with which of the following:
				1) Central counterparties (CCP)
				2) Bilateral clearing"},
        {"a", @"i)  Credit support annex
		ii) A credit support annex is a document that defines the terms
			for the provision of collateral by the parties in derivatives transactions.
		iii) False
		iv)  (2) Bilateral clearing"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {29, new Dictionary<string, string>() {
        {"q", @"Which of the following earns interest? Why? Why not?

			1) Daily variation margin provided by a clearing house member for futures
				contracts (on an exchange).
			2) Daily variation margin provided by a member of a CCP (central counterparty)"},
        {"a", @"1) Does not earn interest. This is because the variation margin constitues daily
				settlement.
			2) Does earn interest. This is because the transactions in the OTC are usually not
				settled daily."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {30, new Dictionary<string, string>() {
        {"q", @"In the context of marginning, what is meant by a 'haircut'?"},
        {"a", @"A haircut refers to the percentage difference between an asset's market value
		and the amount that can be used as collateral for a loan."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {31, new Dictionary<string, string>() {
        {"q", @"State what each of the following quotes represent on the futures market.
			1) open
			2) high
			3) low
			4) prior settlement
			5) last trade
			6) change
			7) volume"},
        {"a", @"1) open - representative of the prices at which contracts were trading immediately
					after the start of trading on a day.
			2) high - the highest price in trading so far during the day
			3) low - the lowest price in trading so far during the day
			4) prior settlement - the price at which the contract traded immediately before
					the end of day's trading session.
			5) last trade - most recent price at which a trade was executed
			6) change - equal to (prior_settle_price - last_trade_price)
			7) volume - the number of contracts traded in the day"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {32, new Dictionary<string, string>() {
        {"q", @"Outline the difference between 'trading volume' and 'open interest'."},
        {"a", @"Trading volume represents the number of derivative contracts traded on a given day.
		Open interest represents the number of outstanding (i.e not settled) long OR
		short derivative contracts."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {33, new Dictionary<string, string>() {
        {"q", @"i) Which party - the long or the short - decides on when to deliver the underlying
		asset of a futures contract?

		ii) Which party - the long or the short - is responsible for all warehousing cost?"},
        {"a", @"i) The short (seller).
		ii) The long"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {34, new Dictionary<string, string>() {
        {"q", @"State the two main types of traders executing futures trades, briefly outline their role."},
        {"a", @"1) FCM (Futures commission merchants) - follow the instructions of their clients
			and charge a commission for doing so.

		2) Locals - individuals trading on their own account."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {35, new Dictionary<string, string>() {
        {"q", @"Briefly explain the following sub-categories of speculators:

			1) Scalpers
			2) Day traders
			3) Position traders"},
        {"a", @"1) Scalpers - watch for very short-term trends and attempt to profit from small
					changes in the contract price. Usually hold their position for only a few
					minutes.
			2) Day traders - hold their position for less than one trading day. They
					are unwilling to take the risk that adverse new will occur overnight.
			3) Position traders - hold their positions for much longer periods of time.
					They hope to make significant profits from major movements in the markets."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {36, new Dictionary<string, string>() {
        {"q", @"What is a 'market order'?"},
        {"a", @"It is a request that a trade be carried out immediately at the best price
		available in the market."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {37, new Dictionary<string, string>() {
        {"q", @"What is a 'limit order'?"},
        {"a", @"A limit order specifies a particular price. The order can be executed only at this
		price or at one more favourable to the trader.

		Thus, if the limit price is $30 for a trader wanting to buy, the order will be
		executed only at a price of $30 or less.
		Conversely, if the limit price is $30 for a trader wanting to sell, the order will be
		executed only at a price of $30 or more."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {38, new Dictionary<string, string>() {
        {"q", @"What is a 'stop order' or 'stop-loss order'?"},
        {"a", @"This order is executed at the best available price once a bid or ask is made
		at that particular price or a less favourable price.

		Essentially a market order with the condition of the specified price being hit.
		Purpose is usually to close out a position if unfavourable price movements take
		place."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {39, new Dictionary<string, string>() {
        {"q", @"What is a 'stop-limit order'?"},
        {"a", @"In a stop-limit, the order becomes a limit order as soon as a bid or ask is made
		at a price equal to or less favourable than the stop price.

		Two prices must be specified in a stop-limit:
			1) the stop price 2) the limit price

		If the market price gaps from being more favourable than the stop to less
		favourable than the limit, the stop-limit will not be executed."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {40, new Dictionary<string, string>() {
        {"q", @"What is a:
			i)  Day order
			ii) GTC order"},
        {"a", @"i) Day order - an order which expires at the end of the current market session
						in which it was placed (i.e end of trading day)

			ii) Good-'til-canceled (GTC) orders - the order is carried over to future trading sessions.
						Different trading platforms and brokerages have varying expiries for GTC
						orders."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {41, new Dictionary<string, string>() {
        {"q", @"What is a 'stop-and-limit order'?"},
        {"a", @"It is a stop-limit order where the stop price and the limit price are the same."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {42, new Dictionary<string, string>() {
        {"q", @"What is a 'market-if-touched' (MIT) order?"},
        {"a", @"Also known as a board order, an MIT becomes a market order once the specified price
		has been hit."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {43, new Dictionary<string, string>() {
        {"q", @"Contrast the design of a stop order with a market-if-touched (MIT) order."},
        {"a", @"A stop order is designed to place a limit on the loss that can occur in the
		event of unfavourable price movements.
		By contrast, a market-if-touched order is designed to ensure that profits are
		taken if sufficiently favourable price movements occur."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {44, new Dictionary<string, string>() {
        {"q", @"In the context of market orders, what is slippage?"},
        {"a", @"Slippage is getting a difference price than expected on an order.
		Since market orders seek the best available price - this doesn't guarantee
		that the best available price is the price that you want."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {45, new Dictionary<string, string>() {
        {"q", @"What is a 'time-of-day' order?"},
        {"a", @"A time-of-day order specified a particular period of time during the day when the
		order can be executed."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {46, new Dictionary<string, string>() {
        {"q", @"What is a 'fill-or-kill' order?"},
        {"a", @"A fill-or-kill order must be executed immediately on receipt or not at all."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {47, new Dictionary<string, string>() {
        {"q", @"Consider the following pairs of statement and determine, for each pair, whether
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
			b) some credit risk"},
        {"a", @"1) a) futures b) forward
		2) a) futures b) forward
		3) a) forward a) futures
		4) a) futures b) forward
		5) a) forward b) futures
		6) a) futures b) forward"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {48, new Dictionary<string, string>() {
        {"q", @"a) What is a short hedge?
		b) When is a short hedge appropriate?"},
        {"a", @"a) A short hedge involves shorting a derivative contract (such as a futures) that
		offsets potential losses in the underlying.

		b) A short hedge is appropriate when the prospective hedger already owns
		the underlying and expects to sell it in the future - e.g. a cattle farmer who expects
		to sell cattle in bulk.

		A short hedge is also appropriate for a market participant that expects to own some asset
		in the future, will be ready for sale - e.g. an exporter who expects to receive an amount
		of foreign currency."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {49, new Dictionary<string, string>() {
        {"q", @"When is a long hedge (going long a derivative such as a futures contract) appropriate?"},
        {"a", @"A long hedge is appropriate when a party knows it will have to purchase some asset in
		the future, and wants to lock in a price now."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {50, new Dictionary<string, string>() {
        {"q", @"Give the formula for `basis` in a hedging situation?"},
        {"a", @"Basis = spot_price_of_asset_to_be_used - futures_price_of_contract_used

		Note that if the asset to be hedged and the asset underlying the futures contract are the same, the
		basis should be zero at the expiration of the futures contract. Prior to expiration, the basis
		may be positive or negative"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {51, new Dictionary<string, string>() {
        {"q", @"a) What is meant by cross hedging?
		b) Give an example of a cross hedge?"},
        {"a", @"a) Cross hedging refers to the practice of hedging risk using two distinct
			assets with positively correlated price movements.
			
		b) A airline company that knows it has to buy X amount of jet fuel hedges the price
			of jet fuel by enterring a long futures contract on crude oil. Since jet fuel
			and crude oil are distinct asset with positive correlation - the airline company's
			decision would be identified as a cross hedge."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {52, new Dictionary<string, string>() {
        {"q", @"What is an anticipatory hedge?"},
        {"a", @"An anticipatory hedge is a futures position taken in advance of
		an upcoming (anticipated) buy and sell transaction.

		Examples include:
			An American exporter that knows they will receive �1,000,000
			and wants to lock in a price will enter in 16 CME GBP/USD contracts sell �1,000,000
			for fixed USD in the same month that they receive the pound sterling.

			A copper fabricator in Jan knows it will need 300,000lbs of copper in May.
			Anticipating this, the copper manufacturer goes long 12 25,000lb CME contracts
			to lock in the price of copper.

		In summary, for anticipatory hedges a long hedge is used to cover a cost, while
		a short hedge is used to lock in a sale price."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {53, new Dictionary<string, string>() {
        {"q", @"One key factor affecting basis risk is the choice of the futures contract to be used
		for hedging. This choice has two components. State them."},
        {"a", @"1) The choice of the asset underlying the futures contract.
		2) The choice of the delivery month."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {54, new Dictionary<string, string>() {
        {"q", @"True or false:
			Basis risk increases as the time difference between the hedge expiration and
			the delivery month increases."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {55, new Dictionary<string, string>() {
        {"q", @"What is the 'hedge ratio'?"},
        {"a", @"The hedge ratio is the size of the position taken in futures contracts
		to the size of the exposure.

		For example, if a copper fabricator knows it will buy 200,000lbs of copper
		in the future and goes long on 4 CME copper futures contracts (25,000lbs each),
		then the copper fabricator has fixed the purchase cost for 100,000lbs of the
		200,000lbs it will buy in the future - leading to a hedge ratio of 0.5."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {56, new Dictionary<string, string>() {
        {"q", @"What is the difference between a:
			1) static hedge
			2) dynamic hedge"},
        {"a", @"Static hedge:
			- when the hedging position or the number of hedging contracts isn't changed over
				the period of the hedge - regardless of the movement in the price of the hedging
				instrument

		Dynamic hedge:
			- increasing number of hedging contracts are bought and sold over the time period of
				the hedge to bring the hedge ratio towards the target hedge ratio."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {57, new Dictionary<string, string>() {
        {"q", @"a) Define 'hedge effectiveness'
		b) Consider the equation:
			
				h_* = rho * (sigma_S / sigma_F)

			where:
				- h_* is the optimal hedge ratio
				- sigma_S is the standard deviation of the changes in spot price S over duration of the hedge
				- sigma_F is the standard deviation of the changes in futures price F over duration of the hedge
				- rho is the correlation coefficient between between S and F

			Use this equation to identify the 'hedge effectiveness'"},
        {"a", @"a) The 'hedge effectiveness' can be defined as the proportion of the variance that is eliminated
			by hedging.

		b) pow(rho, 2) [rho squared]"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {58, new Dictionary<string, string>() {
        {"q", @"What is de-hedging?"},
        {"a", @"De-hedging refers to the process of closing out positions that were originally
		put in place to act as a hedge in a trade or portfolio."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {59, new Dictionary<string, string>() {
        {"q", @"a) What is the federal funds rate?
		b) What is the effective federal funds rate?"},
        {"a", @"a) The federal funds rate is the target interest rate set by the FOMC
		at which commercial banks borrow and lend their excess reseres to each other
		overnight.

		b) The EFFR is the volume-weighted median of overnight federal funds
			transactions."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {60, new Dictionary<string, string>() {
        {"q", @"True or false:
			The federal funds rate is directly set by the federal reserve."},
        {"a", @"False, it is set indirectly via an upper limit and a lower limit.

		Upper limit = Interest on Reserve Balances (IORB):
			The rate of interest a commericial bank earns on reserves kept
			at the federal reserve.

		Lower limit = Overnight reverse repurchase
			Securities, like Treasury bills, that the federal reserve
			lends to banks, usually for a day, while paying interest."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {61, new Dictionary<string, string>() {
        {"q", @"Consider the following rates:
			1) SOFR
			2) SONIA
			3) TONAR
			4) ESTR

		Pick the odd one out, and explain your choice."},
        {"a", @"1) SOFR - since it is a secured rate (using the repo rate on overnight 
			transactions). The others are unsecured, and based on transactions
			between commericals banks when managing excess/deficit reserves."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {62, new Dictionary<string, string>() {
        {"q", @"True or False:

			According to Hull, for most practical purposes continuous compounding
			can be thought of as equivalent to daily compounding."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {63, new Dictionary<string, string>() {
        {"q", @"What is the n-year zero rate?"},
        {"a", @"The n-year zero rate (also 'n-year zero coupon interest rate', 'n-year spot rate', 'n-year zero')
		is the rate of interest earned on a zero-coupon bond."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {64, new Dictionary<string, string>() {
        {"q", @"How can the theoretical price of a bond be calculated?"},
        {"a", @"The theoretical price of a bond can be calculated as the present value of
		all the futures cashflows that the owner of the bond will receive."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {65, new Dictionary<string, string>() {
        {"q", @"True or false:
			The most accurate way of pricing a bond is to use a single discount rate
			to get the present value of the future cashflows."},
        {"a", @"False, a more accurate approach is to use a different zero rate for each cash flow."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {66, new Dictionary<string, string>() {
        {"q", @"Consider American and European options, which option style is:
			a) More widely traded?
            b) Easier to price/analyze?"},
        {"a", @"a) American
            b) European"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {67, new Dictionary<string, string>() {
        {"q", @"True or false:
			Most index option contracts are European-style."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {68, new Dictionary<string, string>() {
        {"q", @"Describe a standard index option contract specification."},
        {"a", @"To buy (long) or sell (short) 100 times the index at a specified strike price K.
        Index options are typically cash-settled."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {69, new Dictionary<string, string>() {
        {"q", @"Which day of the month do (stock) options typically expire in?"},
        {"a", @"The third Friday of the month.
        NB: Options expiring in Fridays other than the third Friday of the month
        are known as 'weeklys'"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {70, new Dictionary<string, string>() {
        {"q", @"What is an option class?"},
        {"a", @"An option class is the set of all options across expirations and strike prices
        of the same type (either calls or puts).

        For example, the set of all IBM calls across all available expirations and strike prices
        are one class. The set of all IBM puts is another option class."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {71, new Dictionary<string, string>() {
        {"q", @"Describe what the following terms classify:
			a) Option type
            b) Option style"},
        {"a", @"a) Refers to the classification of an option as either a put or a call
        b) Refers to the classification of an option as either American-style or European-style (or Bermudan etc)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {72, new Dictionary<string, string>() {
        {"q", @"What is an option series?"},
        {"a", @"An option series consists of all the options of a given class with the same
        expiration date and the same strike price.
        
        E.g. all IBM 160 October 2021 calls would constitute an option series."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {73, new Dictionary<string, string>() {
        {"q", @"a) What are FLEX options? Explain how they work.
        b) Why do FLEX options exist?"},
        {"a", @"a) FLEX options, offered by the CBOE, allow traders to agree to nonstandard
        terms involving the strike price or expiration date as opposed to what is typically
        offered by the exchange.
        
        For instance, can involve a European option on what is normally American-style and vice versa.
        
        b) FLEX options are an attempt by option exchanges to regain business from the OTC markets."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {74, new Dictionary<string, string>() {
        {"q", @"Consider stock splits. An n-for-m stock split should cause the price of the stock
        to be reduced to what fraction of its previous value?"},
        {"a", @"m / n"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {75, new Dictionary<string, string>() {
        {"q", @"Consider a call option to buy 100 shares of a company for $30/share. 
        Suppose the company makes a 3-for-1 stock split.
        
        The terms of the option contract are changed so that the holder has the right
        to buy:
			a) how many shares?
            b) at which strike price per share?"},
        {"a", @"a) 300 shares
            b) $10/share"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {76, new Dictionary<string, string>() {
        {"q", @"Consider a put option with terms:
			a) Sell 100 shares
            b) At K = $15
            
        Suppose the company declares a 25pct stock dividend. What are the terms (a) and (b) now?"},
        {"a", @"A 25pct stock dividend is equivalent to a 5-for-4 stock split. So the new terms are:
			a) Sell (5/4)100 = 125 shares
            b) At K = $(4/5)*15 = $12 per share"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {77, new Dictionary<string, string>() {
        {"q", @"i) 	True or false:
		
			a) Long calls and short puts
			b) Short calls and long puts
			
			For position limiting purporposes, (a) is considered to be one the same
			side and (b)'s positions are considered to be one the same side.
            
        ii) Explain your answer to (i)"},
        {"a", @"i) true
        ii) (a)'s positions are bullish, while (b)'s positions are bearish"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {78, new Dictionary<string, string>() {
        {"q", @"In the context of options markets, define the following:
			a) Position limit
            b) Exercise limit"},
        {"a", @"a) A position limit for options contracts defines the maximum number of options
			contracts that an investor can hold on one side of the market.
            
        b) The exercise limit defines the maximum number of contracts that can be exercised by any
			individual in any period of five consecutive business days.
            
        NB: The position limit value usually equals the exercise limit value."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {79, new Dictionary<string, string>() {
        {"q", @"True or false:
			a) When a trader buys an option, margin is required
            b) When a trader sells an option, margin is required"},
        {"a", @"a) False as the trade does not give rise to future obligations.
			b) True as the trade gives rise to future obligations in the event
				that the option is exercised."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {80, new Dictionary<string, string>() {
        {"q", @"In the context of options, consider an option that is exercised with an OCC
        on day T.
        
        Express, in terms of T and a number of business days, how long it will take for
        the buy/sell transaction as specified in the option contract to take place?"},
        {"a", @"T+3 business days."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {81, new Dictionary<string, string>() {
        {"q", @"True or false:
			The OTC market for options is larger than the exchanged-traded equivalent."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {82, new Dictionary<string, string>() {
        {"q", @"True or false:
			a) It is never optimal to exercise an American call option on a non-dividend-paying
            	stock prior to the option's expiration.
                
			b) It is never optimal to exercise an American put option on a non-dividend-paying
            	stock prior to the option's expiration."},
        {"a", @"a) True.
        b) False - it can be optimal at times."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {83, new Dictionary<string, string>() {
        {"q", @"Let:
			- S_0 be the current stock price of an equity share
            - C be the value of an American-style call option to buy one share
            - c be the value of a European-style call option to buy one share
            
        a) Specify, in terms of the above, the upper bounds for:
			i) An American-style call option
            ii) A European-style call option
            
        b) Explain your answers to a) i) and ii)"},
        {"a", @"a)
			i) C <= S_0
            ii) c <= S_0
            
        b) Before if those upper bounds to not hold true (i.e C > S_0 or c > S_0),
        	an arbitrageur can make a riskless profit by buying the less expensive share
			and writing the call option and earn C-S_0 (or c-s_0)."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {84, new Dictionary<string, string>() {
        {"q", @"Let:
			- S_0 be the current stock price of an equity share
            - P be the value of an American-style put option to buy one share
            - p be the value of a European-style put option to buy one share
            
        a) Specify, in terms of the above, the upper bounds for:
			i) An American-style put option
            ii) A European-style put option
            
        b) Explain your answers to a) i) and ii)"},
        {"a", @"a) 
			i)  P <= K
            ii) p <= Ke^-rT
            
        b) i) The American put option value cannot be worth more than K. In other words,
				a rational market participant would not pay $120 for the right but not the obligation
                to sell at $100.
                
			ii) For European-options, at maturity the option cannot be worth more than K. Since this
				is the only time the option can be exercised, the option value cannot be worth more
				than the present value of K today."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {85, new Dictionary<string, string>() {
        {"q", @"Please specify the lower bounds on the values for the following options on a non-dividend-paying
        stock:
			a) European call
            b) European put"},
        {"a", @"a) c >= max(S_0 - Ke^-rT, 0)
		b) p >= max(Ke^-rT - S_0, 0)
        
        Where:
			- c is the value of a European-style call option
            - p is the value of a European-style put option
            - S_0 is the current stock price
            - r is the risk-free rate of interest
            - K is the strike price
            - T is the time to expiration"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {86, new Dictionary<string, string>() {
        {"q", @"a) Give the equation for put-call parity
        b) Provide of overview of the rationale for put-call parity."},
        {"a", @"a)
        Let:
			- c be the price of a European call option on underlying S
            - p be the price of a European put option on underlying S
            - K be the strike price of the put and the call options
            - r be the risk-free rate of interest
            - S_0 be the current stock price of S
            - T be the time to expiration for the options
        
        We have that:
				c + Ke^-rT = p + S_0
                
		Note that the LHS portfolio is known as a 'fiduciary call' and the RHS
        is known as a 'protective put'
                
		b) The idea is that the payoffs of LHS and RHS portfolios at expiration are the same
        	(specifically max(S_T, K)). Therefore, since they are European options,
            the value of the portfolios today must be the same and the equation holds."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {87, new Dictionary<string, string>() {
        {"q", @"True or false:
			Put-call parity only holds for American options."},
        {"a", @"Super false! Put-call parity only holds for European options."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {88, new Dictionary<string, string>() {
        {"q", @"An American call option on a non-dividend-paying stock has:
			K = 20
            T = 5/12
            C = $1.50
            S_0 = $19.00
            r = 0.1
            
		Derive the upper and lower bounds of the corresponding put option price P."},
        {"a", @"Recall that it can be shown that:
			S_0 - K <= C - P <= S_0 - Ke^-rT
            
		So you should end up with:
			1.68 <= P <= 2.5"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {89, new Dictionary<string, string>() {
        {"q", @"a) True or false:
			It is never optimal to exercise an American call option on a non-dividend-paying
            stock before the expiration date.
            
        b) Provide a formal argument backing your answer to (a)"},
        {"a", @"a) True
        b)
        It can be proven that, for a European call option on a non-dividend-paying stock we have
				c >= S_0 - Ke^-rT (proof by contradiction, if this doesn't hold we can make a riskless profit)
                
        Since embedded within the American call option are the same rights as European options and then
        some we have:
			C >= S_0 - Ke^-rT
            
        Assuming r > 0 and the fact that T > 0 we have:
			C > S_0 - K
            
        This means that C is always greater than its intrinsic value prior to maturity, and that
        exercising early would lead to a loss of (C - (S_0 - K)) > 0. This is commonly referred to
        as the extrinsic or time value."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {90, new Dictionary<string, string>() {
        {"q", @"Give an overview of the structure of a principal-protected note"},
        {"a", @"The structure of a principal-protected note (PPN) consists of:
			a) A riskless asset which matures to the initial principal paid  for the PPN.
            b) A risky asset (e.g. a call option) - the PPN invests:
				(principal-PV(principal) - fees) amount
				into the risky asset."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {91, new Dictionary<string, string>() {
        {"q", @"What are the pros and cons of investing in a principal-protected note packaged
        by a bank over buying the individual assets as a retail investor?"},
        {"a", @"Pro:
			- Banks likely to face narrower bid-ask spreads on derivatives than retail investor
            - Banks likely to earn higher rates of interest than retail investor
            
		Con:
			- Banks to charge built-in fees, retail investment would not have additional fees for
				creating a PPN portfolio."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {92, new Dictionary<string, string>() {
        {"q", @"What does a spread trading strategy involve?"},
        {"a", @"A spread trading strategy involves taking a position in two or more options
        of the same type (i.e. two or more calls or two or more puts)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {93, new Dictionary<string, string>() {
        {"q", @"Describe what the following spread trading strategies entail:
			a) Bull spread
            b) Bear spread"},
        {"a", @"a) A bull spread is one where you sell an option at a higher strike price,
			buy an option at a lower strike price - both options being of the same type
			(both calls OR both puts).
            
        b) A bear spread is one where you buy an option at a higher strike price,
			sell an option at a lower strike price - both options being of the same type
			(both calls OR both puts)."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {94, new Dictionary<string, string>() {
        {"q", @"a) What is the structure of a box spread?
        b) Given your answer to (a), outline the payoff for the box spread
        c) Given your answer to (b), deduce the value of the box spread"},
        {"a", @"a) A box spread is a combination of:
         	1) A bull call spread with strike prices K_1 and K_2
            2) A bear put spread with the same strike prices K_1 and K_2
        Where K_2 > K_1
        
        b) There are 3 possible outcomes at maturity:
			1) S_T <= K_1
            2) K_1 < S_T < K_2
            3) S_T >= K_2
            
            You should fine the all possible outcomes lead to a payoff of (K_2-K_1)
            
        c) Since all possible outcomes lead to a payoff of K_2-K_1 - the value of the box spread
			if always the present value of the payoff (K_2-K_1)e^-rT"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {95, new Dictionary<string, string>() {
        {"q", @"a) What is an alligator spread?
        b) Provide an example of a spread that can be described as an alligator spread?"},
        {"a", @"a) An alligator spread is a trading position that generates too many commissions
        to be profitable. 
        b) A box spread (which involves four options positions) can be described as an alligator."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {96, new Dictionary<string, string>() {
        {"q", @"a) True or false:
            In an options butterfly spread, the use of put options results in exactly the same
            spread as the use of call options.
                
            I.e. Let K1, K2, K3 be strike prices where:
                - K1 < k2 < K3
                - K2 - K1 = K3 - K2

            The following two structures are the same:
                Structure 1:
                    Leg 1: Long call at K1
                    Leg 2: Short 2x calls at K2
                    Leg 3: Long call at K3 

                Structure 2:
                    Structure 1:
                    Leg 1: Long put at K1
                    Leg 2: Short 2x puts at K2
                    Leg 3: Long put at K3 

        b) Prove your answer to (a) by constructing payoff tables for structures 1 and 2,
            assume all options are European."},
        {"a", @"a) True
        b) Exercise for the quizee - but the payoffs for all cases of S_T should be the same."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {97, new Dictionary<string, string>() {
        {"q", @"What is a 'combination' options trading strategy?"},
        {"a", @"A combination is an options trading strategy that involves taking a position in both calls
        and puts on the same underlying. I.e. a multi-leg strategy where legs are of different options types."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {98, new Dictionary<string, string>() {
        {"q", @"Provide the equations which enable an option to be priced when stock price movements are
        given by a one-step binomial tree."},
        {"a", @"f = e^(-r*T)*(p*f_u + (1-p)*f_d)
        
        Where p = (e^(r*T) - d) / (u - d)
        
			r = the risk-free rate of interest
            T = time to expiration of the option
            f = the options price
            d = ratio down move of the underlying from t=0 to t=T
            u = ratio up move of the underlying from t=0 to t=T
            f_u = payoff of the option price given an upmove of the underlying from S_0 to S_0*u
            f_d = payoff of the option price given a downmove of the underlying from S_0 to S_0*d
            
		NB: Parameter `p` should be interpreted as the probability of an up movement in a risk-neutral world,
			so that (1-`p`) should be interpreted as the probability of a down movement in a risk-neutral world."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {99, new Dictionary<string, string>() {
        {"q", @"Risk-neutral valuation states that, when valuing a derivative, we can make the assumption that
        investors are risk-neutral.
        
        What does it mean for an investor to be risk-neutral?"},
        {"a", @"An investor is said to be 'risk-neutral' if they do not increase the expected return they require
        from an investment to compensate for increased risk."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {100, new Dictionary<string, string>() {
        {"q", @"A risk-neutral world has two features that simplify the pricing of derivatives.
        State them."},
        {"a", @"1) The expected return on a stock (or any other underlying asset) is the risk-free rate.
        2) The discount rate used for the expected payoff on an option (or any other derivative instrument) is the risk-free
			rate."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {101, new Dictionary<string, string>() {
        {"q", @"Consider the following equations for the terminal value of an option in a one-step binomial tree:
        
			p*f_u + (1-p)*f_d                        (1)
            
		where:
			p = (e^(r*T) - d) / (u - d)              (2)
            
		
        And consider the following statement:
			`p` should be interpreted as the probability of an up-movement in a risk-neutral world
            while (1-`p`) should be interpreted as the probability of a down movement in a risk-neutral world.
            
        Prove the validity of this statement."},
        {"a", @"In a risk-neutral world, we assume that the expected return of a stock (or any underlying asset)
        should be the risk-free rate.
        
        In a one-step binomial tree, let:
			- p be the probability of an up-move
            - S_0*u be the value of the stock at time T given an up-move
            - S_0*d be the value of the stock at time T given a down-move
            
		The expected value of terminal time T would be
        
			E(S_T) = p*S_0*u + (1-p)*S_0*d
				   = (p*S_0)*(u-d) + S_0*d
                   
		Substituting p = (e^rT-d) / (u-d)
        
				   = S_0*((e^rT-d) / (u-d))*(u-d) + S_0*d
                   = S_0*e^rT - S_0*d + S_0*d
                   = S_0*e^rT
                   
		Implying that the price of the underlying grows at the risk-free rate given the interpretation
        of `p`, which is in line with the risk-neutral world assume. The statement is therefore valid."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {102, new Dictionary<string, string>() {
        {"q", @"What is the key difference between Binomial tree option pricing when is comes to
        the style of the option (i.e. American or European)?"},
        {"a", @"For American options, the value of the option at nodes earlier than the terminal node
        is the greater of:
			(1) The value given by equation:
				f = e^(-r*dt)*[p*f_u + (1-p)*f_d] and;
			(2) The payoff from early exercise:
					I.e. (S_t - K) for a call or (K - S_t) for a put"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {103, new Dictionary<string, string>() {
        {"q", @"In the context of option pricing, what is 'delta'? How may we interpret 'delta'?"},
        {"a", @"The delta of a stock option is:
			- The ratio of the change in the price of the stock (asset) option to the change in the
				price of the underlying stock (asset)
			- It is the number of units of stock we should hold for each stock option shorted to create
	  			a riskless portfolio."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {104, new Dictionary<string, string>() {
        {"q", @"True or false:
			The volatility of a stock (or any other asset), sigma, is defined so that the
            standard deviation of its return in a short period of time dt is sigma*sqrt(dt)"},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {105, new Dictionary<string, string>() {
        {"q", @"True or false:
			When the binomial tree is used to price a European option, the price converges
            to the Black-Scholes-Merton price as the numbre of time steps is increased."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {106, new Dictionary<string, string>() {
        {"q", @"a) Give a non-rigorous description of what a stochastic process is?"},
        {"a", @"a) Any variable whose value changes over time in an uncertain way is said to follow a stochastic process."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}

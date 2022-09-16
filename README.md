# simpleTradingAlgorithm

using alpaca and alphavantage, I created a simple algorithm which buys when the price is less than sqrt(high*low) where high and low are the high price and low price from yesterday. The algorithm then sells when the price goes above 1/2 + this value.

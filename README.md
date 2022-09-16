# simpleTradingAlgorithm

using alpaca and alphavantage, I created a simple algorithm which buys when the price is less than sqrt(high*low) where high and low are the high price and low price from yesterday. The algorithm then sells when the price goes above 1/2 + this value.

To use this script create a secrets.json file with your alpaca KEY, SECRET_KEY, BASE_URL and an alpha vantage key. Both alpaca and alpha vantage let you create an account for free. 

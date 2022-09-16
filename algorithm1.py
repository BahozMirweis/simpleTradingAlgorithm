import datetime
import math
import requests
import alpaca_trade_api
import time
import json

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

API_BASE_URL = secrets['API_BASE_URL']
API_KEY = secrets['API_KEY']
API_SECRET_KEY = secrets['API_SECRET_KEY']
API_ALPHA_VANTAGE_KEY = secrets["ALPHA_VANTAGE_KEY"]

alpaca = alpaca_trade_api.REST(API_KEY, API_SECRET_KEY, API_BASE_URL)

r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_ALPHA_VANTAGE_KEY}')

yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).date().__str__()
yesterdayPrice = r.json()['Time Series (Daily)'][yesterday]

high = yesterdayPrice['2. high']
low = yesterdayPrice['3. low']
tradeAt = math.sqrt(float(high) * float(low))
buy = True

while(True):
    r = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={API_ALPHA_VANTAGE_KEY}')
    price = float(r.json()['Global Quote']['05. price'])

    if price < tradeAt and buy:
        alpaca.submit_order('IBM', 10)
        buy = False
    elif price >= tradeAt + 1/2 and not buy:
        alpaca.submit_order('IBM', 10, 'sell')

    time.sleep(60)
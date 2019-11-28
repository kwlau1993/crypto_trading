#!/usr/bin/python
import requests
import csv
import pandas as pd
import json
# add what coins you want to fetch data for
coin_list = [ "BTC" ]
# , "ETH", "BCH", "EOS", "LTC", "XLM", "XRP", "NEO", "BNB", "NCASH", "TRAC", "DASH", "XEM", "XRM"]

#add what markets you want the coins to be correlated with
#market_list = [ "USD" ]
i = "USD"
#add whatever data u would like to download, check API documentation
time = [ "histominute" ]
#Add exchanges
exchange_list = ["Kraken", "Bitfinex", "Bitstamp", "Coinbase" ]

for j in time:
    for e in exchange_list:
        for c in coin_list: 
            rcomp = requests.get('https://min-api.cryptocompare.com/data/' + j + '?fsym='+ c +'&tsym=' + i + '&limit=1400' +'&e=' + e).json()
            response = rcomp['Data']
            crypto_data = pd.DataFrame(response)
            #care about the directory
            crypto_data.to_csv(c +'-'+ i + '_' + j + '_' + e + '.csv')

from googlefinance import getQuotes
import json
from decimal import Decimal,getcontext
import os
import csv

confFile = os.path.expanduser('~/github/portfoliotracker/stocks.txt')

#config.read(confFile)

def getQuote(stockTicker):
    stackInfo = json.dumps(getQuotes(stockTicker), indent=2)
    stockInfo = json.loads(stackInfo)
    closePrice = stockInfo[0]['LastTradePrice']
    getcontext().prec = 3
    close = Decimal(closePrice)
    return close

value = 0

with open(confFile, 'rb') as csvfile:
    stockReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for ticker,quantity in stockReader:
        stockVal = getQuote(ticker)
        getcontext().prec = 10
        value += stockVal * Decimal(quantity)
        print "ticker: "+ticker+" quantity: "+quantity + " stockValue: ",stockVal

print "value of stock portfolio is:", value
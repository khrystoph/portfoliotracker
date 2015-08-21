from googlefinance import getQuotes
import json
from decimal import Decimal

stackInfo = json.dumps(getQuotes('AMZN'), indent=2)
stockInfo = json.loads(stackInfo)
closePrice = stockInfo[0]['LastTradePrice']
close = Decimal(closePrice)
numShares = 125
shares = Decimal(numShares)
stockVal = close * shares
print stockVal
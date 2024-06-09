from ib_insync import *


ib = IB()
ib.connect('127.0.0.1', 7497, clientId=14)


contract = Crypto('BTC','PAXOS','USD')


bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='10 D',
        barSizeSetting='5 mins',
        whatToShow='MIDPOINT',
        useRTH=True,
        formatDate=1)

df = util.df(bars)
print(df)
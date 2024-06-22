import datetime 
import time
from ib_insync import *
import pandas as pd
import pandas_ta as ta

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=14)

tickers = ['BTC',"ETH"]
exchange='PAXOS'
currency='USD'


contract_objects={}
for tick in tickers:
    print(Crypto(tick,exchange,currency))
    contract_objects[tick]=ib.qualifyContracts(Crypto(tick,exchange,currency))[0]
print(contract_objects)

def get_historical_data(ticker_contract):
    bars = ib.reqHistoricalData(
    ticker_contract, endDateTime='', durationStr='10 D',
    barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True,formatDate=2)
    # convert to pandas dataframe:
    df = util.df(bars)
    # print(df)
    df['sma1']=ta.sma(df.close,20)
    df['sma2']=ta.sma(df.close,50)
    
    return df


def main_strategy_code():

    print("inside main strategy")
    pos=ib.reqPositions()
    if len(pos)==0:
        pos_df=pd.DataFrame([])
    else:
        pos_df=util.df(pos)
        pos_df['name']=[cont.symbol for cont in pos_df['contract']]
        pos_df=pos_df[pos_df['position']>0]
    print(pos_df)
    ord=ib.reqAllOpenOrders()
    if len(ord)==0:
        ord_df=pd.DataFrame([])
    else:
        ord_df=util.df(ord)
        ord_df['name']=[cont.symbol for cont in ord_df['contract']]
    print(ord_df)

    for ticker in tickers:
        print('ticker name is',ticker,'################')
        ticker_contract=contract_objects[ticker]
        hist_df=get_historical_data(ticker_contract)
        print(hist_df)
        print(hist_df.close.iloc[-1])
        capital=int(float([v for v in ib.accountValues() if v.tag == 'AvailableFunds' ][0].value))
        print(capital)
        quantity=int((capital/10)/hist_df.close.iloc[-1])  
        print(quantity)


current_time=datetime.datetime.now()
print(current_time)

print(datetime.datetime.now())
#start time
start_hour,start_min=19,0
#end time
end_hour,end_min=19,50
start_time=datetime.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=datetime.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)
print(start_time)
print(end_time)

candle_size=60

while datetime.datetime.now()<end_time:
    now = datetime.datetime.now()
    print(now)
    seconds_until_next_minute = candle_size - now.second+1
    print(seconds_until_next_minute)
    # Sleep until the end of the current minute
    time.sleep(seconds_until_next_minute)

    # Run your function
    main_strategy_code()
import datetime 
import time
from ib_insync import *


ib = IB()
ib.connect('127.0.0.1', 7497, clientId=14)

def main_strategy_code():
    print('we are inside')

    contract =Crypto('BTC','PAXOS','USD')

    bars = ib.reqHistoricalData(
            contract,
            endDateTime='',
            durationStr='10 D',
            barSizeSetting='1 min',
            whatToShow='MIDPOINT',
            useRTH=True,
            formatDate=2)
    print(bars)
    df = util.df(bars)
    print(df)

current_time=datetime.datetime.now()
print(current_time)

print(datetime.datetime.now())
#start time
start_hour,start_min=19,0
#end time
end_hour,end_min=19,9
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
#%%
import os
import pandas as pd
from trading_calendars import get_calendar

raw_minute_dir = '../csv/raw_minute/'
files = os.listdir(raw_minute_dir)

def get_trading_days(start_date, end_date, country_code):
    if country_code == 'KRX':
        all_trading_days = list(get_calendar('XKRX').all_sessions)
        needed_trading_days = [date for date in all_trading_days if str(date)[:10] >= start_date and str(date)[:10] <= end_date]

    elif country_code == 'US':
        all_trading_days = list(get_calendar('NYSE').all_sessions)
        needed_trading_days = [date for date in all_trading_days if str(date)[:10] >= start_date and str(date)[:10] <= end_date]
    else:
        return print('KRX와 US market만 지원합니다. 둘 중 하나를 입력해주세요')
    return needed_trading_days



for file in files:
    df = pd.read_csv(raw_minute_dir + file, index_col=0)
    df = df[::-1]
    # index 전환
    start_date = list(df.DATE)[0]
    end_date = list(df.DATE)[-1]

    index = get_trading_days(start_date, end_date, 'US')

    df.index = index

    # 거꾸로 돌려주기
    df = df.drop(columns = ['SYMBOL_CODE', 'DATE', 'TIME'])

    df.columns = ['open', 'high', 'low', 'close', 'volume']

    df['dividend'] = 0
    df['ratio'] = 1

    df.to_csv('../csv/minute/' + file)


# %%

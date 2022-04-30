from zipline import run_algorithm
import pandas as pd
import pandas_datareader.data as web
from zipline.api import symbol, order, record

from zipline.api import order_target, record, symbol
import matplotlib.pyplot as plt

class test_run(object):
    def __init__(self):
        pass

    def run(self):
        def initialize(context):
            pass

        def handle_data(context, data):
            order(symbol('AAPL'), 10)
            record(AAPL=data[symbol('AAPL')].price)

        def analyze(context, perf):
            perf.to_csv('../csv/out.csv')

        def run():
            start = pd.Timestamp('2018')
            end = pd.Timestamp('2021')

            sp500 = web.DataReader('SP500', 'fred', start, end).SP500
            benchmark_returns = sp500.pct_change()

            result = run_algorithm(start=start.tz_localize('UTC'),
                                end=end.tz_localize('UTC'),
                                initialize=initialize,
                                handle_data=handle_data,
                                analyze=analyze,
                                capital_base=100000,
                                benchmark_returns=benchmark_returns,
                                bundle='usa_daily_bundle',
                                data_frequency='daily')

if __name__ == '__main__':
    test_run().run()
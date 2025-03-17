import backtrader as bt
import pandas as pd
import yfinance as yf
import backtrader.feeds as btfeeds
from datetime import datetime  # Import the datetime module
from pandas_practice_changingData import CSVProcessor as CSVP

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    
# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        if self.dataclose[0] < self.dataclose[-1]:
            # current close less than previous close

            if self.dataclose[-1] < self.dataclose[-2]:
                # previous close less than the previous close

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.buy()

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    # Datas are in the smae folder
    datapath = 'TSLA.csv'
    # Create a Data Feed
   # Add the data feed from the CSV file
    data = btfeeds.GenericCSVData(
    dataname=datapath,  # Use the datapath variable for consistency
    datetime=0,        # Date is in the 1st column (index 0)
    open=4,            # Open is in the 5th column (index 4)
    high=2,            # High is in the 3rd column (index 2)
    low=3,             # Low is in the 4th column (index 3)
    close=1,           # Close is in the 2nd column (index 1)
    volume=5,          # Volume is in the 6th column (index 5)
    openinterest=-1,   # Open Interest is not present, set to -1
    header=0,          # Header is in the first row (index 0) - Corrected from header=1
    dtformat='%Y-%m-%d', # Date format is Year-Month-Day
    reverse=False      # Data is in chronological order (oldest first)
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()
    cerebro.plot()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
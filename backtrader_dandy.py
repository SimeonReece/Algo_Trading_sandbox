import backtrader as bt
import pandas as pd
import yfinance as yf
import backtrader.feeds as btfeeds
from datetime import datetime  # Import the datetime module

tsla_df = yf.download(tickers='TSLA')
# Save the DataFrame to a CSV file
tsla_df.to_csv('TSLA.csv')
# print("TSLA data saved to TSLA.csv")

# trimming spaces or on open in librecalcl just trim spaces else use this code
## df = pd.read_csv('TSLA.csv', skiprows=3)  # Skip the header rows
## df['Date'] = df['Date'].str.strip()  # Remove leading/trailing spaces
## df.to_csv('TSLA_cleaned.csv', index=False)

#explicitly skipping in pandas
## df = pd.read_csv('TSLA.csv', skiprows=3)
## df['Ticker'] = df['Ticker'].str.strip()  # Replace 'Date' with 'Ticker'
## df.to_csv('TSLA_cleaned.csv', index=False)

#setting stratery
class MyStrategy(bt.Strategy):
    def next(self):
        # Your strategy logic here
        pass

cerebro = bt.Cerebro()

# Add the data feed from the CSV file
data = btfeeds.GenericCSVData(
    dataname='TSLA.csv',
    fromdate=datetime(2010, 6, 29), # Optional: Specify start date
    todate=datetime(2025, 3, 7),   # Optional: Specify end date
    datetime=0,
    open=4,      # Open is in the 5th column (index 4)
    high=2,      # High is in the 3rd column (index 2)
    low=3,       # Low is in the 4th column (index 3)
    close=1,     # Close is in the 2nd column (index 1)
    volume=5,    # Volume is in the 6th column (index 5)
    openinterest=-1,
    header=1,  # Add this line to skip the header row 
    dtformat='%Y-%m-%d'  # Add this line to specify the date format
)

cerebro.adddata(data)
cerebro.addstrategy(MyStrategy)
cerebro.run() 
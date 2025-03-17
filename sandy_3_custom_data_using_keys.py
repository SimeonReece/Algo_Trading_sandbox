import yfinance as yf
import pandas as pd

dhr = yf.Ticker('dhr')
info = dhr.info

# Print each key on its own line for better readability
for key in info.keys():
    print(key)

# # from there you can make your own data like open,daylow,day high 

#print(info['open'])
#print(info['dayLow'])
#print(info['dayHigh'])

# combining ticker with list comprehension 
dhr.get_financials() 
pnl = dhr.financials
bs = dhr.balancesheet
cf = dhr.cashflow
fs = pd.concat([pnl, bs, cf])
tickers=['META','AMZN','NFLX','GOOG']
tickers = [yf.Ticker(ticker) for ticker in tickers]
tickers 
dfs = []
for ticker in tickers:
    # get financial statements for each
    pnl = ticker.financials
    bs = ticker.balancesheet
    cf = ticker.cashflow

    # concat into one dataframe
    fs = pd.concat([pnl, bs, cf])

    # make dataframe format nicer
    data = fs.T  # Swap dates and columns
    data = data.reset_index()  # reset index (data) into a column
    data.columns = ['Date', *data.columns[1:]]  # Rename old index to Date
    data['Ticker'] = ticker.ticker  # Add ticker to dataframe
    dfs.append(data)
#print(data)

# Assuming 'dfs' is a list of DataFrames
for df in dfs:
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique(): 
        cols[cols[cols == dup].index.values.tolist()] = [dup + '.' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
    df.columns = cols

df = pd.concat(dfs, ignore_index=True)
df = df.set_index(['Ticker', 'Date'])
print(df)

aapl = yf.Ticker('aapl')
options = aapl.option_chain()

# from there putsm call, expirey by chaning data
calls= options.calls
puts=options.puts

# getting instituisl holder
aapl.institutional_holders
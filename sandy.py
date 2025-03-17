import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


import yfinance as yf

msft = yf.Ticker('msft')
stockinfo = msft.info # you can look at security, and other type of assest instead of stocks



# we dont want all the dat for now
# for key, value in stockinfo.items():
#     print(key, ":", value)

    # from there you can return the information using a nytax like this  
# numshares = msft.info['sharesOutstanding']
# print(numshares)

#print(msft.recommendations)
#print(msft.splits)


# resample and plotting 
#df = msft.dividends
#data = df.resample('Y').sum()
#data = data.reset_index()
#data['Year'] = data['Date'].dt.year
#plt.figure()
#plt.bar(data['Year'], data['Dividends'])
#plt.ylabel('Dividend Yield ($)')
#plt.xlabel('Year')
#plt.show()

df = msft.history(period='max')
#you can dhange time frames look them up 
plt.figure()
plt.plot(df['Close'])
# you can do open, high, or close

plt.show()
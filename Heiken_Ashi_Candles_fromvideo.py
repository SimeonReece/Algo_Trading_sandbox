# clearimport numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_ta as ta

data = yf.download(tickers='^RUI', start='2012-03-11', end='2022-07-10')
data.drop(['Volume'], axis=1, inplace=True)
data.head(10)
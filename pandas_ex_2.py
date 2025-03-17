import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

tickers = tickers.Symbol.to_list()

print(tickers)

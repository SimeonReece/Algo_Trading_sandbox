import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

tickers = pd.read_html('https://trends.google.com/trends/explore?q=nvidia%20stock&date=now%201-d&geo=US&hl=en')[0]

tickers = tickers.Symbol.to_list()

print(tickers)

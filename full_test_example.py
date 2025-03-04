from tradingview_ta import TA_Handler, Interval, Exchange
import yfinance as yf

from ta.momentum import RSIIndicator


symbol_data = TA_Handler(
    symbol="AAPL",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)

analysis = symbol_data.get_analysis()

print(analysis.indicators)

rsi = analysis.indicators['RSI']
if rsi < 30:
    print("Buy Signal")
elif rsi > 70:
    print("Sell Signal")
else:
    print("Hold")



data = yf.download("AAPL", start="2022-01-01", end="2023-01-01")

data['RSI'] = RSIIndicator(data['Close']).rsi()
buy_signals = data[data['RSI'] < 30]
sell_signals = data[data['RSI'] > 70]



with open("strategy_results.txt", "w") as file:
    file.write(str(results))

import yfinance as yf
from datetime import datetime
from tradingview_ta import TA_Handler, Interval, Exchange

# Define the ticker symbol for Google
ticker_symbol = "GOOG"

# Get today's date and set the start of the month as the beginning date
today = datetime.today().date()
start_of_month = today.replace(day=1)

# Download the stock data
google_data = yf.download(ticker_symbol, start=start_of_month, end=today)

# Print the data
print(google_data)



tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
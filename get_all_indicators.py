from tradingview_ta import TA_Handler, Interval, Exchange

# Example configuration
symbol = "AAPL"
exchange = "NASDAQ"

analysis = TA_Handler(
    symbol=symbol,
    exchange=exchange,
    screener="america",  # Screener region
    interval=Interval.INTERVAL_1_DAY,  # Interval of analysis
)

# Retrieve analysis data
analysis_result = analysis.get_analysis()
print("Indicators:", *analysis_result.indicators.keys() ,sep="\n" )  # Lists indicators used in the analysis on it own line



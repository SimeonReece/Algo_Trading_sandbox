import yfinance as yf
aapl = yf.Ticker("AAPL")

# balance sheet and dividends : remember this is a panda dataframe
# print(aapl.quarterly_balancesheet)
# print(aapl.dividends)
balance_sheet_df = aapl.quarterly_balancesheet  # Corrected from balance_sheet to balancesheet
balance_sheet_df.to_excel("Apple_data.xlsx")
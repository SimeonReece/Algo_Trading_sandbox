import pandas as pd

def calculate_heikin_ashi(data):
    """
    Calculates Heikin-Ashi candles from a Pandas DataFrame.

    Args:
        data: Pandas DataFrame with 'Open', 'High', 'Low', 'Close' columns.

    Returns:
        Pandas DataFrame with Heikin-Ashi 'HA_Open', 'HA_High', 'HA_Low', 'HA_Close' columns.
    """
    ha_data = pd.DataFrame()

    ha_close = (data['Open'] + data['High'] + data['Low'] + data['Close']) / 4  # Corrected line
    ha_open = (data['Open'].shift(1) + data['Close'].shift(1)) / 2
    ha_open.iloc[0] = (data['Open'].iloc[0] + data['Close'].iloc[0]) / 2  # First HA open is the same as the first regular candle's midpoint.
    ha_high = data[['High', ha_open, ha_close]].max(axis=1)
    ha_low = data[['Low', ha_open, ha_close]].min(axis=1)

    ha_data['HA_Open'] = ha_open
    ha_data['HA_High'] = ha_high
    ha_data['HA_Low'] = ha_low
    ha_data['HA_Close'] = ha_close

    return ha_data

# Example usage
dataname = 'TSLA.csv'  # Define dataname first

# Read CSV, skipping the header row
df = pd.read_csv(dataname, skiprows=1, decimal=',')

# Explicitly select the columns
df = df[['Open', 'High', 'Low', 'Close']]

print(df.columns)

#ha_df = calculate_heikin_ashi(df)

# print(ha_df)
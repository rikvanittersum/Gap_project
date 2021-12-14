from pandas_datareader import data as pdr
import yfinance as yf
from candle_checks import *
import numpy as np
import datetime
yf.pdr_override()

start = "2021-10-10"
end = "2021-10-25"
stock = "INTC"

def get_df_gaps(stock, start, end):
    df_history = pdr.get_data_yahoo(stock, start=start, end=end)
    df = pdr.get_data_yahoo(stock, start=start, end=end)
    df['Gap'] = candeles_overlap(df)

    df['Gap_up'] = gap_up(df['High'], df['High'].shift(1))
    df['Gap_size'] = np.where(df['Gap_up'] == True, size_gap_up(df['Low'], df['High'].shift(1), df['Adj Close'].shift(1)), size_gap_down(df['High'], df['Low'].shift(1), df['Adj Close'].shift(1)))
    df['Low_day_before'] = df['Low'].shift(1)

    df = df.query("Gap == True")

    df.drop(['Volume', 'Open', 'Close', 'Adj Close', 'Gap'], 1, inplace=True)
    df.reset_index(inplace=True)
    df_history.reset_index(inplace=True)
    return [df_history, df]

dfs = get_df_gaps(stock, start, end)
df_historical = dfs[0]
df_gaps = dfs[1]

print(df_historical)






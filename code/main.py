from pandas_datareader import data as pdr
import yfinance as yf
from candle_checks import *
import numpy as np
from gap_checkers import *

yf.pdr_override()

start = "2022-01-10"
end = "2022-01-29"
stock = "INTC"

def get_df_gaps(stock, start, end):
    df_history = pdr.get_data_yahoo(stock, start=start, end=end)
    df = pdr.get_data_yahoo(stock, start=start, end=end)
    df['Gap'] = candeles_overlap(df)

    df['Gap_up'] = gap_up(df['High'], df['High'].shift(1))
    df['Gap_size'] = np.where(df['Gap_up'] is True, size_gap_up(df['Low'], df['High'].shift(1), df['Adj Close'].shift(1)), size_gap_down(df['High'], df['Low'].shift(1), df['Adj Close'].shift(1)))
    df['Low_day_before'] = df['Low'].shift(1)

    df = df.query("Gap == True")

    df.drop(columns=['Volume', 'Open', 'Close', 'Adj Close', 'Gap'])
    df.reset_index(inplace=True)
    df_history.reset_index(inplace=True)
    return [df_history, df]

dfs = get_df_gaps(stock, start, end)
df_historical = dfs[0]
df_gaps = dfs[1]

gap_up_checkers = []
gap_down_checkers = []
#print(df_gaps)

for index, gap  in df_gaps.iterrows():
    print(gap)
    if gap["Gap_up"]:
        gap_up_checkers.append(gap_up_checker(df_historical, gap["High"], gap["Date"]).price_day_before_gap_is_reached())
    else:
        gap_down_checkers.append(gap_down_checker(df_historical, gap["Low_day_before"], gap["Date"]).price_day_before_gap_is_reached())


print(gap_up_checkers)
print(gap_down_checkers)







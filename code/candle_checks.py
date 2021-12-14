from pandas_datareader import data as pdr
def high_in_candle_day_before(high, high_db, low_db):
    return (high < high_db) & (high > low_db)

def low_in_candle_day_before(low, high_db, low_db):
    return (low < high_db) & (low > low_db)

def candeles_overlap(df):
    return ~(high_in_candle_day_before(df['High'], df['High'].shift(1), df['Low'].shift(1)) + low_in_candle_day_before(df['Low'], df['High'].shift(1), df['Low'].shift(1)) + high_in_candle_day_before(df['High'].shift(1), df['High'], df['Low']) + low_in_candle_day_before(df['Low'].shift(1), df['High'], df['Low']))

def gap_up(high, high_db):
    return high > high_db

def size_gap_up(low, high_db, close_db):
    return (low - high_db) / close_db * 100

def size_gap_down(high, low_db, close_db):
    return (low_db - high)  / close_db * 100




import datetime
import pandas as pd

class gaps_checker():
    def __init__(self, history_df, low_price, date):
        self.history = history_df
        self.date = date
        self.low_price_gap = low_price

    def trim_df(self):
        self.history = self.history[self.history['Date'] > datetime.datetime(self.date)]

    def check_if_gap_is_filled(self, date):
        self.trim_df()
        return self.price_before_gap_is_reached()

    def price_day_before_gap_is_reached(self):
        return not (self.history[['Low', 'High']] < self.low_price_gap).any().empty





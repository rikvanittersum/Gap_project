import datetime

class gap_down_checker():
    def __init__(self, history_df, price, date):
        self.history = history_df
        self.date = date
        self.price_gap = price

    def trim_df(self):
        self.history = self.history[self.history['Date'] > datetime.datetime(self.date)]

    def check_if_gap_is_filled(self, date):
        self.trim_df()
        return self.price_before_gap_is_reached()

    def price_day_before_gap_is_reached(self):
        return ((self.history['High'] >= self.price_gap) & (self.history['Low'] >= self.price_gap)).any()

class gap_up_checker(gap_down_checker):
    def __init__(self, history_df, price, date):
        super().__init__(history_df, price, date)

    def price_day_before_gap_is_reached(self):
        return ((self.history['High'] <= self.price_gap) & (self.history['Low'] <= self.price_gap)).any()



import datetime

class gap_down_checker():
    def __init__(self, history_df, price, date):
        self.history = history_df
        self.date = date
        self.price_gap = price

    def price_day_before_gap_is_reached(self):
        return ((self.history['High'] >= self.price_gap) & (self.history['Low'] >= self.price_gap)).any()

class gap_up_checker(gap_down_checker):
    def __init__(self, history_df, price, date):
        super().__init__(history_df, price, date)

    def price_day_before_gap_is_reached(self):
        return ((self.history['High'] <= self.price_gap) & (self.history['Low'] <= self.price_gap) & (self.history['Date'] <= self.price_gap)).any()





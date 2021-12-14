class stats():
    def __init__(self, stock, history_df):
        self.stock = stock
        self.gaps = 0
        self.filled = 0
        self.not_filled = 0

    def filled_gap(self):
        gaps = self.gaps + 1
        filled = self.filled + 1

    def not_filled_gap(self):
        gaps = self.gaps + 1
        not_filled = self.not_filled + 1

    def percentage_filled(self):
        return self.filled / self.gaps
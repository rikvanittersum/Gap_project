import unittest
import pandas as pd
import numpy as np

from gaps_checker import *


def create_df(date, data):
    dates = pd.date_range(date, periods=len(data), freq="D")

    df = pd.DataFrame(data, index=dates, columns=['High', 'Low'])
    df.index.name = 'Date'
    df.reset_index(inplace=True)

    print(df.head())
    return df

class MyTestCase(unittest.TestCase):
    def test_price_before_gap_is_reached(self):
        df = create_df("2020-10-08", [[1,2],[4,5]])
        gc = gaps_checker(df, 3, "2020-10-08")
        self.assertTrue(gc.price_before_gap_is_reached())

if __name__ == '__main__':
    unittest.main()

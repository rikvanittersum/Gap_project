import unittest
import pandas as pd
import numpy as np

from gap_checkers import *


def create_df(date, data):
    dates = pd.date_range(date, periods=len(data), freq="D")

    df = pd.DataFrame(data, index=dates, columns=['Low', 'High'])
    df.index.name = 'Date'
    df.reset_index(inplace=True)

    return df

class MyTestCase(unittest.TestCase):
    def test_when_price_before_gap_down_is_reached_should_return_true(self):
        df = create_df("2020-10-08", [[4,5],[1,2]])
        gc = gap_down_checker(df, 3, "2020-10-08")
        self.assertTrue(gc.price_day_before_gap_is_reached())

    def test_when_price_before_gap_down_is_not_reached_should_return_false(self):
        df = create_df("2020-10-08", [[4,5],[1,2]])
        gc = gap_down_checker(df, 10, "2020-10-08")
        self.assertFalse(gc.price_day_before_gap_is_reached())

    def test_when_price_before_gap_up_is_reached_should_return_true(self):
        df = create_df("2020-10-08", [[4,5],[2,3]])
        gc = gap_up_checker(df, 3, "2020-10-08")
        self.assertTrue(gc.price_day_before_gap_is_reached())

    def test_when_price_before_gap_up_is_not_reached_should_return_false(self):
        df = create_df("2020-10-08", [[4,5],[2,3]])
        gc = gap_up_checker(df, 1, "2020-10-08")
        self.assertFalse(gc.price_day_before_gap_is_reached())

if __name__ == '__main__':
    unittest.main()

import unittest
from candle_checks import *
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_high_in_candle_day_before(self):
        high = 5
        high_db = 10
        low_db = 1

        in_candle_db = high_in_candle_day_before(high, high_db, low_db)

        self.assertTrue(in_candle_db)

    def test_high_not_in_candle_day_before(self):
        high = 15
        high_db = 10
        low_db = 1

        in_candle_db = high_in_candle_day_before(high, high_db, low_db)

        self.assertFalse(in_candle_db)

    def test_low_in_candle_day_before(self):
        low = 5
        high_db = 10
        low_db = 1

        in_candle_db = high_in_candle_day_before(low, high_db, low_db)

        self.assertTrue(in_candle_db)

    def test_low_not_in_candle_day_before(self):
        low = 15
        high_db = 10
        low_db = 1

        in_candle_db = high_in_candle_day_before(low, high_db, low_db)

        self.assertFalse(in_candle_db)

    def test_gap_up(self):
        d = {'High': [1, 10], 'Low': [0, 9]}
        df = pd.DataFrame(data=d)
        e = [[True], [True]]
        expected = pd.DataFrame(data=e)

        df = candeles_overlap(df)

        pd.testing.assert_series_equal(df, expected.iloc[:, 0], check_names=False)

    def test_direction_gap(self):
        high = 10
        high_db = 1
        higher_db = 11

        self.assertTrue(gap_up(high, high_db))
        self.assertFalse(gap_up(high, higher_db))



if __name__ == '__main__':
    unittest.main()

import sys
import pandas as pd
import numpy as np
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from funksjoner import introduser_NaN

class test_introduserNaN(unittest.TestCase):
    def test_positiv(self):
        df=pd.DataFrame({'Data': [1,2,3,4,5]})
        df_NaN=introduser_NaN(df, kolonne='Data', frac=0.4)
        self.assertEqual(df_NaN['A'].isna().sum,2)
    def test_invalid_frac(self):
        df = pd.DataFrame({"A": [1, 2, 3]})
        with self.assertRaises(ValueError):
            introduser_NaN(df, kolonne="A", frac=1.5)

    def test_invalid_df(self):
        with self.assertRaises(TypeError):
            introduser_NaN([1, 2, 3], kolonne="A", frac=0.1)

    def test_missing_column(self):
        df = pd.DataFrame({"A": [1, 2, 3]})
        with self.assertRaises(ValueError):
            introduser_NaN(df, kolonne="B", frac=0.1)

if __name__ == "__main__":
    unittest.main()
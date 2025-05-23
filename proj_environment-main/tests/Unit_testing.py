import sys
import pandas as pd
import numpy as np
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from funksjoner import introduser_NaN

class test_introduserNaN(unittest.TestCase):

    def setUp(self):
        self.df=pd.DataFrame({'Data':[1,2,3,4,5]})

    def test_positiv(self):
        df_NaN=introduser_NaN(self.df, column='Data', frac=0.4)
        self.assertEqual(df_NaN['Data'].isna().sum(),2)

    def test_invalid_frac(self):
        with self.assertRaises(ValueError):
            introduser_NaN(self.df, column="Data", frac=1.5)

    def test_invalid_df(self):
        with self.assertRaises(TypeError):
            introduser_NaN([1, 2, 3], column="Data", frac=0.1)

    def test_missing_column(self):
        with self.assertRaises(ValueError):
            introduser_NaN(self.df, column="B", frac=0.1)

from funksjoner import introduser_uteliggere
class test_introduserUteliggere(unittest.TestCase):

    def setUp(self):
        self.df=pd.DataFrame({'Data':[1,2,3,4,5]})

    def test_positiv(self):
        df_uteliggere=introduser_uteliggere(self.df,column='Data',frac=0.4)
        count=(df_uteliggere['Data']==570).sum()
        self.assertEqual(count,2)
    
    def test_zerofrac(self):
        df_zerofrac=introduser_uteliggere(self.df,column='Data',frac=0.0)
        self.assertTrue((df_zerofrac['Data'] != 570).all())
    
    def test_invalid_frac_high(self):
        with self.assertRaises(ValueError):
            introduser_uteliggere(self.df, column='Data', frac=1.2)
    
    def test_invalid_frac_low(self):
        with self.assertRaises(ValueError):
            introduser_uteliggere(self.df, column='Data', frac=-0.1)
    
    def test_invalid_dataframe(self):
        with self.assertRaises(TypeError):
            introduser_uteliggere([1, 2, 3], frac=0.2)

    def test_missing_column(self):
        df = pd.DataFrame({'Data': [1, 2, 3]})
        with self.assertRaises(ValueError):
            introduser_uteliggere(df, column='Database')
    
    def test_column_unchanged_elsewhere(self):
        result = introduser_uteliggere(self.df, 'Data',frac=0.4)
        unchanged = result[result['Data'] != 570]
        self.assertTrue((unchanged['Data'] < 100).all())

from funksjoner import håndter_mangler

class TestHåndterMangler(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'Data': [1.0, np.nan, 3.0, np.nan, 5.0]})

    def test_median_fill(self):
        result = håndter_mangler(self.df, column='Data', method="median")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 3.0)

    def test_mean_fill_default(self):
        result = håndter_mangler(self.df, column='Data', method="unknown")
        self.assertFalse(result['Data'].isna().any())
        expected_mean = np.nanmean([1.0, 3.0, 5.0])
        self.assertAlmostEqual(result['Data'][1], expected_mean)

    def test_ffill(self):
        result = håndter_mangler(self.df, column='Data', method="ffill")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 1.0)

    def test_bfill(self):
        result = håndter_mangler(self.df, column='Data', method="bfill")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 3.0)

    def test_interpolation_polynomial(self):
        result = håndter_mangler(self.df, column='Data', method="interpolate", degree=2)
        self.assertFalse(result['Data'].isna().any())
        # Just check that interpolation filled values and didn’t alter existing
        self.assertEqual(result['Data'][0], 1.0)
        self.assertEqual(result['Data'][2], 3.0)
        self.assertEqual(result['Data'][4], 5.0)

    def test_invalid_column(self):
        with self.assertRaises(ValueError):
            håndter_mangler(self.df, column="B", method="mean")

    def test_invalid_interpolation(self):
        bad_df = pd.DataFrame({'Data': ['Data', "b", np.nan, "c"]})
        with self.assertRaises(RuntimeError):
            håndter_mangler(bad_df, column='Data', method="interpolate")

if __name__ == "__main__":
    unittest.main()
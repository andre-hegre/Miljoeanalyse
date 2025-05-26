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

    def test_positiv(self): #Tester positiv tilfelle at alt kjører bra
        df_NaN=introduser_NaN(self.df, column='Data', frac=0.4)
        self.assertEqual(df_NaN['Data'].isna().sum(),2)

    def test_invalid_frac(self): #Tester med ugyldig frac
        with self.assertRaises(ValueError):
            introduser_NaN(self.df, column="Data", frac=1.5)

    def test_invalid_df(self): #Tester med ugyldig dataframe
        with self.assertRaises(TypeError):
            introduser_NaN([1, 2, 3], column="Data", frac=0.1)

    def test_missing_column(self): #Tester med manglende kolonne
        with self.assertRaises(ValueError):
            introduser_NaN(self.df, column="B", frac=0.1)

from funksjoner import introduser_uteliggere
class test_introduserUteliggere(unittest.TestCase):

    def setUp(self):
        self.df=pd.DataFrame({'Data':[1,2,3,4,5]})

    def test_positiv(self): #Positiv test, sjekker at sum av antall uteliggere er 2
        df_uteliggere=introduser_uteliggere(self.df,column='Data',frac=0.4)
        count=(df_uteliggere['Data']==570).sum()
        self.assertEqual(count,2)
    
    def test_zerofrac(self): #Tester med frac=0
        df_zerofrac=introduser_uteliggere(self.df,column='Data',frac=0.0)
        self.assertTrue((df_zerofrac['Data'] != 570).all())
    
    def test_invalid_frac_high(self): #Tester med for høy frac
        with self.assertRaises(ValueError):
            introduser_uteliggere(self.df, column='Data', frac=1.2)
    
    def test_invalid_frac_low(self): #Tester med for lav frac
        with self.assertRaises(ValueError):
            introduser_uteliggere(self.df, column='Data', frac=-0.1)
    
    def test_invalid_dataframe(self): #Tester med ugyldig dataframe
        with self.assertRaises(TypeError):
            introduser_uteliggere([1, 2, 3], frac=0.2)

    def test_missing_column(self): #Tester med manglende kolonne
        df = pd.DataFrame({'Data': [1, 2, 3]})
        with self.assertRaises(ValueError):
            introduser_uteliggere(df, column='Database')
    
    def test_column_unchanged_elsewhere(self): #Tester at andre deler av kolonnen er uendret
        result = introduser_uteliggere(self.df, 'Data',frac=0.4)
        unchanged = result[result['Data'] != 570]
        self.assertTrue((unchanged['Data'] < 100).all())

from funksjoner import håndter_mangler

class TestHåndterMangler(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'Data': [1.0, np.nan, 3.0, np.nan, 5.0]})

    def test_median_fill(self): #Tester median metode
        result = håndter_mangler(self.df, column='Data', method="median")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 3.0)

    def test_mean_fill_default(self): #Tester mean fill som er default
        result = håndter_mangler(self.df, column='Data', method="unknown")
        self.assertFalse(result['Data'].isna().any())
        expected_mean = np.nanmean([1.0, 3.0, 5.0])
        self.assertAlmostEqual(result['Data'][1], expected_mean)

    def test_ffill(self): #Tester ffill metode
        result = håndter_mangler(self.df, column='Data', method="ffill")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 1.0)

    def test_bfill(self): #Tester bfill metode
        result = håndter_mangler(self.df, column='Data', method="bfill")
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][1], 3.0)

    def test_interpolation_polynomial(self): #tester interpolation metode
        result = håndter_mangler(self.df, column='Data', method="interpolate", degree=2)
        self.assertFalse(result['Data'].isna().any())
        self.assertEqual(result['Data'][0], 1.0)
        self.assertEqual(result['Data'][2], 3.0)
        self.assertEqual(result['Data'][4], 5.0)

    def test_invalid_column(self): #Tester ugyldig kolonne
        with self.assertRaises(ValueError):
            håndter_mangler(self.df, column="B", method="mean")

    def test_invalid_interpolation(self): #Tester ugyldig interpolering
        bad_df = pd.DataFrame({'Data': ['Data', "b", np.nan, "c"]})
        with self.assertRaises(RuntimeError):
            håndter_mangler(bad_df, column='Data', method="interpolate")

from funksjoner import håndter_uteliggere

class TestHåndterUteliggere(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "temperature": [-100, -40, 20, 50, 120]})

    def test_outliers_replaced_with_nan(self): #Omgjøre uteliggere med NaN
        result = håndter_uteliggere(self.df, column="temperature", lower=-50, upper=100)
        self.assertTrue(np.isnan(result["temperature"].iloc[0]))  # -100 blir NaN
        self.assertTrue(np.isnan(result["temperature"].iloc[4]))  # 120 blir NaN
        self.assertEqual(result["temperature"].isna().sum(), 2)

    def test_no_outliers(self): #Tester der det ikke er uteliggere, bør forbli det samme
        df_no_outliers = pd.DataFrame({"temperature": [0, 10, 20]})
        result = håndter_uteliggere(df_no_outliers, column="temperature")
        pd.testing.assert_frame_equal(result, df_no_outliers.astype(float))

    def test_invalid_upper_lower_boundaries(self): #Tester ugyldig grenser
        with self.assertRaises(TypeError):
            håndter_uteliggere(self.df, column="temperature", lower=100, upper=50)

    def test_invalid_dataframe_input(self): #tester ugyldig dataframe
        with self.assertRaises(TypeError):
            håndter_uteliggere([1, 2, 3], column="temperature")

    def test_missing_column(self): #Tester manglende kolonne
        with self.assertRaises(ValueError):
            håndter_uteliggere(self.df, column="humidity")

    def test_data_copying(self): #Tester at originale dataframe ikke forandres
        original = self.df.copy()
        _ = håndter_uteliggere(self.df, column="temperature", lower=-50, upper=100)
        pd.testing.assert_frame_equal(self.df, original)

from funksjoner import beregn_statistikk

class TestBeregningStatistikk(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "value": [1, 2, 3, 4, 5]
        })

    def test_korrekt_statistikk(self): #Tester at statistikken er korrekt
        stat = beregn_statistikk(self.df, kolonne="value")
        self.assertEqual(stat["gjennomsnitt"], 3.0)
        self.assertEqual(stat["median"], 3.0)
        self.assertAlmostEqual(stat["standardavvik"], np.std([1, 2, 3, 4, 5], ddof=1))

    def test_kolonne_ikke_funnet(self): #Tester at kolonne ikke finnes
        with self.assertRaises(ValueError):
            beregn_statistikk(self.df, kolonne="ukjent")

    def test_tom_kolonne(self): # Tester tom kolonne
        df_tom = pd.DataFrame({"value": []})
        stat = beregn_statistikk(df_tom, kolonne="value")
        self.assertTrue(np.isnan(stat["gjennomsnitt"]))
        self.assertTrue(np.isnan(stat["median"]))
        self.assertTrue(np.isnan(stat["standardavvik"]))

    def test_nan_verdier(self): # Tester håndtering av NaN-verdier
        df_nan = pd.DataFrame({"value": [1, np.nan, 3, np.nan, 5]})
        stat = beregn_statistikk(df_nan, kolonne="value")
        self.assertAlmostEqual(stat["gjennomsnitt"], np.nanmean([1, 3, 5]))
        self.assertAlmostEqual(stat["median"], np.nanmedian([1, 3, 5]))
        self.assertAlmostEqual(stat["standardavvik"], np.nanstd([1, 3, 5], ddof=1))

if __name__ == "__main__":
    unittest.main()



    if __name__ == "__main__":
        unittest.main()
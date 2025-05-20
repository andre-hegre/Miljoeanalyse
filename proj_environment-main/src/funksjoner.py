import pandas as pd
import numpy as np


# introduserer uregelmessigheter (NaN til omtrent 6% av verdiene i valgt kolonne)
def introduser_NaN(df , kolonne="mean(relative_humidity P1D)" , frac=0.06):

    df=df.copy()
    df.loc[df.sample(frac=frac).index, kolonne] = np.nan 
    return df

# introduserer enkelte tallverdier på 570, som ikke gir mening (uteliggere)
def introduser_uteliggere(df , kolonne="mean(air_temperature P1D)" , frac=0.04):
    df=df.copy()
    df.loc[df.sample(frac=frac).index, kolonne] = 570
    return df



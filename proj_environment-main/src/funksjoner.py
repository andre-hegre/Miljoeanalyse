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

def håndter_mangler(df,column,method,degree=1):
    df=df.copy()
    if method=='median':
        df[column]=df[column].fillna(df[column].median())
    elif method == 'interpolate':
        df[column] = df[column].interpolate(method='polynomial',order=degree)
    elif method == 'ffill':
        df[column] = df[column].fillna(method='ffill')
    elif method == 'bfill':
        df[column] = df[column].fillna(method='bfill')
    else: 
        df[column] = df[column].fillna(df[column].mean())
    return df


def håndter_uteliggere(df,column,upper=100,lower=-50):
    df=df.copy()
    
    df[column]=np.where((df[column]<lower) | (df[column]>upper),np.nan,df[column])
    return df

import pandas as pd
import numpy as np


# introduserer uregelmessigheter (NaN til omtrent 6% av verdiene i valgt kolonne)
def introduser_NaN(df , column, frac=0.06):
    df=df.copy()
    if frac>1 or frac<0:
        raise ValueError("Frac must be a value between 0 and 1")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df input must be pandas dataframe")
    if column not in df.columns:
        raise ValueError(f"Column {column} not found in df Dataframe")
    df.loc[df.sample(frac=frac).index, column] = np.nan 
    return df

# introduserer enkelte tallverdier på 570, som ikke gir mening (uteliggere)
def introduser_uteliggere(df , column, frac=0.04):
    df=df.copy()
    if frac>1 or frac<0:
        raise ValueError("Frac must be a value between 0 and 1")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df input must be pandas dataframe")
    if column not in df.columns:
        raise ValueError(f"Column {column} not found in df Dataframe")
    df.loc[df.sample(frac=frac).index, column] = 570
    return df

def håndter_mangler(df,column,method,degree=1):
    df=df.copy()
    if column not in df:
        raise ValueError(f"Column {column} not found in df Dataframe")
    try: 

        if method=='median':
            df[column]=df[column].fillna(df[column].median())
        elif method == 'interpolate':
            if not np.issubdtype(df[column].dropna().dtype, np.number):
                raise TypeError("Dataframe must consist of numeric data, not text or other data")
            df[column] = df[column].interpolate(method='polynomial',order=degree)
        elif method == 'ffill':
            df[column] = df[column].fillna(method='ffill')
        elif method == 'bfill':
            df[column] = df[column].fillna(method='bfill')
        else: 
            df[column] = df[column].fillna(df[column].mean())
    except Exception as e:
        raise RuntimeError(f"Unable to handle missing values with method {method}: {e}")
    return df


def håndter_uteliggere(df,column,upper=100,lower=-50):
    df=df.copy()
    if upper<=lower:
        raise TypeError("Upper boundary not be equal to or lower than lower boundary")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df input must be pandas dataframe")
    if column not in df:
        raise ValueError(f"Column {column} not found in df Dataframe")
    
    df[column]=np.where((df[column]<lower) | (df[column]>upper),np.nan,df[column])
    return df

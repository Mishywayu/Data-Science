import pandas as pd

filepath = 'nairobi_property_prices_large.csv'

def wrangle(filepath):
    df = pd.read_csv(filepath)
    return df

print(wrangle(filepath))
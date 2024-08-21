import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
})

# Identify missing values
# print(df.isna())

# Drop rows with missing data
df_dropped = df.dropna()
# print(df)

# Fill missing values with a specific value
df_filled = df.fillna(0)
# print(df)

# Forward fill missing values
df_ffill = df.fillna(method='ffill')


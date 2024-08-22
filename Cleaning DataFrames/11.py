import pandas as pd

# Sample DataFrame for pivoting
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02'],
    'Variable': ['A', 'B', 'A'],
    'Value': [100, 200, 150]
})

# Pivot the DataFrame
df_pivoted = df.pivot(index='Date', columns='Variable', values='Value')

# Melting the DataFrame back to long format
df_melted = pd.melt(df_pivoted.reset_index(), id_vars=['Date'], value_vars=['A', 'B'])

import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value1': [10, 20, 30]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Value2': [100, 200, 400]
})

# Merge DataFrames on 'ID'
df_merged = pd.merge(df1, df2, on='ID', how='inner')

# Join DataFrames
df_joined = df1.set_index('ID').join(df2.set_index('ID'))

# Concatenate DataFrames
df_concat = pd.concat([df1, df2], axis=0)

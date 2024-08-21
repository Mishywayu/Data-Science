import pandas as pd

#Sample DataFrame with duplicates
df = pd.DataFrame({
    'A': [1, 2, 2, 4],
    'B': [5, 6, 6, 8],
    'C': [9, 10, 10, 12]
})

# Identify duplicates
print(df.duplicated())

# Drop duplicates
df_no_duplicates = df.drop_duplicates()


import pandas as pd

# Apply a function to each element in a column
df['Value'] = df['Value'].apply(lambda x: x * 2)

# Apply a function to each element in the entire DataFrame
df = df.applymap(lambda x: x + 1 if isinstance(x, (int, float)) else x)

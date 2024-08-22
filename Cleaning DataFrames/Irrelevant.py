import pandas as pd

# Drop a column
df = df.drop(columns=['IrrelevantColumn'])

# Filter rows where 'Value' is greater than 20
df_filtered = df[df['Value'] > 20]

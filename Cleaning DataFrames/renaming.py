import pandas as pd

# Rename specific columns
df = df.rename(columns={'A': 'Column1', 'B': 'Column2'})

# Rename all columns
df.columns = ['NewCol1', 'NewCol2', 'NewCol3']
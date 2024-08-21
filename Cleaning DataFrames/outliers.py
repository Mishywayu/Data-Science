import pandas as pd
import numpy as np

# Z-score method to identify outliers
df['Z'] = (df['A'] - df['A'].mean()) / df['A'].std()
df_outliers = df[np.abs(df['Z']) > 3]

# Remove outliers
df_no_outliers = df[np.abs(df['Z']) <= 3]

import pandas as pd

# Sample DataFrame for grouping
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Value': [10, 20, 30, 40]
})

# Group by 'Category' and sum the 'Value'
df_grouped = df.groupby('Category')['Value'].sum()

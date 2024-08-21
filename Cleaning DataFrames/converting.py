import pandas as pd

# Sample DataFrame with mixed data types
df = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['5.1', '6.2', '7.3', '8.4'],
    'C': ['True', 'False', 'True', 'False']
})

# Convert strings to integers
df['A'] = df['A'].astype(int)

# Convert strings to floats
df['B'] = df['B'].astype(float)

# Convert strings to boolean
df['C'] = df['C'].astype(bool)

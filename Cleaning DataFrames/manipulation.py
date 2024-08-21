import pandas as pd

# Sample DataFrame with strings
df = pd.DataFrame({
    'Name': [' Alice ', ' Bob', 'Charlie ', '  David']
})

# Strip whitespace
df['Name'] = df['Name'].str.strip()

# Replace substrings
df['Name'] = df['Name'].str.replace('i', 'I')

# Convert to uppercase
df['Name'] = df['Name'].str.upper()

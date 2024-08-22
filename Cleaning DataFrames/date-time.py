import pandas as pd

# Sample DataFrame with date strings
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-02-01', '2021-03-01'],
    'Value': [100, 200, 300]
})

# Convert strings to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Set date as index
df.set_index('Date', inplace=True)

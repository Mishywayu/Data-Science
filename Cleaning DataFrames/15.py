import pandas as pd

# Read a large CSV file in chunks
chunks = pd.read_csv('large_data.csv', chunksize=1000)
for chunk in chunks:
    # Process each chunk
    process(chunk)

# Optimize data types
df['Category'] = df['Category'].astype('category')

# An index in a pandas DataFrame is a label or set of labels used to identify rows.
# It acts like a primary key in a database table, ensuring that each row is uniquely identifiable.

# The index can be a simple integer sequence (default), 
# a specific column, or 
# a multi-level index (MultiIndex).


# Default Index
# When a DataFrame is created, pandas automatically assigns a default integer index starting from 0.
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Setting a Custom Index
df = df.set_index('Name')

# Resetting the Index
df = df.reset_index()

# Dropping the Index Column
# df = df.set_index('Name').reset_index(drop=True)

# Accessing Rows by Index
# You can use .loc[] to access rows by their index label.
df = df.set_index('Name')
# print(df.loc['Alice'])


# Slicing DataFrames
# DataFrames can be sliced by indices using: 
# .loc[] for label-based indexing or 
# .iloc[] for position-based indexing.

# Label-based indexing
# print(df.loc['Alice':'Bob'])

# Position-based indexing
# print(df.iloc[0:2])



# Creating a MultiIndex


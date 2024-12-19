# Pandas is a powerful and popular Python library used for data manipulation and analysis,
#  particularly with tabular data.

# The two primary data structures in pandas are:
# 1. Series (one-dimensional labeled array)
# 2. DataFrame (two-dimensional labeled data structure with columns of potentially different types).

# Here is a simple example of creating a DataFrame:
import pandas as pd

data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT
#     Name  Age  Score
# 0    Tom   20     90
# 1   Nick   21     85
# 2   John   19     88




# Reading Data:
# Pandas provides various functions to read data from different file formats such as 
# CSV, Excel, JSON, etc. 

# Here's an example of reading a CSV file:
import pandas as pd
df = pd.read_csv('books.csv')
print(df.head())  # prints the first 5 rows of the DataFrame




# Exploratory Data Analysis (EDA):
# Pandas provides various functions for exploratory data analysis such as 
# describe(), info(), head(), tail(), etc.

# Here's an example of using describe():
import pandas as pd

df = pd.read_csv('books.csv')
print(df.describe())




# Data Types:
# Pandas provides various data types such as int64, float64, object, 
# datetime64, etc. 

# Here's an example of checking the data types of a DataFrame:
import pandas as pd

df = pd.read_csv('books.csv')
print(df.dtypes)




# Column Operations:
# Pandas provides various functions for column operations such as rename(), drop(), 
# insert(), etc.

# Here's an example of renaming a column:
import pandas as pd

df = pd.read_csv('books.csv')
df = df.rename(columns={'Author': 'Author_Name'})
print(df.head())




# String Operations:
# Pandas provides various functions for string operations such as 
# str.contains(), str.findall(), etc. 

# Here's an example of using str.contains():
import pandas as pd

df = pd.read_csv('books.csv')
print(df['Title'].str.contains('Python'))




# Missing Values:
# Pandas provides various functions for handling missing values such as 
# isnull(), notnull(), fillna(), etc.

# Here's an example of checking for missing values:
import pandas as pd

df = pd.read_csv('books.csv')
print(df.isnull().sum())




# Date Operations:
# Pandas provides various functions for date operations such as 
# to_datetime(), date_range(), etc. 

# Here's an example of converting a column to datetime:
import pandas as pd

df = pd.read_csv('books.csv')
df['Published_Date'] = pd.to_datetime(df['Published_Date'])
print(df.head())




# Styling Data Frames:
# Pandas provides various functions for styling DataFrames such as
#  style.format(), style.highlight_max(), etc. 

# Here's an example of formatting a column:
import pandas as pd

df = pd.read_csv('books.csv')
df.style.format({'Score': '{:.2f}'})




# Misc:
# Pandas provides various miscellaneous functions such as 
# get_dummies(), melt(), pivot_table(), etc.

# Here's an example of using get_dummies():
import pandas as pd

df = pd.read_csv('books.csv')
df = pd.get_dummies(df, columns=['Genre'])
print(df.head())


#Dropping columns and rows
# Given a dataset colombia-real-estate-2 that has features:
#  0   property_type  3066 non-null   object 
#  1   department     3066 non-null   object 
#  2   lat            2958 non-null   float64
#  3   lon            2958 non-null   float64
#  4   area_m2        3066 non-null   float64
#  5   price_cop      3066 non-null   float64
#  6   price_m2       3066 non-null   float64
# and we want to drop column 'department', the code would look like:

df = pd.read_csv("data/colombia-real-estate-2.csv")
df = df.drop("department", axis="columns")

# Dropping an entire row the axis changes to index
# eg:
df = pd.read_csv("data/colombia-real-estate-2.csv")
df = df.drop(5, axis="index")

# Including rows with empty cells can radically skew the results of our analysis, 
# so we often drop them from the dataset. We can do this with the dropna method. 
# If we wanted to do this with df, the code would look like this:
df = pd.read_csv("data/colombia-real-estate-2.csv")
df = df.dropna(inplace=True)
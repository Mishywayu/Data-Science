# 1. Importing Data from CSV Files
CSV (Comma-Separated Values) is the most common format for storing tabular data. The pandas library provides a simple method to read CSV files into a DataFrame.  
import pandas as pd

-- Import data from a CSV file  
df = pd.read_csv('books.csv')  
-- Display the first few rows  
print(df.head())  

#### Handling CSV Parameters  
* sep: Specifies the delimiter (default is ,).
* header: Row number to use as the column names.
* index_col: Column to use as the row labels.
* usecols: Subset of columns to read.  

--Custom delimiter and specific columns   
df = pd.read_csv('books.csv', sep=';', usecols=['Title', 'Author', 'Year'])


# 2. Importing Data from Excel Files
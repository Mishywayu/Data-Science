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
Excel files are widely used for storing structured data. Pandas can read Excel files using the read_excel() function.

-- Import data from an Excel file  
df = pd.read_excel('books.xlsx')  

-- Display the first few rows  
print(df.head())  

#### Handling Excel Parameters
* sheet_name: Name or index of the sheet to read.
* usecols: Columns to import.
* skiprows: Rows to skip at the beginning.
* header: Row to use as column names.

-- Import data from a specific sheet and columns  
df = pd.read_excel('books.xlsx', sheet_name='Sheet1', usecols='A:D')

# 3. Importing Data from SQL Databases
SQL databases are commonly used for storing and managing large datasets. You can use sqlite3 for SQLite databases or SQLAlchemy for more complex databases like MySQL or PostgreSQL.

### Using SQLite and Pandas
import sqlite3  
import pandas as pd  

-- Connect to SQLite database  
conn = sqlite3.connect('books.db')  

-- Import data from a SQL query  
df = pd.read_sql_query("SELECT * FROM books", conn)

--Display the first few rows  
print(df.head())

### Using SQLAlchemy
from sqlalchemy import create_engine  
import pandas as pd  

-- Create an engine for a MySQL database  
engine = create_engine('mysql+pymysql://  user:password@localhost/books_db')

-- Import data from a SQL table  
df = pd.read_sql_table('books', engine)  

-- Display the first few rows  
print(df.head())

# 4. Importing Data from JSON Files
JSON (JavaScript Object Notation) is a common format for representing structured data, especially in web applications.

import pandas as pd  

-- Import data from a JSON file  
df = pd.read_json('books.json')

-- Display the first few rows  
print(df.head())

### Handling JSON Structure
If the JSON structure is complex (e.g., nested):  

import pandas as pd  

-- Import data from a nested JSON file  
df = pd.read_json('books_nested.json')

-- Normalize the nested JSON into a flat table  
df_flat = pd.json_normalize(df['nested_column'])

# 5. Importing Data from Web APIs

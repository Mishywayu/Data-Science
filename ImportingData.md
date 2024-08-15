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
APIs (Application Programming Interfaces) are used to retrieve data from web services.

import requests  
import pandas as pd

-- Fetch data from an API  
response = requests.get('https://api.example.com/books')
data = response.json()

-- Convert JSON data to DataFrame  
df = pd.DataFrame(data)

-- Display the first few rows  
print(df.head())

# 6. Importing Data via Web Scraping
Web scraping involves extracting data from websites using programming languages.  
'BeautifulSoup' and 'requests' are commonly used libraries for this purpose.

import requests  
from bs4 import BeautifulSoup  
import pandas as pd  

-- Fetch HTML content from a webpage  
response = requests.get('https://example.com/books')
soup = BeautifulSoup(response.content, 'html.parser')

-- Extract relevant data (assuming table structure)  
table = soup.find('table')  
df = pd.read_html(str(table))[0]

-- Display the first few rows  
print(df.head())

# 7. Importing Data from Dictionaries
Dictionaries are a common way to represent structured data in Python, where data is stored in key-value pairs. You can easily convert dictionaries to a pandas DataFrame, which is a powerful data structure for analyzing tabular data.

## (a) Basic Dictionary to DataFrame / Dictionary of Lists
If you have a dictionary where the keys represent column names and the values are lists (representing rows of data), you can directly convert it to a DataFrame.

import pandas as pd  

-- Example dictionary  
data = {  
    "Title": ["Book A", "Book B", "Book C"],  
    "Author": ["Author A", "Author B", "Author C"],  
    "Year": [2001, 2005, 2010],  
    "Price": [10.99, 12.99, 8.99]  
}

-- Convert dictionary to DataFrame  
df = pd.DataFrame(data)

-- Display the DataFrame  
print(df)


## (b) Dictionary of Dictionaries
If your dictionary contains nested dictionaries, where the outer dictionary keys are row labels and inner dictionaries represent column names, you can still convert this structure into a DataFrame.

import pandas as pd  

-- Example dictionary  
books_dict = {  
    "Book1": {"Title": "The Great Gatsby",   "Author": "F. Scott Fitzgerald", "Year": 1925,  "Price": 10.99},  
    "Book2": {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year": 1960, "Price": 7.99},  
    "Book3": {"Title": "1984", "Author": "George Orwell", "Year": 1949, "Price": 8.99}    
}

-- Convert dictionary of dictionaries to DataFrame  
df = pd.DataFrame(books_dict).T  # Transpose to get the right structure

-- Display the DataFrame  
print(df)

## (c) Using Lists of Dictionaries
If you have a list of dictionaries where each dictionary represents a row, you can convert this directly to a DataFrame.

import pandas as pd  

-- Example list of dictionaries  
books_list = [  
    {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year": 1925, "Price": 10.99},  
    {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year": 1960, "Price": 7.99},  
    {"Title": "1984", "Author": "George Orwell", "Year": 1949, "Price": 8.99}  
]

-- Convert list of dictionaries to DataFrame  
df = pd.DataFrame(books_list)

-- Display the DataFrame  
print(df)

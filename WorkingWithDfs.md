# Working with DataFrames in Python (Using a Books Dataset)
Pandas is the go-to library in Python for working with tabular data.  
DataFrames, a core data structure in Pandas, provide powerful tools for data manipulation, analysis, and visualization.

# 1. Creating a DataFrame
You can create a DataFrame in several ways: from dictionaries, lists of dictionaries, CSV files, etc.

### Example code
import pandas as pd  

--Creating a DataFrame from a dictionary  
data = {  
    "Title": ["The Great Gatsby", "To Kill a Mockingbird", "1984"],    
    "Author": ["F. Scott Fitzgerald", "Harper Lee", "George Orwell"],  
    "Year": [1925, 1960, 1949],  
    "Price": [10.99, 7.99, 8.99]  
}

df = pd.DataFrame(data)  
print(df)

# 2. Reading and Writing DataFrames
You can load data into a DataFrame from various file formats and also export it.
## a. Reading from a CSV File
### Example code
df = pd.read_csv('books.csv')  
print(df.head())  # Display the first 5 rows

## b. Writing to a CSV File
### Example code
df.to_csv('output_books.csv', index=False)

## c. Reading from Excel
### Example code 
df = pd.read_excel('books.xlsx', sheet_name='Sheet1')

## d. Writing to Excel
df.to_excel('output_books.xlsx', index=False)

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

# 3. Data Exploration
Exploring the structure and contents of your DataFrame is essential.
## a. Viewing Data
* First 5 rows  
print(df.head())

* Last 5 rows  
print(df.tail())

* Summary statistics  
print(df.describe())

* Data types
print(df.dtypes)

## b. Shape of Data
print(df.shape)  # (rows, columns)

## c. Information Summary
print(df.info())


# 4. Selecting Data
You can select data from a DataFrame using various methods.

## a. Selecting Columns
### Example code
-- Single column  
print(df['Title'])

-- Multiple columns  
print(df[['Title', 'Author']])

## b. Selecting Rows
* By Index Position:  
print(df.iloc[0])  # First row

* By Index Label:  
df.set_index('Title', inplace=True)  
print(df.loc['1984'])  # Row with index '1984'

## c. Slicing Data
### Example code
-- Slicing rows  
print(df.iloc[1:3])

-- Slicing columns  
print(df.iloc[:, 0:2])

# 5. Filtering Data
You can filter data based on conditions.

### Example code
-- Books published after 1950  
print(df[df['Year'] > 1950])

-- Books priced below $10  
print(df[df['Price'] < 10])


# 6. Adding and Removing Data
## a. Adding Columns
#### Example code
-- Adding a new column  
df['Discounted Price'] = df['Price'] * 0.9
print(df)

## b. Removing Columns
#### Example code
-- Removing a column  
df.drop('Discounted Price', axis=1, inplace=True)


## c. Adding Rows
#### Example code
-- Adding a new row  
new_book = pd.Series({  
    "Title": "Brave New World",  
    "Author": "Aldous Huxley",  
    "Year": 1932,  
    "Price": 6.99  
    })  
df = df.append(new_book, ignore_index=True)  
print(df)


## d. Removing Rows
#### Example code
-- Removing a row by index  
df.drop(0, axis=0, inplace=True)


# 7. Handling Missing Data
Missing data can be filled, replaced, or removed.
### Example code
-- Checking for missing values  
print(df.isnull().sum())

-- Filling missing values  
df.fillna(value={"Price": df['Price'].mean()}, inplace=True)

-- Dropping rows with missing values  
df.dropna(inplace=True)


# 8. Sorting Data
Sorting is crucial for organizing data.
### Example code
-- Sort by a single column  
df.sort_values(by='Price', ascending=False, inplace=True)

-- Sort by multiple columns  
df.sort_values(by=['Year', 'Price'], ascending=[True, False], inplace=True)


# 9. Grouping and Aggregating
Grouping and aggregation are essential for summarizing data.

-- Grouping by 'Author' and summing prices  
author_group = df.groupby('Author')['Price'].sum()
print(author_group)


# 10. Merging and Joining DataFrames
You can merge and join DataFrames to combine data from multiple sources.

### Example code
-- Example DataFrames  
df1 = pd.DataFrame({  
    "Title": ["The Great Gatsby", "1984", "The Catcher in the Rye"],  
    "Genre": ["Fiction", "Dystopian", "Fiction"]  
})

df2 = pd.DataFrame({  
    "Title": ["The Great Gatsby", "1984", "Moby Dick"],  
    "Sales": [1500000, 2500000, 500000]  
})

-- Merging on 'Title'  
merged_df = pd.merge(df1, df2, on='Title', how='inner')  
print(merged_df)


# 11. Pivot Tables
Pivot tables allow you to reshape data for easier analysis.

-- Creating a pivot table  
pivot_table = df.pivot_table(values='Price', index='Author', columns='Year', aggfunc='mean')  
print(pivot_table)

# 12. Working with Dates
Handling dates is common in time series data.

-- Converting a column to datetime  
df['Publication Date'] = pd.to_datetime(df['Year'], format='%Y')

-- Extracting year, month, day  
df['Year'] = df['Publication Date'].dt.year


# 13. Applying Functions
You can apply custom functions to DataFrame elements.

-- Applying a lambda function to each element in a column  
df['Price After Tax'] = df['Price'].apply(lambda x: x * 1.05)


# 14. Visualizing Data
Pandas integrates well with Matplotlib for quick plotting.  

import matplotlib.pyplot as plt  

-- Simple plot of prices  
df['Price'].plot(kind='bar')  
plt.show()


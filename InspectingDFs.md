# Inspecting DataFrames
Inspecting DataFrames using pandas is an essential skill for data analysis, as it allows you to understand the structure, contents, and quality of your dataset.  

## 1. Basic Information about the DataFrame
### 1.1. df.info()
* Provides a concise summary of the DataFrame.
* Displays the number of non-null entries, data types, and memory usage.
### 1.2. df.shape
* Returns a tuple representing the dimensionality of the DataFrame: (rows, columns).
### 1.3. df.columns
* Returns an Index object containing column names.
### 1.4. df.index
* Returns an Index object representing the row labels.
### 1.5. df.head(n)
* Displays the first n rows of the DataFrame (default is 5).
### 1.6. df.tail(n)
* Displays the last n rows of the DataFrame (default is 5).
### 1.7. df.describe()
* Generates descriptive statistics for numerical columns, including count, mean, standard deviation, min, and percentiles.

## 2. Accessing and Inspecting Columns
### 2.1. Access a single column
* Use square brackets or dot notation to access a single column.  
eg:   
df['Name']  
df.Name

### 2.2. Access multiple columns
* Use a list of column names.  
eg:  
df[['Name', 'Age']]

## 3. Accessing and Inspecting Rows
### 3.1 df.loc[]
* Access a group of rows and columns by labels or a boolean array.  
Eg:  
df.loc[1]  # Access row with index label 1  
df.loc[1:3]  # Access rows with index labels 1 to 3  
df.loc[df['Department'] == 'HR']  # Access rows where 'Department' is 'HR'  

### 3.2 df.iloc[]
* Access rows and columns by integer-location based indexing.  
Eg:  
df.iloc[2]  # Access the 3rd row  
df.iloc[1:4]  # Access rows 2 to 4 (exclusive)  
# 1. Handling Missing Data
* Identifying Missing Data:  
Missing data can be identified using isna() or isnull().
* Dropping Missing Data:  
Remove rows or columns with missing data using dropna().
* Filling Missing Data:  
Fill missing values using fillna(), interpolate(), or other methods.


# 2. Handling Duplicates
* Identifying Duplicates:  
Use duplicated() to find duplicate rows.
* Removing Duplicates:  
Use drop_duplicates() to remove duplicates.


# 3. Handling Outliers
* Identifying Outliers:  
Use methods like the Z-score, IQR, or visualization to detect outliers.
* Removing/Transforming Outliers:  
Remove outliers or transform them using capping, flooring, or replacing.


# 4. String Manipulation
* Removing Whitespace:  
Use str.strip(), str.lstrip(), str.rstrip() to remove whitespace.
* Replacing Values:  
Use str.replace() to replace substrings.
* Changing Case:  
Use str.lower(), str.upper(), str.title() to change the case of strings.


# 5. Converting Data Types
* Converting Data Types:  
Use astype() to convert data types.
* Handling Conversion Errors:  
Use pd.to_numeric() with errors='coerce' to handle errors in conversion.


# 6. Renaming Columns
* Renaming Single or Multiple Columns:  
Use rename() to rename columns.
* Renaming All Columns:  
Use df.columns to set new column names.


# 7. Handling Categorical Data
* Converting Categorical Data:  
Convert text or string columns to categorical data using astype('category').
* One-Hot Encoding:  
Use pd.get_dummies() for one-hot encoding.


# 8. Handling Date/Time Data
* Parsing Dates:  
Use pd.to_datetime() to convert strings to datetime objects.
* Extracting Date/Time Components:  
Extract year, month, day, etc., using .dt accessor.
* Setting Date as Index:  
Use set_index() to set a date column as the index.


# 9. Reindexing and Resampling
* Reindexing:  
Use reindex() to change the index of the DataFrame.
* Resampling Time Series Data:  
Use resample() to resample time series data.


# 10. Merging, Joining, and Concatenating
* Merging DataFrames:  
Use merge() to combine DataFrames based on keys.
* Joining DataFrames:  
Use join() to join DataFrames on indexes.
* Concatenating DataFrames:  
Use concat() to concatenate DataFrames along a particular axis.


# 11. Pivoting and Melting
* Pivoting:  
Use pivot() or pivot_table() to reshape data.
* Melting:  
Use melt() to unpivot data.


# 12. Data Transformation
* Applying Functions:  
Use apply(), applymap(), or map() to apply functions to DataFrame elements.
* Lambda Functions:  
Use lambda functions for inline operations.


# 13. Grouping and Aggregation
* Grouping:  
Use groupby() to group data based on one or more columns.
* Aggregation:  
Use functions like sum(), mean(), count(), etc., on grouped data


# 14. Removing Irrelevant Data
* Dropping Columns:  
Use drop() to remove unnecessary columns.
* Filtering Rows:  
Use conditions to filter out irrelevant rows.


# 15. Dealing with Large Datasets
* Chunking:  
Use read_csv() with chunksize to process large datasets in chunks.
* Optimizing Data Types:  
Convert columns to appropriate data types to save memory.
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
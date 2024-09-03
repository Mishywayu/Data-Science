import pandas as pd

# 1. Loading dataset to a dataframe
# file_path = "large_synthetic_dataset.csv"
df = pd.read_csv("large_synthetic_dataset.csv")
print(df.head())

# 2. Identifying columns with missing values and the number of missing values.
print(df.info()) #There are no missing values

#If there were missing values then this would been the code
# missing_values = df.isnull().sum() #Finding missing values and sum in eaach column
# print(missing_values)
# # Impute missing values in the Age column with the mean value
# if 'Age' in df.columns:
#     mean_age = df['Age'].mean()
#     df['Age'] = df['Age'].fillna(mean_age)
#     print(f"Missing 'Age' values filled with mean: {mean_age}")
# #Fill missing Department values with "Not Specified"
# if 'Department' in df.columns:
#     df['Department'] = df['Department'].fillna('Not Specified')
#     print("Missing 'Department' values filled with 'Not Specified'")

# 3. Dealing with Inconsistent Data:
df['Department'] = df['Department'].str.upper() #changing values to uppercase
print(df['Department'])

df['Comments'] = df['Comments'].str.strip()
print(df['Comments'])

print(df.duplicated().sum()) #check duplicate rows
# if there were duplicated rows to remove them this would have been the code:
# df = df.drop_duplicates()


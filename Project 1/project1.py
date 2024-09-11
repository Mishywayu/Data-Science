import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading dataset to a dataframe
# file_path = "large_synthetic_dataset.csv"
df = pd.read_csv("large_synthetic_dataset.csv")
# print(df.head())

# 2. Identifying columns with missing values and the number of missing values.
# print(df.info()) #There are no missing values

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
# print(df['Department'])

df['Comments'] = df['Comments'].str.strip()
# print(df['Comments'])

# print(df.duplicated().sum()) #check duplicate rows
# if there were duplicated rows to remove them this would have been the code:
# df = df.drop_duplicates()


#CONVERTING THE JOINING DATE COLUMN TO A STANDARD DATETIME FORMAT (which is YYYY/MM/DD)
df["Joining Date"]=pd.to_datetime(df["Joining Date"])
print(df["Joining Date"])

# Extract the year and month from the Joining Date and create two new columns: Joining Year and Joining Month.
df["Joining Year"]=df["Joining Date"].dt.year
df['Joining Month'] = df['Joining Date'].dt.month

# print(df["Joining Year"])
# print(df["Joining Month"])
# print(df)




#7. Visualization:
# creating a scatter plot where x axis is age and y axis is salary uisng matplotlib (using Matplotlib)
fig, ax = plt.subplots()
ax.scatter(df["Age"], df["Salary"], color="orange", label="df1")
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.legend()
# plt.show()

# Create a box plot for Performance Score by Department.
average_scores = df.groupby('department')['performance_score'].mean().reset_index()

# print(df["Department"].unique())
# print(df.head())
print(df.info())
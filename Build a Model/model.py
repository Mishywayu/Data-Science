import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic DataSet (using pandas)
# filepath = './titanic.csv'
filepath_2 = './TITANIC2.csv'
df = pd.read_csv(filepath_2)


# Exploratory Data Analysis (EDA)
# prints out the first two observations
# print(df.head(2))
# provides a concise summary
# print(df.info())
# prints the dimension of the DF
# print(df.shape) 


#Feature Engineering
# drop columns with null values
df = df.dropna()
# df.info()


# Encoding Categorical Features
# One-hot encoding for 'sex' and 'embarked' features
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
# Let's drop columns that won't help (like 'name', 'ticket', 'fare')
df = df.drop(columns=['Name', 'Fare'])
df.info()

# # Selecting relevant features for modeling
# X = df[['pclass', 'Age', 'SibSp', 'Parch', 'sex_male']]
# y = df['Survived']

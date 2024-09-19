import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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
# df = df.dropna()
# df.info()


# Encoding Categorical Features
# One-hot encoding for 'sex' and 'embarked' features
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
# Let's drop columns that won't help (like 'name', 'ticket', 'fare')
df = df.drop(columns=['Name', 'Fare'])
df = df.dropna()
df.info()
# print(df['Embarked'].unique())
# df['Embarked_Q'].head()
# df['Embarked_S'].head(5)


# # Selecting relevant features for modeling
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Sex_male']]
y = df['Survived']


#MODEL SELECTION
# Splitting the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Instantiate the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model
model.fit(X_train, y_train)


#





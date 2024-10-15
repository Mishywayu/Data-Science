# Random Forest Classifier
Let's go deeper into the process of building a machine learning model, taking into consideration more complex data preprocessing, model selection, and performance evaluation techniques. This time, we’ll build a Random Forest Classifier for a classification problem using the Titanic dataset, which is a well-known dataset used in data science for binary classification tasks (whether a passenger survived or not).

We’ll cover:

1. Data Exploration & Preprocessing
2. Feature Engineering
3. Model Selection
4. Hyperparameter Tuning
5. Advanced Evaluation 


Check the code snippets in file: model.py

# 1. Data Exploration & Preprocessing
The first step in any machine learning pipeline is to understand and clean the data. Let’s load the Titanic dataset and explore it.

### Exploratory Data Analysis (EDA)
Before building the model, it’s crucial to explore the data to understand the underlying patterns, missing values, and relationships between features.

# 2. Feature Engineering
* 2(a) Handling Missing Values  
This requires addressing missing values in a manner suited to the data's context. 

code: df.info()  
output:  
![Alt text](./df.info().PNG)



* 2(b) Encoding Categorical Features  
Machine learning models generally work with numeric data, so categorical features need to be encoded into numeric format. We will use one-hot encoding for multi-class features and dropping any columns that won't help, like name, fare etc 

code: df = pd.get_dummies(df, columns=['sex', 'name'], drop_first=True)

#### ** Explanation **
* pd.get_dummies(df, ...):  
This function converts categorical variables (e.g., strings like 'male', 'female', or names) into dummy/indicator variables.  
Each unique value in the categorical column gets a new column, where the value is 1 if the observation falls into that category, and 0 otherwise.

* columns=['sex', 'name']:  
This specifies which columns in the DataFrame should be transformed into dummy variables.  
In this case, the columns 'sex' and 'name' are being transformed.  
If the sex column has values like 'male' and 'female', two new columns, sex_male and sex_female, will be created.  
Similarly, the name column will be converted into multiple dummy columns based on the unique names in the data.  

* drop_first=True:  
This argument prevents multicollinearity by dropping the first dummy column for each category.  
For example, if there are two categories, like male and female, instead of creating two columns (sex_male and sex_female), only one column (sex_male) will be created.  
If the value is 0, it's understood to be female. This helps reduce the number of columns and avoids redundancy.


* 2(c) Feature Selection
Let’s select the most relevant features for our model.  
You can use domain knowledge or automatic feature selection techniques (like Recursive Feature Elimination or feature importance) to determine the most important features.

code: 
#### Selecting relevant features for modeling
X = df[['pclass', 'age', 'sibsp', 'parch', 'sex_male', 'embarked_Q', 'embarked_S']]  
y = df['survived']  

#### ** Explanation **
1. Feature Selection (X):  
X represents the feature set that will be used to train the machine learning model.  
X = df[['pclass', 'age', 'sibsp', 'parch', 'sex_male', 'embarked_Q', 'embarked_S']]:  
This selects a subset of columns (features) from the DataFrame df.  
These features are chosen because they are likely relevant to predicting whether a passenger survived.  
Explanation of Selected Features:  
- 'pclass': The passenger class (1st, 2nd, or 3rd class).
- 'age': The age of the passenger.
- 'sibsp': The number of siblings or spouses aboard the Titanic with the passenger.
- 'parch': The number of parents or children aboard the Titanic with the passenger.
- 'sex_male': A dummy variable representing the sex of the passenger. (1 for male, 0 for female—likely created using pd.get_dummies()).
- 'embarked_Q', 'embarked_S': Dummy variables representing the port of embarkation (Q for Queenstown, S for Southampton). Since there were three embarkation points (C = Cherbourg, Q = Queenstown, and S = Southampton), one of them (likely 'C') is dropped to avoid multicollinearity, often handled by drop_first=True in pd.get_dummies().  

2. Target Variable (y):
y represents the target variable, which is the outcome you are trying to predict.  
y = df['survived']:  
This selects the column 'survived' from the DataFrame df.  
The column 'survived' contains the labels for classification—whether each passenger survived (1) or not (0).  

# 3. Model Selection
Now, we’ll use a Random Forest classifier, which is a powerful ensemble method that combines multiple decision trees to improve predictive performance.

# 4. Hyperparameter Tuning
The performance of a Random Forest model can depend on hyperparameters such as the number of trees (n_estimators), the maximum depth of the trees, and the minimum number of samples required to split a node.

We’ll use GridSearchCV to perform hyperparameter tuning to find the best parameters.
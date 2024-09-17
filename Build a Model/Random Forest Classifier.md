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
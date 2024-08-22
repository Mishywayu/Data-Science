import pandas as pd

# Sample DataFrame with categorical data
df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Apple', 'Orange'],
    'Color': ['Red', 'Yellow', 'Green', 'Orange']
})

# Convert to categorical data type
df['Fruit'] = df['Fruit'].astype('category')

# One-hot encode categorical data
df_encoded = pd.get_dummies(df, columns=['Fruit'])

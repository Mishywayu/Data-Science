# import pandas as pd
import matplotlib.pyplot as plt #for data visualization
from sklearn.datasets import load_breast_cancer #to load the dataset

data = load_breast_cancer(as_frame=True)
df = data.frame

# print (df.head(5))
# print (df.info())
# print (df.shape)

# check missing values
# print (df.isnull().sum()) #No missing value

#Visualization

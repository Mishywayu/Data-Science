# LINE PLOTS
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Plot directly using Pandas
df.plot(y=['sepal length (cm)', 'petal length (cm)'], kind='line', title="Line Plot of Sepal and Petal Lengths")

# Show plot
# plt.show()



# BAR PLOT
# Plot the mean values of the features using Pandas
df.mean().plot(kind='bar', title="Mean of Features in the Iris Dataset", rot=45)

# Show plot
# plt.show()



# HISTOGRAM
# Create a histogram for the sepal length
df['sepal length (cm)'].plot(kind='hist', bins=20, edgecolor='black', title="Histogram of Sepal Length")

# Show plot
plt.show()

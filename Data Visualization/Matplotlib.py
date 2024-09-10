#LINE PLOT
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset and convert to DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Plot
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')

# Add title, labels, and legend
plt.title("Line Plot of Sepal and Petal Lengths")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()

# Show plot
plt.show()



# BAR PLOT
# Create a summary of the mean values of each feature
means = df.mean()

# Plot bar chart
plt.bar(df.columns, means)

# Add title and labels
plt.title("Mean of Features in the Iris Dataset")
plt.ylabel("Mean Value")

# Rotate x labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.show()



#HISTOGRAM
plt.hist(df['sepal length (cm)'], bins=20, edgecolor='black')

# Add title and labels
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

# Show plot
plt.show()

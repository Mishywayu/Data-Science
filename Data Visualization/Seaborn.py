# SCATTER PLOT
import seaborn as sns
import matplotlib.pyplot as plt

# Load Seaborn's version of the iris dataset
iris = sns.load_dataset('iris')

# Scatter plot with regression line
sns.lmplot(x='sepal_length', y='petal_length', data=iris, hue='species')

# Title and show plot
plt.title("Scatter Plot of Sepal vs Petal Length with Regression Line")
plt.show()



# BOX PLOT
# Create a box plot of petal lengths for different species
sns.boxplot(x='species', y='petal_length', data=iris)

# Title and show plot
plt.title("Box Plot of Petal Length by Species")
plt.show()



# Pair Plot
# Pairplot to show relationships between all features
sns.pairplot(iris, hue='species')

# Show plot
plt.show()

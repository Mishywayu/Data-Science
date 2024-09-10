# # LINE PLOT
# from bokeh.plotting import figure, show
# from bokeh.io import output_notebook
# from sklearn.datasets import load_iris
# import pandas as pd

# output_notebook()

# # Load the dataset
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)

# # Create a Bokeh figure
# p = figure(title="Bokeh Line Plot of Sepal and Petal Lengths", x_axis_label="Index", y_axis_label="Length (cm)")

# # Add lines for Sepal and Petal lengths
# p.line(df.index, df['sepal length (cm)'], legend_label="Sepal Length", line_width=2)
# p.line(df.index, df['petal length (cm)'], legend_label="Petal Length", line_width=2, color="green")

# # Show plot
# show(p)



# SCATTER PLOT
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Convert the data to a format Bokeh can use
source = ColumnDataSource(df)

# Create a Bokeh figure
p = figure(title="Bokeh Scatter Plot of Sepal vs Petal Length", x_axis_label="Sepal Length (cm)", y_axis_label="Petal Length (cm)")

# Add a scatter plot
p.circle('sepal length (cm)', 'petal length (cm)', source=source, size=10, color="navy", alpha=0.5)

# Show plot
show(p)

# LINE PLOT
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset and convert to DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Create an interactive line plot
fig = go.Figure()

# Add lines for sepal and petal lengths
fig.add_trace(go.Scatter(x=df.index, y=df['sepal length (cm)'], mode='lines', name='Sepal Length'))
fig.add_trace(go.Scatter(x=df.index, y=df['petal length (cm)'], mode='lines', name='Petal Length'))

# Customize layout
fig.update_layout(title="Interactive Line Plot of Sepal and Petal Lengths", xaxis_title="Index", yaxis_title="Length (cm)")

# Show the interactive plot
# fig.show()



#BAR PLOT
# Mean values for features
means = df.mean()

# Create an interactive bar plot
fig = px.bar(x=df.columns, y=means, labels={'x': 'Feature', 'y': 'Mean Value'}, title="Mean of Features in the Iris Dataset")

# Show plot
# fig.show()



#SCATTER PLOT
# Create a scatter plot with Plotly
# fig = px.scatter(iris, x='sepal_length', y='petal_length', color='species', title="Interactive Scatter Plot of Sepal vs Petal Length")

# # Show plot
# fig.show()

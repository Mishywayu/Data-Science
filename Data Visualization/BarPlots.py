# Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Dataset: categorical data with counts
categories = ['A', 'B', 'C', 'D']
counts = [10, 20, 15, 5]

plt.bar(categories, counts)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Bar plot of categorical data')
plt.show()


# Seaborn
import seaborn as sns
import pandas as pd

# Dataset: survey responses
data = {'Category': ['A', 'B', 'C', 'D'], 
        'Response': [10, 20, 15, 5]}
df = pd.DataFrame(data)

sns.barplot(x='Category', y='Response', data=df)
plt.xlabel('Category')
plt.ylabel('Response')
plt.title('Bar plot of survey responses')
plt.show()


# Plotly
import plotly.express as px
import pandas as pd

# Dataset: sales by region
data = {'Region': ['North', 'South', 'East', 'West'], 
        'Sales': [100, 200, 150, 50]}
df = pd.DataFrame(data)

fig = px.bar(df, x='Region', y='Sales')
fig.show()


# Bokeh
import bokeh.plotting as bp
from bokeh.io import output_notebook
output_notebook()

# Dataset: website traffic by day
data = {'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], 
        'Traffic': [100, 200, 300, 400, 500]}

p = bp.figure(title='Bar plot of website traffic')
p.vbar(x=data['Day'], top=data['Traffic'], width=0.5)
p.xaxis.axis_label = 'Day'
p.yaxis.axis_label = 'Traffic'
bp.show(p)


# ggplot
import ggplot

# Dataset: survey responses
data = {'Category': ['A', 'B', 'C', 'D'], 
        'Response': [10, 20, 15, 5]}

ggplot(data, aes(x='Category', y='Response')) + 
    geom_bar(stat='identity') + 
    labs(title='Bar plot of survey responses', x='Category', y='Response')


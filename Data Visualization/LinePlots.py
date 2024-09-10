# Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Dataset: sin(x) from 0 to 10
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line plot of sin(x)')
plt.show()


# Seaborn
import seaborn as sns
import pandas as pd

# Dataset: stock prices over time
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
        'Price': [100, 105, 110, 108, 112]}
df = pd.DataFrame(data)

sns.lineplot(x='Date', y='Price', data=df)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Line plot of stock prices')
plt.show()


# Plotly
import plotly.express as px
import pandas as pd

# Dataset: temperature over time
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
        'Temperature': [20, 22, 25, 24, 26]}
df = pd.DataFrame(data)

fig = px.line(df, x='Date', y='Temperature')
fig.show()


# Bokeh
import bokeh.plotting as bp
from bokeh.io import output_notebook
output_notebook()

# Dataset: CPU usage over time
data = {'Time': [1, 2, 3, 4, 5], 'CPU': [20, 30, 40, 50, 60]}

p = bp.figure(title='Line plot of CPU usage')
p.line(data['Time'], data['CPU'], legend_label='CPU Usage')
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'CPU (%)'
bp.show(p)


# ggplot
import ggplot

# Dataset: exam scores over time
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Score': [80, 85, 90, 92, 95]}

ggplot(data, aes(x='Year', y='Score')) + 
    geom_line() + 
    labs(title='Line plot of exam scores', x='Year', y='Score')
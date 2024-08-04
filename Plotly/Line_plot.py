import plotly.graph_objs as go
import plotly.offline as pyo

# Line plot
trace = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[10, 15, 13, 17, 22],
    mode='lines',
    name='Line Plot'
)
data = [trace]
layout = go.Layout(title='Line Plot')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='line_plot.html')

# Scatter plot
trace = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[10, 15, 13, 17, 22],
    mode='markers',
    name='Scatter Plot'
)
data = [trace]
layout = go.Layout(title='Scatter Plot')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter_plot.html')

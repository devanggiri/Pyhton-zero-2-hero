# Histogram
trace = go.Histogram(
    x=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    name='Histogram'
)
data = [trace]
layout = go.Layout(title='Histogram')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='histogram.html')

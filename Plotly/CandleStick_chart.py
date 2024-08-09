import plotly.graph_objs as go

# Candlestick chart
trace = go.Candlestick(
    x=['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
    open=[10, 11, 12, 11, 13],
    high=[15, 16, 17, 16, 18],
    low=[5, 6, 7, 6, 8],
    close=[12, 14, 13, 15, 17],
    name='Candlestick Chart'
)
data = [trace]
layout = go.Layout(title='Candlestick Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='candlestick_chart.html')

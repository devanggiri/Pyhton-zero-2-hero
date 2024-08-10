# Multiple subplots
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, subplot_titles=('Plot 1', 'Plot 2'))

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name='Line')
trace2 = go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2], name='Bar')

fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=1, col=2)

fig.update_layout(title='Multiple Subplots')
pyo.plot(fig, filename='multiple_subplots.html')

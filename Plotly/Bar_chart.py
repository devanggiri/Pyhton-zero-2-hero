# Bar chart
trace = go.Bar(
    x=['A', 'B', 'C', 'D'],
    y=[5, 7, 3, 8],
    name='Bar Chart'
)
data = [trace]
layout = go.Layout(title='Bar Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar_chart.html')

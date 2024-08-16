# Pie chart
trace = go.Pie(
    labels=['A', 'B', 'C', 'D'],
    values=[5, 7, 3, 8],
    name='Pie Chart'
)
data = [trace]
layout = go.Layout(title='Pie Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='pie_chart.html')

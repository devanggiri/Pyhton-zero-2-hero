# Bubble chart
trace = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
        color=[0, 1, 2, 3]
    ),
    name='Bubble Chart'
)
data = [trace]
layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_chart.html')

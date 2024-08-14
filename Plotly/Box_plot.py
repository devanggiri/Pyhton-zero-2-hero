# Box plot
trace = go.Box(
    y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    name='Box Plot'
)
data = [trace]
layout = go.Layout(title='Box Plot')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box_plot.html')

# Heatmap
trace = go.Heatmap(
    z=[[1, 20, 30],
       [20, 1, 60],
       [30, 60, 1]],
    name='Heatmap'
)
data = [trace]
layout = go.Layout(title='Heatmap')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')

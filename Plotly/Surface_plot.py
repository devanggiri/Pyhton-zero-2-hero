# Surface plot
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

trace = go.Surface(
    z=z,
    name='Surface Plot'
)
data = [trace]
layout = go.Layout(title='Surface Plot')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='surface_plot.html')

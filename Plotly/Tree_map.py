import plotly.express as px

# Treemap
df = px.data.tips()
fig = px.treemap(
    df,
    path=['sex', 'day', 'time'],
    values='total_bill',
    title='Treemap'
)
pyo.plot(fig, filename='treemap.html')

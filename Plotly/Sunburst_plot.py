import plotly.express as px

# Sunburst chart
df = px.data.tips()
fig = px.sunburst(
    df, 
    path=['sex', 'day', 'time'],
    values='total_bill',
    title='Sunburst Chart'
)
pyo.plot(fig, filename='sunburst_chart.html')

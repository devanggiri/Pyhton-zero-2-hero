import plotly.express as px

# Funnel chart
df = px.data.tips()
fig = px.funnel(
    df,
    x='total_bill',
    y='day',
    title='Funnel Chart'
)
pyo.plot(fig, filename='funnel_chart.html')

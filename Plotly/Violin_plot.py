import plotly.express as px

# Violin plot
df = px.data.tips()
fig = px.violin(
    df, 
    y="total_bill", 
    x="day", 
    color="sex", 
    box=True, 
    points="all",
    title='Violin Plot'
)
pyo.plot(fig, filename='violin_plot.html')

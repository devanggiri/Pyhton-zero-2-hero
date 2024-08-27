# Categorical Plot (Catplot)
sns.catplot(x='survived', y='age', hue='sex', kind='swarm', data=data)
plt.title('Categorical Plot')
plt.show()

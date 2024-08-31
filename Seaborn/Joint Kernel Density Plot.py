# Joint Kernel Density Plot
sns.jointplot(x='fare', y='age', data=data, kind="kde", hue="survived")
plt.title('Joint Kernel Density Plot')
plt.show()

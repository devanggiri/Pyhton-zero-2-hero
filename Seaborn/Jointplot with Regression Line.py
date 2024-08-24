# Jointplot with Regression Line
sns.jointplot(x='age', y='fare', data=data, kind="reg", color="g")
plt.title('Jointplot with Regression Line')
plt.show()

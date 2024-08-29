# Diverging Palette Plot
sns.kdeplot(data['fare'], data['age'], cmap="coolwarm", fill=True, clip_on=False)
plt.title('Diverging Color Palette Plot')
plt.show()

# Multivariate KDE Plot
sns.kdeplot(data['age'], data['fare'], cmap="viridis", fill=True)
plt.title('Multivariate KDE Plot')
plt.show()

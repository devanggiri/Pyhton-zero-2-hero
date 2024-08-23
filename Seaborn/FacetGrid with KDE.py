# FacetGrid with KDE
g = sns.FacetGrid(data, hue="survived", col="class")
g.map(sns.kdeplot, "age", shade=True)
g.add_legend()
plt.show()

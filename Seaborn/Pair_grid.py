# PairGrid
g = sns.PairGrid(data, hue="survived")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()

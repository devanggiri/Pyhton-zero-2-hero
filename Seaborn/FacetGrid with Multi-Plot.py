import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = sns.load_dataset('titanic')

# FacetGrid for multiple plots
g = sns.FacetGrid(data, col="survived", row="class", margin_titles=True)
g.map(sns.histplot, "age",

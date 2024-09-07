import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Sample dataset (Iris dataset)
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
print("Original DataFrame:\n", df.head())

# Standardizing the features before applying dimensionality reduction techniques
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('target', axis=1))

# 1. Principal Component Analysis (PCA)
pca = PCA(n_components=2)  # Reducing to 2 dimensions
X_pca = pca.fit_transform(X_scaled)
print("\nExplained Variance by PCA components:", pca.explained_variance_ratio_)

# Visualizing PCA result
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['target'], cmap='viridis', edgecolor='k', s=100)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label='Target')
plt.show()

# 2. Linear Discriminant Analysis (LDA)
lda = LDA(n_components=2)  # Reducing to 2 dimensions
X_lda = lda.fit_transform(X_scaled, df['target'])
print("\nExplained Variance by LDA components:", lda.explained_variance_ratio_)

# Visualizing LDA result
plt.figure(figsize=(8,6))
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=df['target'], cmap='coolwarm', edgecolor='k', s=100)
plt.title("LDA of Iris Dataset")
plt.xlabel("LDA Component 1")
plt.ylabel("LDA Component 2")
plt.colorbar(label='Target')
plt.show()

# 3. t-SNE (t-Distributed Stochastic Neighbor Embedding)
tsne = TSNE(n_components=2, random_state=0, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# Visualizing t-SNE result
plt.figure(figsize=(8,6))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=df['target'], cmap='plasma', edgecolor='k', s=100)
plt.title("t-SNE of Iris Dataset")
plt.xlabel("t-SNE Component 1")
plt.ylabel("t-SNE Component 2")
plt.colorbar(label='Target')
plt.show()

# 4. Autoencoders for Dimensionality Reduction
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# Define an autoencoder model
input_dim = X_scaled.shape[1]
encoding_dim = 2  # Reducing to 2 dimensions

# Autoencoder architecture
input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='sigmoid')(encoded)

# Model for compression (encoder)
autoencoder = Model(input_layer, decoded)
encoder = Model(input_layer, encoded)

# Compile and train the autoencoder
autoencoder.compile(optimizer='adam', loss='mean_squared_error')
autoencoder.fit(X_scaled, X_scaled, epochs=50, batch_size=16, shuffle=True)

# Obtain the reduced data
X_autoencoder = encoder.predict(X_scaled)

# Visualizing Autoencoder result
plt.figure(figsize=(8,6))
plt.scatter(X_autoencoder[:, 0], X_autoencoder[:, 1], c=df['target'], cmap='inferno', edgecolor='k', s=100)
plt.title("Autoencoder of Iris Dataset")
plt.xlabel("Autoencoder Component 1")
plt.ylabel("Autoencoder Component 2")
plt.colorbar(label='Target')
plt.show()



'''
Techniques Explained:
Principal Component Analysis (PCA):

PCA is a widely used technique that transforms the data into a set of linearly uncorrelated variables called principal components.
PCA reduces dimensionality by identifying directions (principal components) along which the variance of the data is maximum.
The variance explained by each component is displayed using pca.explained_variance_ratio_.
Linear Discriminant Analysis (LDA):

LDA is a supervised method that maximizes the separability between known categories (e.g., target classes).
It tries to model the difference between classes and is useful when there are categorical targets.
LDA also returns the explained variance of the components using lda.explained_variance_ratio_.
t-Distributed Stochastic Neighbor Embedding (t-SNE):

t-SNE is a non-linear dimensionality reduction technique that preserves the local structure of the data.
It's commonly used for high-dimensional data visualization in two or three dimensions.
Unlike PCA and LDA, t-SNE does not rely on the linearity of the data and is particularly useful for complex datasets.
Autoencoders (Neural Network-Based):

Autoencoders are a type of neural network that compresses the data into a lower-dimensional representation (latent space) and then reconstructs it.
The encoder network reduces the dimensions, and the decoder reconstructs the original data.
Autoencoders are a versatile method for non-linear dimensionality reduction and can handle highly complex datasets.
Summary of Methods for Dimensionality Reduction:
PCA: Reduces dimensionality while preserving as much variance as possible. Best for linear data.
LDA: Supervised method for dimensionality reduction that focuses on maximizing class separability.
t-SNE: Non-linear technique that focuses on preserving local structure, best suited for visualization.
Autoencoders: Neural network-based, non-linear dimensionality reduction suitable for complex data.
'''

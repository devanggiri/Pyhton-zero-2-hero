
 import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline

# Sample Dataset
data = {
    'Age': [25, 30, np.nan, 22, 45],
    'Gender': ['Male', 'Female', 'Female', 'Male', np.nan],
    'Income': [50000, 60000, 70000, np.nan, 45000],
    'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes'],
    'Review': ["Great product", "Not good", "Excellent quality", np.nan, "Bad experience"]
}

df = pd.DataFrame(data)

# Step 1: Handling Missing Data
numerical_imputer = SimpleImputer(strategy='mean')
categorical_imputer = SimpleImputer(strategy='most_frequent')

df['Age'] = numerical_imputer.fit_transform(df[['Age']])
df['Income'] = numerical_imputer.fit_transform(df[['Income']])
df['Gender'] = categorical_imputer.fit_transform(df[['Gender']])
df['Review'] = categorical_imputer.fit_transform(df[['Review']])

# Step 2: Encoding Categorical Features
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

one_hot_encoder = OneHotEncoder(sparse=False)
gender_encoded = one_hot_encoder.fit_transform(df[['Gender']])
gender_encoded_df = pd.DataFrame(gender_encoded, columns=one_hot_encoder.get_feature_names_out(['Gender']))
df = df.drop('Gender', axis=1)
df = pd.concat([df, gender_encoded_df], axis=1)

# Step 3: Text Feature Extraction (TF-IDF)
tfidf_vectorizer = TfidfVectorizer(max_features=5)
tfidf_features = tfidf_vectorizer.fit_transform(df['Review']).toarray()
tfidf_df = pd.DataFrame(tfidf_features, columns=tfidf_vectorizer.get_feature_names_out())
df = df.drop('Review', axis=1)
df = pd.concat([df, tfidf_df], axis=1)

# Step 4: Feature Scaling
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])

# Step 5: Dimensionality Reduction (PCA)
pca = PCA(n_components=2)
pca_features = pca.fit_transform(df)

# Step 6: Feature Selection
X = df.drop('Purchased', axis=1)
y = df['Purchased']
selector = SelectKBest(f_classif, k=2)
X_new = selector.fit_transform(X, y)

# Output Results
print("Original DataFrame:")
print(df)
print("\nPCA Output (Reduced to 2 dimensions):")
print(pca_features)
print("\nSelected Features using SelectKBest (ANOVA):")
print(X_new)







'''
Explanation of the Pipeline Steps:
Handling Missing Data:

Impute missing numerical data with the mean value, and categorical data with the most frequent value (mode).
Encoding Categorical Features:

Label Encoding converts binary categories to numerical values (e.g., "Yes" becomes 1 and "No" becomes 0).
One-Hot Encoding creates binary columns for non-binary categories (e.g., "Male" and "Female" become separate columns).
Text Feature Extraction (TF-IDF):

TF-IDF is used to convert text data into numerical features based on word importance in the document.
Feature Scaling:

StandardScaler scales numerical features to have a mean of 0 and a variance of 1, ensuring all features have the same scale.
Dimensionality Reduction (PCA):

PCA reduces the dimensionality of the dataset while retaining most of the variance.
Feature Selection (SelectKBest):

SelectKBest selects the top k features based on ANOVA F-value, which helps in choosing the most relevant features for your model.
Customization Tips:
You can use other imputation strategies (like median or constant) depending on the nature of your dataset.
For scaling, you can also try MinMaxScaler if your dataset needs normalization instead of standardization.
For feature extraction, if you have a different type of data (like categorical data with many levels), you could consider using frequency encoding or target encoding.
If dimensionality reduction needs more components, increase n_components in the PCA step. Similarly, SelectKBest can choose the top k features as required.
This pipeline can be extended and customized based on the dataset you're working with and the type of features you want to extract and process.
'''

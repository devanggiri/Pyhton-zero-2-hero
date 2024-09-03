import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv('your_dataset.csv')

# 1. View Basic Information
print("Basic Information:")
print(df.info())
print("\nFirst 5 rows:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# 2. Handling Missing Values
# 2.1 Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# 2.2 Drop rows with missing values (if necessary)
df_cleaned = df.dropna()

# 2.3 Fill missing values with mean (or other strategies)
df['column_with_na'] = df['column_with_na'].fillna(df['column_with_na'].mean())

# 3. Handle Duplicates
# 3.1 Check for duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# 3.2 Drop duplicates
df_cleaned = df.drop_duplicates()

# 4. Handle Outliers
# 4.1 Identify outliers using IQR
Q1 = df['numeric_column'].quantile(0.25)
Q3 = df['numeric_column'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[((df['numeric_column'] < (Q1 - 1.5 * IQR)) | (df['numeric_column'] > (Q3 + 1.5 * IQR)))]

# 4.2 Remove outliers
df_cleaned = df[~((df['numeric_column'] < (Q1 - 1.5 * IQR)) | (df['numeric_column'] > (Q3 + 1.5 * IQR)))]

# 5. Convert Data Types
df['date_column'] = pd.to_datetime(df['date_column'])  # Convert to datetime
df['categorical_column'] = df['categorical_column'].astype('category')  # Convert to categorical

# 6. Handle Text Data (if applicable)
# 6.1 Remove leading/trailing whitespaces
df['text_column'] = df['text_column'].str.strip()

# 6.2 Remove special characters
df['text_column'] = df['text_column'].str.replace('[^a-zA-Z0-9 ]', '')

# 7. Feature Engineering
# 7.1 Creating new features
df['new_feature'] = df['numeric_column1'] * df['numeric_column2']

# 7.2 Binning
df['age_bin'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'])

# 8. EDA (Exploratory Data Analysis)
# 8.1 Univariate Analysis
sns.histplot(df['numeric_column'])
plt.title('Histogram of Numeric Column')
plt.show()

sns.boxplot(df['numeric_column'])
plt.title('Boxplot of Numeric Column')
plt.show()

# 8.2 Bivariate Analysis
sns.scatterplot(x='numeric_column1', y='numeric_column2', data=df)
plt.title('Scatter Plot between Numeric Columns')
plt.show()

sns.barplot(x='categorical_column', y='numeric_column', data=df)
plt.title('Bar Plot of Categorical vs Numeric')
plt.show()

# 8.3 Correlation Matrix
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 8.4 Pairplot
sns.pairplot(df, hue='categorical_column')
plt.title('Pairplot')
plt.show()

# 8.5 Multivariate Analysis (using PairGrid or similar)
g = sns.PairGrid(df, hue="categorical_column")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()

# 9. Data Transformation (if necessary)
# 9.1 Normalization
df['normalized_column'] = (df['numeric_column'] - df['numeric_column'].min()) / (df['numeric_column'].max() - df['numeric_column'].min())

# 9.2 Standardization
df['standardized_column'] = (df['numeric_column'] - df['numeric_column'].mean()) / df['numeric_column'].std()

# 10. Save the Cleaned Data
df_cleaned.to_csv('cleaned_dataset.csv', index=False)

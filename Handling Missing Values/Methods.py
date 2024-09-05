import pandas as pd
from sklearn.impute import SimpleImputer

# Load dataset (replace 'your_dataset.csv' with your actual file)
df = pd.read_csv('your_dataset.csv')

# 1. Checking for missing values
print("Missing Values in Each Column:\n", df.isnull().sum())

# 2. Drop rows with missing values
df_dropped_rows = df.dropna()
print("\nData after dropping rows with missing values:\n", df_dropped_rows.head())

# 3. Drop columns with missing values
df_dropped_columns = df.dropna(axis=1)
print("\nData after dropping columns with missing values:\n", df_dropped_columns.head())

# 4. Fill missing values with Mean (for numeric columns)
mean_imputer = SimpleImputer(strategy='mean')
df['numeric_column_mean'] = mean_imputer.fit_transform(df[['numeric_column']])
print("\nData after filling missing values with mean:\n", df[['numeric_column', 'numeric_column_mean']].head())

# 5. Fill missing values with Median (for numeric columns)
median_imputer = SimpleImputer(strategy='median')
df['numeric_column_median'] = median_imputer.fit_transform(df[['numeric_column']])
print("\nData after filling missing values with median:\n", df[['numeric_column', 'numeric_column_median']].head())

# 6. Fill missing values with Mode (for categorical columns)
mode_imputer = SimpleImputer(strategy='most_frequent')
df['categorical_column_mode'] = mode_imputer.fit_transform(df[['categorical_column']])
print("\nData after filling missing values with mode:\n", df[['categorical_column', 'categorical_column_mode']].head())

# 7. Fill missing values with a constant value (e.g., 0 or "Unknown")
constant_imputer = SimpleImputer(strategy='constant', fill_value=0)
df['numeric_column_filled_constant'] = constant_imputer.fit_transform(df[['numeric_column']])
print("\nData after filling missing values with constant value 0:\n", df[['numeric_column', 'numeric_column_filled_constant']].head())

# 8. Forward Fill (using the last available value)
df['numeric_column_ffill'] = df['numeric_column'].fillna(method='ffill')
print("\nData after forward filling:\n", df[['numeric_column', 'numeric_column_ffill']].head())

# 9. Backward Fill (using the next available value)
df['numeric_column_bfill'] = df['numeric_column'].fillna(method='bfill')
print("\nData after backward filling:\n", df[['numeric_column', 'numeric_column_bfill']].head())

# 10. Interpolation (linear interpolation for numeric columns)
df['numeric_column_interpolated'] = df['numeric_column'].interpolate(method='linear')
print("\nData after linear interpolation:\n", df[['numeric_column', 'numeric_column_interpolated']].head())

# 11. Fill missing values with a rolling window average (moving average)
df['numeric_column_rolling'] = df['numeric_column'].fillna(df['numeric_column'].rolling(window=3, min_periods=1).mean())
print("\nData after filling with rolling window average:\n", df[['numeric_column', 'numeric_column_rolling']].head())

# 12. Fill missing values based on conditions (custom approach)
df['numeric_column_custom'] = df['numeric_column'].fillna(df['numeric_column'].mean() if df['numeric_column'].isnull().sum() > 10 else df['numeric_column'].median())
print("\nData after filling based on a custom condition:\n", df[['numeric_column', 'numeric_column_custom']].head())

# 13. Using sklearn's SimpleImputer for advanced imputation (mean, median, mode)
imputer = SimpleImputer(strategy='mean')
df['numeric_column_sklearn'] = imputer.fit_transform(df[['numeric_column']])
print("\nData after filling missing values with sklearn SimpleImputer:\n", df[['numeric_column', 'numeric_column_sklearn']].head())

# 14. Removing entire entities (e.g., rows or columns with more than X% missing values)
threshold = 0.5  # Remove columns with more than 50% missing values
df_removed_entities = df.loc[:, df.isnull().mean() < threshold]
print("\nData after removing columns with more than 50% missing values:\n", df_removed_entities.head())

# 15. Summary of missing values handling
print("\nFinal dataset with cleaned missing values:\n", df.head())

# Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)








'''
Explanation of Techniques
Drop Rows with Missing Values: Removes rows containing any missing data, but this can result in data loss if many rows are dropped.
Drop Columns with Missing Values: Removes entire columns that have missing values.
Fill with Mean: Fills missing numeric values with the column's mean.
Fill with Median: Fills missing numeric values with the column's median.
Fill with Mode: Fills missing categorical values with the most frequent value (mode).
Fill with a Constant: Replaces missing values with a fixed value (e.g., 0 or "Unknown").
Forward Fill: Propagates the last valid observation forward to fill missing data.
Backward Fill: Propagates the next valid observation backward to fill missing data.
Interpolation: Estimates missing values using linear interpolation.
Rolling Window Average: Fills missing data with the average of values in a rolling window (e.g., over 3 rows).
Conditional Filling: Custom logic for filling missing values based on certain conditions.
sklearn's SimpleImputer: A flexible method to handle missing data using various strategies like mean, median, mode, or constant filling.
Remove Entities: Removes entire rows or columns if the percentage of missing data exceeds a specified threshold.
'''

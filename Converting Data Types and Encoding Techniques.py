import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer

# Sample dataset
data = {
    'age': [25, 35, 45, 55, np.nan],
    'salary': ['low', 'medium', 'high', 'medium', 'low'],
    'experience': [1, 5, 10, 15, 20],
    'gender': ['male', 'female', 'female', 'male', 'female'],
    'purchased': ['no', 'yes', 'no', 'yes', 'no']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. Convert numeric columns to integer (handling missing values)
df['age'] = df['age'].fillna(df['age'].mean()).astype(int)
print("\nDataFrame after converting 'age' to integer:\n", df)

# 2. Convert categorical to numeric using LabelEncoder (for binary categorical variables)
label_encoder = LabelEncoder()
df['purchased_encoded'] = label_encoder.fit_transform(df['purchased'])
print("\nDataFrame after Label Encoding 'purchased':\n", df)

# 3. Convert categorical to numeric using OneHotEncoder (for nominal categorical variables)
one_hot_encoder = OneHotEncoder(sparse=False)
encoded_gender = one_hot_encoder.fit_transform(df[['gender']])
df_gender_encoded = pd.DataFrame(encoded_gender, columns=one_hot_encoder.get_feature_names_out(['gender']))
df = pd.concat([df, df_gender_encoded], axis=1).drop('gender', axis=1)
print("\nDataFrame after OneHotEncoding 'gender':\n", df)

# 4. Ordinal Encoding (for ordinal categorical variables like 'salary')
ordinal_encoder = OrdinalEncoder(categories=[['low', 'medium', 'high']])
df['salary_encoded'] = ordinal_encoder.fit_transform(df[['salary']])
print("\nDataFrame after Ordinal Encoding 'salary':\n", df)

# 5. Convert numeric columns to float
df['experience_float'] = df['experience'].astype(float)
print("\nDataFrame after converting 'experience' to float:\n", df)

# 6. Scaling data using StandardScaler (Z-score normalization)
scaler = StandardScaler()
df['experience_scaled'] = scaler.fit_transform(df[['experience']])
print("\nDataFrame after Standard Scaling 'experience':\n", df)

# 7. Min-Max Scaling (normalize to a range [0,1])
min_max_scaler = MinMaxScaler()
df['experience_minmax'] = min_max_scaler.fit_transform(df[['experience']])
print("\nDataFrame after Min-Max Scaling 'experience':\n", df)

# 8. Convert Boolean-like column (Yes/No) to Binary (1/0)
df['purchased_binary'] = df['purchased'].map({'yes': 1, 'no': 0})
print("\nDataFrame after converting 'purchased' to binary 1/0:\n", df)

# 9. Casting column to categorical type (Categorical data type)
df['salary'] = pd.Categorical(df['salary'], categories=['low', 'medium', 'high'], ordered=True)
print("\nDataFrame after converting 'salary' to categorical:\n", df)

# 10. Changing entire DataFrame column types using 'astype()'
df = df.astype({'age': 'int32', 'experience': 'int32'})
print("\nDataFrame after changing multiple column types:\n", df.dtypes)

# 11. Backward and forward filling for missing values (handling before converting types)
df['age_ffill'] = df['age'].fillna(method='ffill')
df['age_bfill'] = df['age'].fillna(method='bfill')
print("\nDataFrame after forward/backward filling 'age':\n", df)

# 12. Combining transformations into a pipeline for automatic processing
column_transformer = ColumnTransformer(transformers=[
    ('ohe_gender', OneHotEncoder(), ['gender']),
    ('ordinal_salary', OrdinalEncoder(categories=[['low', 'medium', 'high']]), ['salary']),
    ('scaling_experience', StandardScaler(), ['experience'])
], remainder='passthrough')

transformed_data = column_transformer.fit_transform(df)
print("\nTransformed DataFrame using ColumnTransformer pipeline:\n", transformed_data)

# Save the cleaned and transformed dataset
df.to_csv('transformed_dataset.csv', index=False)







'''
Explanation of Techniques
Convert Numeric Columns to Integer: Fills missing values (if any) and converts the column to integer type.
Label Encoding: Converts binary categorical columns into numerical values (e.g., 'yes' to 1 and 'no' to 0).
One-Hot Encoding: Converts nominal categorical variables into multiple binary columns (e.g., 'male', 'female' into two columns).
Ordinal Encoding: Converts ordinal categorical variables into numbers (e.g., 'low', 'medium', 'high' as 0, 1, 2).
Convert Numeric to Float: Casts numeric columns to float data types for better precision.
Standard Scaling: Normalizes numeric columns by converting them to z-scores (mean 0, standard deviation 1).
Min-Max Scaling: Normalizes numeric columns into a range, typically [0, 1].
Map Boolean-like Columns: Converts binary categorical variables (like 'yes'/'no') into 1 and 0.
Categorical Data Type: Converts a column into a categorical data type for optimized storage and easier manipulation.
Using astype() for Bulk Conversions: Converts multiple columns' data types at once using the astype() method.
Forward and Backward Filling: Fills missing values by propagating the last or next valid observation forward or backward.
Pipeline Using ColumnTransformer: Automatically processes multiple transformation steps (like OneHotEncoding, Ordinal Encoding, and Scaling) in a single call.
Summary of Methods to Convert Data Types
astype(): General-purpose method to convert column types (e.g., int, float).
Label Encoding: Use LabelEncoder for binary categorical columns.
One-Hot Encoding: Use OneHotEncoder for nominal categorical columns.
Ordinal Encoding: Use OrdinalEncoder for ordinal categorical columns.
Scaling: Use StandardScaler or MinMaxScaler for normalizing numeric data.
Mapping Boolean Columns: Use map() for direct binary conversion (e.g., Yes/No to 1/0).
pd.Categorical: Optimize columns as categorical for storage and efficiency.
'''

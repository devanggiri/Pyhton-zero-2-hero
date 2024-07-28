import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': ['a', 'b', 'c', 'd']
})

print("Original DataFrame:\n", df)

# Access a column
column_a = df['A']
print("\nAccess column 'A':\n", column_a.tolist())

# Access multiple columns
multiple_columns = df[['A', 'C']]
print("\nAccess columns 'A' and 'C':\n", multiple_columns)

# Access a row by label
row_0 = df.loc[0]
print("\nAccess row 0 by label:\n", row_0)

# Access multiple rows by label
rows_0_2 = df.loc[[0, 2]]
print("\nAccess rows 0 and 2 by label:\n", rows_0_2)

# Access a row by position
row_0_by_pos = df.iloc[0]
print("\nAccess row 0 by position:\n", row_0_by_pos)

# Access multiple rows by position
rows_0_2_by_pos = df.iloc[[0, 2]]
print("\nAccess rows 0 and 2 by position:\n", rows_0_2_by_pos)

# Access a range of rows by position
range_of_rows = df.iloc[1:3]
print("\nAccess rows 1 to 2 by position:\n", range_of_rows)

# Add a new column
df['D'] = [9, 10, 11, 12]
print("\nAdd column 'D':\n", df)

# Remove a column
df_dropped = df.drop(columns=['D'])
print("\nDrop column 'D':\n", df_dropped)

# Update a column
df['A'] = [10, 20, 30, 40]
print("\nUpdate column 'A':\n", df)

# Add a new row
df.loc[4] = [50, 60, 'e', 70]
print("\nAdd row:\n", df)

# Remove a row
df_dropped_row = df.drop(index=4)
print("\nDrop row 4:\n", df_dropped_row)

# Filter rows by condition
filtered_rows = df[df['A'] > 20]
print("\nFilter rows where 'A' > 20:\n", filtered_rows)

# Set a new index
df_indexed = df.set_index('C')
print("\nSet 'C' as new index:\n", df_indexed)

# Reset index
df_reset_index = df_indexed.reset_index()
print("\nReset index:\n", df_reset_index)

# Sort by column
df_sorted = df.sort_values(by='B')
print("\nSort by column 'B':\n", df_sorted)

# Get a summary of the DataFrame
summary = df.describe()
print("\nSummary:\n", summary)

# Get the shape of the DataFrame
shape = df.shape
print("\nShape of DataFrame:", shape)

# Transpose the DataFrame
transposed = df.T
print("\nTranspose:\n", transposed)

# Check for null values
null_values = df.isnull()
print("\nCheck for null values:\n", null_values)

# Fill null values
df_with_nulls = df.copy()
df_with_nulls.loc[0, 'A'] = None
filled_df = df_with_nulls.fillna(0)
print("\nFill null values:\n", filled_df)

# Drop null values
dropped_nulls = df_with_nulls.dropna()
print("\nDrop rows with null values:\n", dropped_nulls)

# Group by a column and get mean
grouped = df.groupby('C').mean()
print("\nGroup by 'C' and get mean:\n", grouped)

# Merge two DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})
merged = pd.merge(df1, df2, on='key', how='inner')
print("\nMerge two DataFrames on 'key':\n", merged)

# Concatenate two DataFrames
concatenated = pd.concat([df1, df2], axis=0)
print("\nConcatenate two DataFrames:\n", concatenated)

# Pivot the DataFrame
df_pivot = df.pivot(index='A', columns='C', values='B')
print("\nPivot DataFrame:\n", df_pivot)

# Melt the DataFrame
df_melted = pd.melt(df, id_vars=['A'], value_vars=['B', 'C', 'D'])
print("\nMelt DataFrame:\n", df_melted)

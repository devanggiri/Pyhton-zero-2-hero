import pandas as pd

# Create a Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Access a value by label
value_by_label = s['a']
print("s['a']:", value_by_label)

# Access values by list of labels
values_by_labels = s[['a', 'c', 'e']]
print("s[['a', 'c', 'e']]:", values_by_labels.tolist())

# Access a value by position
value_by_position = s.iloc[1]
print("s.iloc[1]:", value_by_position)

# Access values by list of positions
values_by_positions = s.iloc[[1, 3, 4]]
print("s.iloc[[1, 3, 4]]:", values_by_positions.tolist())

# Access a range of values by position
range_of_values = s.iloc[1:4]
print("s.iloc[1:4]:", range_of_values.tolist())

# Add a new element
s['f'] = 6
print("Add 'f': 6:", s.tolist())

# Remove an element
s = s.drop('b')
print("drop('b'):", s.tolist())

# Update an element
s['a'] = 10
print("Update 'a': 10:", s.tolist())

# Check if an element exists
contains_label = 'c' in s
print("'c' in s:", contains_label)

# Get the length of the Series
length_of_series = len(s)
print("len(s):", length_of_series)

# Get the index of the Series
index_of_series = s.index
print("index:", index_of_series.tolist())

# Get the values of the Series
values_of_series = s.values
print("values:", values_of_series.tolist())

# Apply a function to each element
squared_series = s.apply(lambda x: x**2)
print("apply(lambda x: x**2):", squared_series.tolist())

# Filter the Series
filtered_series = s[s > 3]
print("s[s > 3]:", filtered_series.tolist())

# Series arithmetic operations
added_series = s + 2
print("s + 2:", added_series.tolist())

multiplied_series = s * 2
print("s * 2:", multiplied_series.tolist())

# Get the sum of the Series
sum_of_series = s.sum()
print("sum():", sum_of_series)

# Get the mean of the Series
mean_of_series = s.mean()
print("mean():", mean_of_series)

# Get the maximum value in the Series
max_value = s.max()
print("max():", max_value)

# Get the minimum value in the Series
min_value = s.min()
print("min():", min_value)

# Sort the Series by index
sorted_by_index = s.sort_index()
print("sort_index():", sorted_by_index.tolist())

# Sort the Series by values
sorted_by_values = s.sort_values()
print("sort_values():", sorted_by_values.tolist())

# Get the unique values in the Series
unique_values = s.unique()
print("unique():", unique_values.tolist())

# Get the value counts in the Series
value_counts = s.value_counts()
print("value_counts():", value_counts.tolist())

# Convert Series to a list
series_to_list = s.tolist()
print("tolist():", series_to_list)

# Convert Series to a dictionary
series_to_dict = s.to_dict()
print("to_dict():", series_to_dict)

# Convert Series to a DataFrame
series_to_dataframe = s.to_frame()
print("to_frame():\n", series_to_dataframe)

# Copy the Series
copied_series = s.copy()
print("copy():", copied_series.tolist())

# Clear all elements from the Series
cleared_series = s.drop(s.index)
print("clear():", cleared_series.tolist())

# Create a new Series for demonstration of other operations
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Get the first element of the Series
first_element = s.head(1)
print("head(1):", first_element.tolist())

# Get the last element of the Series
last_element = s.tail(1)
print("tail(1):", last_element.tolist())

# Get the description of the Series
description = s.describe()
print("describe():\n", description)

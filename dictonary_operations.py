# Original dictionary
d = {'a': 1, 'b': 2, 'c': 3}

# Add a new key-value pair
d['d'] = 4
print("Add 'd': 4:", d)

# Update the value of an existing key
d['a'] = 10
print("Update 'a': 10:", d)

# Remove a key-value pair using del
del d['b']
print("del 'b':", d)

# Remove a key-value pair using pop
popped_value = d.pop('c')
print("pop('c'):", popped_value, "; dictionary:", d)

# Remove and return a (key, value) pair using popitem
popped_item = d.popitem()
print("popitem():", popped_item, "; dictionary:", d)

# Check if a key is in the dictionary
contains_key = 'a' in d
print("'a' in dictionary:", contains_key)

# Get the value of a key
value_of_key = d.get('a')
print("get('a'):", value_of_key)

# Get the value of a key with a default if key does not exist
value_of_nonexistent_key = d.get('e', 'default_value')
print("get('e', 'default_value'):", value_of_nonexistent_key)

# Set default value if key does not exist
default_value = d.setdefault('e', 5)
print("setdefault('e', 5):", default_value, "; dictionary:", d)

# Update dictionary with another dictionary
d.update({'f': 6, 'g': 7})
print("update({'f': 6, 'g': 7}):", d)

# Get all keys in the dictionary
keys = d.keys()
print("keys():", list(keys))

# Get all values in the dictionary
values = d.values()
print("values():", list(values))

# Get all key-value pairs in the dictionary
items = d.items()
print("items():", list(items))

# Copy the dictionary
copied_dict = d.copy()
print("copy():", copied_dict)

# Clear all key-value pairs from the dictionary
d.clear()
print("clear():", d)

# Create a new dictionary for demonstration of other operations
d = {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension to create a new dictionary
squared_dict = {k: v**2 for k, v in d.items()}
print("dictionary comprehension {k: v**2 for k, v in d.items()}:", squared_dict)

# Merge two dictionaries (Python 3.9+)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged_dict = d1 | d2
print("merged_dict d1 | d2:", merged_dict)

# Using dict constructor to create a dictionary
constructed_dict = dict([('a', 1), ('b', 2)])
print("dict([('a', 1), ('b', 2)]):", constructed_dict)

# Create a dictionary with fromkeys method
keys = ['a', 'b', 'c']
fromkeys_dict = dict.fromkeys(keys, 0)
print("fromkeys(['a', 'b', 'c'], 0):", fromkeys_dict)

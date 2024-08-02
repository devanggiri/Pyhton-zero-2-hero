# Create a dictionary
hashmap = {'a': 1, 'b': 2, 'c': 3}
print("Original hashmap:", hashmap)

# Access value by key
value_a = hashmap['a']
print("\nAccess value by key 'a':", value_a)

# Add a new key-value pair
hashmap['d'] = 4
print("\nAfter adding a new key-value pair ('d': 4):", hashmap)

# Update the value for an existing key
hashmap['b'] = 20
print("\nAfter updating the value for key 'b':", hashmap)

# Remove a key-value pair
removed_value = hashmap.pop('c')
print("\nAfter removing key 'c':", hashmap)
print("Removed value:", removed_value)

# Get the value for a key with a default
value_e = hashmap.get('e', 'Not found')
print("\nGet the value for key 'e' with a default:", value_e)

# Check if a key exists in the dictionary
key_exists = 'a' in hashmap
print("\nCheck if key 'a' exists in the hashmap:", key_exists)

# Iterate over keys
print("\nIterate over keys:")
for key in hashmap.keys():
    print(key, end=" ")
print()

# Iterate over values
print("\nIterate over values:")
for value in hashmap.values():
    print(value, end=" ")
print()

# Iterate over key-value pairs
print("\nIterate over key-value pairs:")
for key, value in hashmap.items():
    print(f"{key}: {value}")

# Clear the dictionary
hashmap.clear()
print("\nAfter clearing the hashmap:", hashmap)

# Recreate dictionary for further operations
hashmap = {'a': 1, 'b': 2, 'c': 3}
print("\nRecreated hashmap:", hashmap)

# Copy a dictionary
hashmap_copy = hashmap.copy()
print("\nCopy of the hashmap:", hashmap_copy)

# Update a dictionary with another dictionary
hashmap.update({'d': 4, 'e': 5})
print("\nAfter updating hashmap with another dictionary:", hashmap)

# Using dictionary comprehension
squared_values = {k: v**2 for k, v in hashmap.items()}
print("\nDictionary with squared values:", squared_values)

# Length of the dictionary
length = len(hashmap)
print("\nLength of the hashmap:", length)

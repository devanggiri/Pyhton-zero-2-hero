import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Append an element to the array
arr.append(6)
print("append(6):", arr.tolist())

# Extend the array by appending elements from another array
arr.extend([7, 8, 9])
print("extend([7, 8, 9]):", arr.tolist())

# Insert an element at a specific position
arr.insert(3, 10)
print("insert(3, 10):", arr.tolist())

# Remove the first occurrence of an element
arr.remove(10)
print("remove(10):", arr.tolist())

# Pop an element from the array (without index pops last element)
popped_element = arr.pop()
print("pop():", popped_element, "; array:", arr.tolist())

# Pop an element from a specific position
popped_element_at_index = arr.pop(3)
print("pop(3):", popped_element_at_index, "; array:", arr.tolist())

# Find the index of the first occurrence of an element
index_of_element = arr.index(4)
print("index(4):", index_of_element)

# Count the occurrences of an element in the array
count_of_element = arr.count(3)
print("count(3):", count_of_element)

# Reverse the order of elements in the array
arr.reverse()
print("reverse():", arr.tolist())

# Convert the array to a list
list_from_array = arr.tolist()
print("tolist():", list_from_array)

# Get the length of the array
length_of_array = len(arr)
print("len(arr):", length_of_array)

# Get the buffer information of the array
buffer_info = arr.buffer_info()
print("buffer_info():", buffer_info)

# Get the type code of the array
type_code = arr.typecode
print("typecode:", type_code)

# Slice the array (from index 1 to 3)
sliced_array = arr[1:4]
print("sliced_array[1:4]:", sliced_array.tolist())

# Array comprehension to create a new array
squared_array = array.array('i', (x**2 for x in arr))
print("array comprehension (x**2 for x in arr):", squared_array.tolist())

# Create a copy of the array
copied_array = arr[:]
print("copy():", copied_array.tolist())

# Clear all elements from the array
arr.clear()
print("clear():", arr.tolist())

# Create a new array for demonstration of other operations
arr = array.array('i', [1, 2, 3, 4, 5])

# Concatenate two arrays
arr2 = array.array('i', [6, 7, 8])
concatenated_array = arr + arr2
print("concatenated_array:", concatenated_array.tolist())

# Multiply the array
multiplied_array = arr * 3
print("multiplied_array (arr * 3):", multiplied_array.tolist())

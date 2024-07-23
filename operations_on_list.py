# Original list
lst = [1, 2, 3, 4, 5]

# Append an element to the list
lst.append(6)
print("append(6):", lst)

# Extend the list by appending elements from another list
lst.extend([7, 8, 9])
print("extend([7, 8, 9]):", lst)

# Insert an element at a specific position
lst.insert(3, 10)
print("insert(3, 10):", lst)

# Remove the first occurrence of an element
lst.remove(10)
print("remove(10):", lst)

# Pop an element from the list (without index pops last element)
popped_element = lst.pop()
print("pop():", popped_element, "; list:", lst)

# Pop an element from a specific position
popped_element_at_index = lst.pop(3)
print("pop(3):", popped_element_at_index, "; list:", lst)

# Find the index of the first occurrence of an element
index_of_element = lst.index(4)
print("index(4):", index_of_element)

# Count the occurrences of an element in the list
count_of_element = lst.count(3)
print("count(3):", count_of_element)

# Sort the list in ascending order
lst.sort()
print("sort():", lst)

# Sort the list in descending order
lst.sort(reverse=True)
print("sort(reverse=True):", lst)

# Reverse the order of elements in the list
lst.reverse()
print("reverse():", lst)

# Copy the list
copied_list = lst.copy()
print("copy():", copied_list)

# Clear all elements from the list
lst.clear()
print("clear():", lst)

# Create a new list for demonstration of other operations
lst = [1, 2, 3, 4, 5]

# Slice the list (from index 1 to 3)
sliced_list = lst[1:4]
print("sliced_list[1:4]:", sliced_list)

# List comprehension to create a new list
squared_list = [x**2 for x in lst]
print("list comprehension [x**2 for x in lst]:", squared_list)

# Check if an element is in the list
contains_element = 3 in lst
print("3 in lst:", contains_element)

# Get the length of the list
length_of_list = len(lst)
print("len(lst):", length_of_list)

# Get the maximum value from the list
max_value = max(lst)
print("max(lst):", max_value)

# Get the minimum value from the list
min_value = min(lst)
print("min(lst):", min_value)

# Sum of all elements in the list
sum_of_elements = sum(lst)
print("sum(lst):", sum_of_elements)

# Create a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
print("list_of_lists:", list_of_lists)

# Flatten a list of lists using list comprehension
flattened_list = [item for sublist in list_of_lists for item in sublist]
print("flattened_list:", flattened_list)

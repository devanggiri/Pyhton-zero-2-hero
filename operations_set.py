# Create a set
set1 = {1, 2, 3, 4, 5}
print("Original set1:", set1)

# Add an element
set1.add(6)
print("\nAfter adding 6:", set1)

# Remove an element
set1.remove(3)  # Raises KeyError if 3 is not in the set
print("\nAfter removing 3:", set1)

# Discard an element
set1.discard(2)  # Does not raise an error if 2 is not in the set
print("\nAfter discarding 2:", set1)

# Pop an element (removes and returns an arbitrary element)
popped_element = set1.pop()
print("\nAfter popping an element:", set1)
print("Popped element:", popped_element)

# Clear the set
set1.clear()
print("\nAfter clearing set1:", set1)

# Create another set
set2 = {3, 4, 5, 6, 7}
print("\nOriginal set2:", set2)

# Union of sets
set3 = {1, 2, 3}
union_set = set3.union(set2)
print("\nUnion of set3 and set2:", union_set)

# Intersection of sets
intersection_set = set3.intersection(set2)
print("\nIntersection of set3 and set2:", intersection_set)

# Difference of sets
difference_set = set3.difference(set2)
print("\nDifference of set3 and set2:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set3.symmetric_difference(set2)
print("\nSymmetric difference of set3 and set2:", symmetric_difference_set)

# Check if a set is a subset of another set
is_subset = set3.issubset(set2)
print("\nIs set3 a subset of set2?", is_subset)

# Check if a set is a superset of another set
is_superset = set2.issuperset(set3)
print("\nIs set2 a superset of set3?", is_superset)

# Check if two sets are disjoint
are_disjoint = set3.isdisjoint(set2)
print("\nAre set3 and set2 disjoint?", are_disjoint)

# Copy a set
set4 = set2.copy()
print("\nCopy of set2 (set4):", set4)

# Update a set with another set
set4.update(set3)
print("\nAfter updating set4 with set3:", set4)

# Intersection update
set4.intersection_update(set2)
print("\nAfter intersection update of set4 with set2:", set4)

# Difference update
set4.difference_update(set3)
print("\nAfter difference update of set4 with set3:", set4)

# Symmetric difference update
set4.symmetric_difference_update(set2)
print("\nAfter symmetric difference update of set4 with set2:", set4)

# Create sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {1, 2}
print("Original sets:")
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

# add()
set1.add(4)
print("\nAfter adding 4 to set1:", set1)

# clear()
set1.clear()
print("\nAfter clearing set1:", set1)

# copy()
set1 = set2.copy()
print("\nCopy of set2 to set1:", set1)

# difference()
diff_set = set2.difference(set3)
print("\nDifference between set2 and set3:", diff_set)

# difference_update()
set1.difference_update(set3)
print("\nAfter difference update of set1 with set3:", set1)

# discard()
set1.discard(4)
print("\nAfter discarding 4 from set1 (no error if not present):", set1)

# intersection()
intersection_set = set2.intersection(set3)
print("\nIntersection of set2 and set3:", intersection_set)

# intersection_update()
set2.intersection_update(set3)
print("\nAfter intersection update of set2 with set3:", set2)

# isdisjoint()
are_disjoint = set1.isdisjoint(set3)
print("\nAre set1 and set3 disjoint?", are_disjoint)

# issubset()
is_subset = set3.issubset(set2)
print("\nIs set3 a subset of set2?", is_subset)

# <= operator for issubset
is_subset_operator = set3 <= set2
print("\nIs set3 a subset of set2 (using <=)?", is_subset_operator)

# < operator for proper subset
is_proper_subset = set3 < set2
print("\nIs set3 a proper subset of set2 (using <)?", is_proper_subset)

# issuperset()
is_superset = set2.issuperset(set3)
print("\nIs set2 a superset of set3?", is_superset)

# >= operator for issuperset
is_superset_operator = set2 >= set3
print("\nIs set2 a superset of set3 (using >=)?", is_superset_operator)

# > operator for proper superset
is_proper_superset = set2 > set3
print("\nIs set2 a proper superset of set3 (using >)?", is_proper_superset)

# pop()
popped_element = set1.pop()
print("\nAfter popping an element from set1:", set1)
print("Popped element:", popped_element)

# remove()
set1.add(4)
set1.remove(4)
print("\nAfter removing 4 from set1:", set1)

# symmetric_difference()
symmetric_diff_set = set1.symmetric_difference(set3)
print("\nSymmetric difference between set1 and set3:", symmetric_diff_set)

# symmetric_difference_update()
set1.symmetric_difference_update(set3)
print("\nAfter symmetric difference update of set1 with set3:", set1)

# union()
union_set = set1.union(set2)
print("\nUnion of set1 and set2:", union_set)

# update()
set1.update(set2)
print("\nAfter updating set1 with set2:", set1)

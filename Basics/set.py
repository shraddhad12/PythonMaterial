# Initialize sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Add and Remove
set_a.add(6)
set_a.remove(1)

# Union and Update
union_set = set_a.union(set_b)  # {2, 3, 4, 5, 6}
set_a.update(set_b)  # set_a is now {2, 3, 4, 5, 6}

# Intersection and Intersection Update
intersection_set = set_a.intersection(set_b)  # {3, 4, 5}
set_a.intersection_update(set_b)  # set_a is now {3, 4, 5}

# Difference and Difference Update
difference_set = set_b.difference(set_a)  # {6}
set_b.difference_update(set_a)  # set_b is now {6}

# Symmetric Difference and Symmetric Difference Update
sym_diff_set = set_a.symmetric_difference(set_b)  # {2, 6}
set_a.symmetric_difference_update(set_b)  # set_a is now {2, 6}

print(f"Union Set: {union_set}")
print(f"Intersection Set: {intersection_set}")
print(f"Difference Set: {difference_set}")
print(f"Symmetric Difference Set: {sym_diff_set}")
print(f"Set A after operations: {set_a}")
print(f"Set B after operations: {set_b}")
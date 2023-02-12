# Set: Sets are very similar to dictionaries. They store unordered collections of data and every item is unique. 
# Items cannot be modified nor accessed by the index. Use sets when you want to store a collection you know you won't need to modify.

sets = {1, 2, 3, 4, 5}

print(type(sets))
print(sets)

# Here are some ways you can use set for:

# Union() - creates a new set that contains elements from different sets.
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_set = set_a.union(set_b)
print(union_set) # prints {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection() - creates a new set that contains the elements that are common to both sets.
intersection_set = set_a.intersection(set_b)
print(intersection_set) # prints {4, 5}

# Difference() - creates a new set that contains the elements that are in set_a but not in set_b.
difference_set = set_a.difference(set_b)
print(difference_set) # prints {1, 2, 3}

# Eliminate duplicates from a list
names = ['Alice', 'Bob', 'Charlie', 'Alice', 'Dave']
unique_names = set(names)
print(unique_names)  # prints {'Alice', 'Bob', 'Charlie', 'Dave'}
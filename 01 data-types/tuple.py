# Tuples: Ordered collection of values or items. It is similar to the lists but, unlike those, tuples cannot be modified once they are created.
tuple = ("one", "two", "three", 4, 5)

# Use type() to get the data type and print it
print(type(tuple))

# Access to an specific item of the list and print it
print(tuple[2])


# Trying to modify an item of the tuple will result in an error.
#tuple[2] = 3
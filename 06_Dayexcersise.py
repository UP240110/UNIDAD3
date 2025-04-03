#Day 6
# Excersise 1
# Declare a tuple with three values of your choice.

my_tuple = ('one', 'two', 'three')
print(my_tuple)

# Excersise 2
# Assign the first value to a variable name, the second value to a variable age and the third value to a variable address.

name, age, address = my_tuple
print(name)
print(age)
print(address)

# Excersise 3

# Declare a tuple with different data types: 'a', 1, 2.0

my_tuple = ('a', 1, 2.0)
print(my_tuple)

# Excersise 4
# Find the length of your tuple

print(len(my_tuple))

# Excersise 5
# Get the first item in the tuple

print(my_tuple[0])

# Excersise 6
# Get the second item in the tuple

print(my_tuple[1])

# Excersise 7
# Get the last item in the tuple

print(my_tuple[-1])

# Excersise 8
# Use slicing to get the first two items in the tuple

print(my_tuple[0:2])

# Excersise 9
# Use slicing to get the last two items in the tuple

print(my_tuple[1:])

# Excersise 10
# Use slicing to get the middle item in the tuple

print(my_tuple[1])

# Excersise 11
# Delete the first item in the tuple

my_tuple = my_tuple[1:]
print(my_tuple)

# Excersise 12
# Delete the last item in the tuple

my_tuple = my_tuple[:-1]
print(my_tuple)

# Excersise 13
# Delete the middle item in the tuple

my_tuple = my_tuple[0:1] + my_tuple[2:]
print(my_tuple)

# Excersise 14
# Delete the whole tuple

del my_tuple
print(my_tuple) # This will raise an error because the tuple has been deleted





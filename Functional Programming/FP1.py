# Using final data structures (immutable list and tuple)
immutable_list = [1, 2, 3, 4, 5]
immutable_tuple = (6, 7, 8, 9, 10)

# Function for mapping: doubling each element
def double(x):
    return x * 2

# Function for filtering: keeping only even numbers
def is_even(x):
    return x % 2 == 0

# Applying map and filter to immutable list
mapped_result = list(map(double, immutable_list))
filtered_result = list(filter(is_even, immutable_list))

# Applying map to immutable tuple
mapped_tuple = tuple(map(double, immutable_tuple))

# Printing results
print("Original List:", immutable_list)
print("Mapped List (doubled):", mapped_result)
print("Filtered List (even numbers):", filtered_result)
print("Mapped Tuple (doubled):", mapped_tuple)


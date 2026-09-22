
# Day 6: Python Lists and Tuples

# 1. Introduction to Lists

# Lists are ordered, mutable collections that allow duplicate values.
my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])
print("Data Type:", type(my_list))


# 2. List Operations

print("\n--- List Operations ---")

numbers = [10, 20, 30, 40]

# Adding elements
numbers.append(50)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.extend([60, 70])
print("After extend:", numbers)

# Removing elements
numbers.remove(15)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

# Updating elements
numbers[0] = 100
print("After updating:", numbers)

# Concatenation
print("Concatenation:", [1, 2] + [3, 4])

# Repetition
print("Repetition:", [1, 2] * 3)

# Membership
print("20 in numbers:", 20 in numbers)

# List slicing
print("Slicing:", numbers[1:4])

# Sorting and reversing
numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)


# 3. List Functions

print("\n--- List Functions ---")

values = [45, 12, 78, 23, 12]

print("Length:", len(values))
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))
print("Sorted:", sorted(values))
print("Count of 12:", values.count(12))
print("Index of 78:", values.index(78))

# Copying a list
copy_list = values.copy()
print("Copied List:", copy_list)

# Clearing a list
copy_list.clear()
print("After clear:", copy_list)


# 4. Introduction to Tuples

# Tuples are ordered, immutable collections that allow duplicate values.
my_tuple = (10, 20, 30, 40, 50)

print("\n--- Introduction to Tuples ---")
print("Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])
print("Data Type:", type(my_tuple))

# Single-element tuple
single_tuple = (10,)
print("Single Element Tuple:", single_tuple)

# Tuple without parentheses
another_tuple = 10, 20, 30
print("Another Tuple:", another_tuple)


# 5. Tuple Operations

print("\n--- Tuple Operations ---")

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print("Concatenation:", t1 + t2)

# Repetition
print("Repetition:", t1 * 2)

# Membership
print("2 in t1:", 2 in t1)

# Indexing
print("First Element:", t1[0])

# Slicing
print("Slicing:", t1[1:])

# Tuple unpacking
a, b, c = t1
print("Unpacked Values:", a, b, c)


# 6. Tuple Functions

print("\n--- Tuple Functions ---")

numbers_tuple = (10, 20, 30, 20, 40)

print("Length:", len(numbers_tuple))
print("Minimum:", min(numbers_tuple))
print("Maximum:", max(numbers_tuple))
print("Sum:", sum(numbers_tuple))
print("Count of 20:", numbers_tuple.count(20))
print("Index of 30:", numbers_tuple.index(30))
print("Sorted:", sorted(numbers_tuple))

# Convert tuple to list
converted_list = list(numbers_tuple)
print("Tuple to List:", converted_list)

# Convert list to tuple
converted_tuple = tuple(converted_list)
print("List to Tuple:", converted_tuple)

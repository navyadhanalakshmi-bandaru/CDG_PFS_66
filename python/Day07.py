
# Day 7: Python Sets and Dictionaries

# 1. Introduction to Sets

# Sets are unordered collections of unique elements.
my_set = {10, 20, 30, 40, 20}

print("Set:", my_set)
print("Data Type:", type(my_set))

# Empty set
empty_set = set()
print("Empty Set:", empty_set)


# 2. Set Operations

print("\n--- Set Operations ---")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Adding elements
s1.add(5)
print("After add:", s1)

s1.update([6, 7])
print("After update:", s1)

# Removing elements
s1.remove(7)
print("After remove:", s1)

s1.discard(10)
print("After discard:", s1)

# Union
print("Union:", s1.union(s2))

# Intersection
print("Intersection:", s1.intersection(s2))

# Difference
print("Difference:", s1.difference(s2))

# Symmetric difference
print("Symmetric Difference:", s1.symmetric_difference(s2))

# Membership
print("3 in s1:", 3 in s1)

# Subset and superset
print("Subset:", {1, 2}.issubset(s1))
print("Superset:", s1.issuperset({1, 2}))

# Disjoint
print("Disjoint:", {10, 11}.isdisjoint(s2))


# 3. Set Functions

print("\n--- Set Functions ---")

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

# Copy
copy_set = numbers.copy()
print("Copied Set:", copy_set)

# Pop removes an arbitrary element
copy_set.pop()
print("After pop:", copy_set)

# Clear
copy_set.clear()
print("After clear:", copy_set)


# 4. Introduction to Dictionaries

# Dictionaries store data as key-value pairs.
student = {
    "name": "Navya",
    "age": 21,
    "course": "Python"
}

print("\n--- Introduction to Dictionaries ---")
print("Dictionary:", student)
print("Data Type:", type(student))
print("Name:", student["name"])
print("Age:", student["age"])


# 5. Dictionary Operations

print("\n--- Dictionary Operations ---")

# Adding a new key-value pair
student["city"] = "Eluru"
print("After adding:", student)

# Updating a value
student["age"] = 22
print("After updating:", student)

# Accessing using get()
print("Course:", student.get("course"))

# Removing a key
student.pop("city")
print("After pop:", student)

# Removing the last inserted pair
student.popitem()
print("After popitem:", student)

# Adding multiple items
student.update({"age": 21, "language": "Python"})
print("After update:", student)

# Membership checks keys
print("name in student:", "name" in student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)


# 6. Dictionary Functions

print("\n--- Dictionary Functions ---")

marks = {
    "Maths": 90,
    "Science": 85,
    "English": 95
}

print("Length:", len(marks))
print("Keys:", marks.keys())
print("Values:", marks.values())
print("Items:", marks.items())

# Get a value safely
print("Maths Marks:", marks.get("Maths"))

# Copy dictionary
copy_dict = marks.copy()
print("Copied Dictionary:", copy_dict)

# Set default value
marks.setdefault("Computer", 100)
print("After setdefault:", marks)

# Clear dictionary
copy_dict.clear()
print("After clear:", copy_dict)

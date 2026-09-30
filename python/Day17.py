# ============================================================
# Day 17: Lambda Functions
# ============================================================
# SubTopics:
# 1. Anonymous Functions
# 2. Lambda Syntax
# 3. Lambda Examples
# 4. Filter
# 5. Map
# 6. Reduce


# ============================================================
# 1. ANONYMOUS FUNCTIONS
# ============================================================

# An anonymous function is a function without a name.
# In Python, anonymous functions are created using lambda.


# Normal function

def square(n):
    return n * n


print("Normal Function:", square(5))


# Anonymous function

square_lambda = lambda n: n * n

print("Lambda Function:", square_lambda(5))


# ============================================================
# 2. LAMBDA SYNTAX
# ============================================================

# Syntax:
#
# lambda arguments: expression
#
# Example:
# lambda x: x * 2


double = lambda x: x * 2

print("Double:", double(10))


# Multiple arguments

add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Three arguments

multiply = lambda a, b, c: a * b * c

print("Multiplication:", multiply(2, 3, 4))


# ============================================================
# 3. LAMBDA EXAMPLES
# ============================================================

# Example 1: Square

square = lambda x: x ** 2

print("Square:", square(6))


# Example 2: Cube

cube = lambda x: x ** 3

print("Cube:", cube(3))


# Example 3: Check even

even = lambda x: x % 2 == 0

print("Is Even:", even(10))


# Example 4: Check odd

odd = lambda x: x % 2 != 0

print("Is Odd:", odd(7))


# Example 5: Find largest of two numbers

largest = lambda a, b: a if a > b else b

print("Largest:", largest(25, 40))


# Example 6: Find smallest of two numbers

smallest = lambda a, b: a if a < b else b

print("Smallest:", smallest(25, 40))


# Example 7: Calculate simple interest

simple_interest = lambda p, r, t: (p * r * t) / 100

print("Simple Interest:", simple_interest(10000, 5, 2))


# ============================================================
# 4. FILTER()
# ============================================================

# filter() is used to select elements from an iterable
# based on a condition.
#
# Syntax:
# filter(function, iterable)


# Example 1: Filter even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# Example 2: Filter odd numbers

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd Numbers:", odd_numbers)


# Example 3: Filter numbers greater than 5

numbers = [2, 5, 7, 10, 3, 8, 12]

greater_than_5 = list(filter(lambda x: x > 5, numbers))

print("Numbers greater than 5:", greater_than_5)


# Example 4: Filter positive numbers

numbers = [-5, 10, -2, 8, -1, 15]

positive_numbers = list(filter(lambda x: x > 0, numbers))

print("Positive Numbers:", positive_numbers)


# Example 5: Filter names starting with A

names = ["Anil", "Rahul", "Arun", "Priya", "Ajay"]

a_names = list(filter(lambda name: name.startswith("A"), names))

print("Names starting with A:", a_names)


# ============================================================
# 5. MAP()
# ============================================================

# map() applies a function to every element of an iterable.
#
# Syntax:
# map(function, iterable)


# Example 1: Find squares

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)


# Example 2: Find cubes

cubes = list(map(lambda x: x ** 3, numbers))

print("Cubes:", cubes)


# Example 3: Double every number

numbers = [10, 20, 30, 40]

double_numbers = list(map(lambda x: x * 2, numbers))

print("Doubled:", double_numbers)


# Example 4: Add 10 to every number

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x + 10, numbers))

print("After adding 10:", result)


# Example 5: Convert names to uppercase

names = ["navya", "rahul", "anil"]

uppercase_names = list(map(lambda name: name.upper(), names))

print("Uppercase Names:", uppercase_names)


# Example 6: Add two lists

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = list(map(lambda a, b: a + b, list1, list2))

print("Added Lists:", result)


# ============================================================
# 6. REDUCE()
# ============================================================

# reduce() repeatedly applies a function to the elements
# and produces a single result.
#
# reduce() is available in the functools module.


from functools import reduce


# Example 1: Sum of numbers

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)


# Example 2: Product of numbers

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)


# Example 3: Find maximum number

numbers = [10, 25, 7, 40, 15]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum:", maximum)


# Example 4: Find minimum number

numbers = [10, 25, 7, 40, 15]

minimum = reduce(lambda a, b: a if a < b else b, numbers)

print("Minimum:", minimum)


# ============================================================
# COMBINING FILTER, MAP AND REDUCE
# ============================================================

# Example:
# Find the sum of squares of even numbers.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squares = map(lambda x: x ** 2, even_numbers)

result = reduce(lambda a, b: a + b, squares)

print("Sum of squares of even numbers:", result)


# ============================================================
# PRACTICE PROBLEMS
# ============================================================

# Problem 1: Find even numbers

numbers = [10, 15, 20, 25, 30, 35]

result = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", result)


# Problem 2: Find numbers greater than 10

numbers = [5, 12, 8, 20, 15, 3]

result = list(filter(lambda x: x > 10, numbers))

print("Greater than 10:", result)


# Problem 3: Find squares of numbers

numbers = [2, 4, 6, 8]

result = list(map(lambda x: x ** 2, numbers))

print("Squares:", result)


# Problem 4: Convert Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(
    map(lambda c: (c * 9 / 5) + 32, celsius)
)

print("Fahrenheit:", fahrenheit)


# Problem 5: Find sum using reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)


# Problem 6: Find product using reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)


# Problem 7: Find sum of even numbers

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

total = reduce(lambda a, b: a + b, even_numbers)

print("Sum of even numbers:", total)


# ============================================================
# END OF DAY 17
# ============================================================
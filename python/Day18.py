# ============================================================
# Day 18: List Comprehensions and Generators
# ============================================================
# SubTopics:
# 1. List Comprehensions
# 2. Nested Comprehensions
# 3. Generators
# 4. Yield Keyword
# 5. Next Keyword
# 6. Difference between Functions & Generators


# ============================================================
# 1. LIST COMPREHENSIONS
# ============================================================

# List comprehension provides a short way to create a list.

# Normal for loop

numbers = []

for i in range(1, 6):
    numbers.append(i)

print("Normal List:", numbers)


# Using list comprehension

numbers = [i for i in range(1, 6)]

print("List Comprehension:", numbers)


# Example 1: Squares

squares = [i ** 2 for i in range(1, 6)]

print("Squares:", squares)


# Example 2: Even numbers

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print("Even Numbers:", even_numbers)


# Example 3: Odd numbers

odd_numbers = [i for i in range(1, 11) if i % 2 != 0]

print("Odd Numbers:", odd_numbers)


# Example 4: Numbers greater than 5

numbers = [2, 5, 7, 10, 3, 8]

result = [i for i in numbers if i > 5]

print("Numbers greater than 5:", result)


# Example 5: Convert strings to uppercase

names = ["navya", "rahul", "anil"]

upper_names = [name.upper() for name in names]

print("Uppercase Names:", upper_names)


# Example 6: Length of each word

words = ["Python", "Java", "SQL"]

lengths = [len(word) for word in words]

print("Lengths:", lengths)


# ============================================================
# 2. NESTED COMPREHENSIONS
# ============================================================

# A list comprehension inside another list comprehension
# is called a nested comprehension.


# Example 1: Create a matrix

matrix = [[j for j in range(1, 4)] for i in range(3)]

print("Matrix:", matrix)


# Example 2: Create a 3 x 3 matrix

matrix = [[0 for j in range(3)] for i in range(3)]

print("3 x 3 Matrix:", matrix)


# Example 3: Flatten a nested list

numbers = [[1, 2], [3, 4], [5, 6]]

result = [num for row in numbers for num in row]

print("Flattened List:", result)


# Example 4: Create multiplication table

table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print("Multiplication Table:")

for row in table:
    print(row)


# Example 5: Even numbers from nested list

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

even_numbers = [
    num
    for row in numbers
    for num in row
    if num % 2 == 0
]

print("Even Numbers:", even_numbers)


# ============================================================
# 3. GENERATORS
# ============================================================

# A generator produces values one at a time instead of
# storing all values in memory at once.


# Normal function

def normal_numbers():

    return [1, 2, 3, 4, 5]


print("Normal Function:", normal_numbers())


# Generator function

def generate_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


result = generate_numbers()

print("Generator:", result)

for number in result:
    print(number)


# Example 2: Generate numbers using a loop

def generate_numbers_loop(n):

    for i in range(1, n + 1):
        yield i


for number in generate_numbers_loop(5):
    print("Generated:", number)


# ============================================================
# 4. YIELD KEYWORD
# ============================================================

# yield is used inside a generator function.
# It returns a value temporarily and pauses the function.
# The function continues from where it stopped when requested
# for the next value.


def count_numbers(n):

    i = 1

    while i <= n:
        yield i
        i += 1


for number in count_numbers(5):
    print("Count:", number)


# Example: Generate squares

def generate_squares(n):

    for i in range(1, n + 1):
        yield i ** 2


for square in generate_squares(5):
    print("Square:", square)


# ============================================================
# 5. NEXT KEYWORD
# ============================================================

# next() is used to get the next value from a generator.


def numbers_generator():

    yield 10
    yield 20
    yield 30


numbers = numbers_generator()

print("First:", next(numbers))
print("Second:", next(numbers))
print("Third:", next(numbers))


# Example with more values

def letters_generator():

    yield "A"
    yield "B"
    yield "C"


letters = letters_generator()

print(next(letters))
print(next(letters))
print(next(letters))


# ============================================================
# 6. DIFFERENCE BETWEEN FUNCTIONS & GENERATORS
# ============================================================

# Normal Function:
# - Uses return
# - Returns the result immediately
# - Function execution ends after return
# - Usually creates/returns the complete result
#
# Generator:
# - Uses yield
# - Produces values one at a time
# - Pauses after each yield
# - Continues when next value is requested
# - Useful for memory-efficient processing


# Normal Function Example

def normal_function():

    return [1, 2, 3, 4, 5]


result = normal_function()

print("Normal Function Result:", result)


# Generator Example

def generator_function():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


result = generator_function()

print("Generator Result:", result)

for value in result:
    print(value)


# ============================================================
# PRACTICE PROBLEMS
# ============================================================

# Problem 1: Create a list of cubes

cubes = [i ** 3 for i in range(1, 6)]

print("Cubes:", cubes)


# Problem 2: Create a list of multiples of 5

multiples = [i * 5 for i in range(1, 11)]

print("Multiples of 5:", multiples)


# Problem 3: Find vowels using list comprehension

text = "programming"

vowels = [char for char in text if char in "aeiou"]

print("Vowels:", vowels)


# Problem 4: Find numbers divisible by both 2 and 3

numbers = range(1, 31)

result = [i for i in numbers if i % 2 == 0 and i % 3 == 0]

print("Divisible by 2 and 3:", result)


# Problem 5: Flatten a nested list

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flattened = [
    value
    for row in nested_list
    for value in row
]

print("Flattened:", flattened)


# Problem 6: Generate even numbers

def even_generator(n):

    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i


for number in even_generator(20):
    print("Even:", number)


# Problem 7: Generate Fibonacci numbers

def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print("Fibonacci:", number)


# Problem 8: Generate squares of even numbers

def even_squares(n):

    for i in range(1, n + 1):

        if i % 2 == 0:
            yield i ** 2


for value in even_squares(10):
    print("Even Square:", value)


# ============================================================
# END OF DAY 18
# ============================================================
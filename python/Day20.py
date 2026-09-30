# ============================================================
# Day 20: Built-in Modules
# ============================================================
# SubTopics:
# 1. Math Module
# 2. Random Module
# 3. Sys Module
# 4. Platform Module
# 5. Collections Module
# 6. Itertools Module


# ============================================================
# 1. MATH MODULE
# ============================================================

import math

# Square root
print("Square Root:", math.sqrt(25))

# Power
print("Power:", math.pow(2, 3))

# Factorial
print("Factorial:", math.factorial(5))

# Ceiling
print("Ceiling:", math.ceil(4.3))

# Floor
print("Floor:", math.floor(4.8))

# Absolute value
print("Absolute:", math.fabs(-10))

# Greatest Common Divisor
print("GCD:", math.gcd(12, 18))

# Least Common Multiple
print("LCM:", math.lcm(12, 18))

# Constants
print("PI:", math.pi)
print("Euler's Number:", math.e)


# ============================================================
# MATH MODULE - PRACTICE
# ============================================================

# Find area of a circle

radius = 5

area = math.pi * radius ** 2

print("Area of Circle:", area)


# ============================================================
# 2. RANDOM MODULE
# ============================================================

import random

# Generate random integer

number = random.randint(1, 100)

print("Random Number:", number)


# Generate random floating-point number

number = random.random()

print("Random Float:", number)


# Random number within a range

number = random.randrange(1, 20, 2)

print("Random Odd Number:", number)


# Choose a random element

names = ["Navya", "Rahul", "Anil", "Priya"]

print("Random Name:", random.choice(names))


# Select multiple random elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Random Sample:", random.sample(numbers, 3))


# Shuffle a list

cards = [1, 2, 3, 4, 5]

random.shuffle(cards)

print("Shuffled List:", cards)


# ============================================================
# RANDOM MODULE - PRACTICE
# ============================================================

# Simple number guessing

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct Guess")
else:
    print("Wrong Guess")
    print("The number was:", secret_number)


# ============================================================
# 3. SYS MODULE
# ============================================================

import sys

# Python version

print("Python Version:", sys.version)


# Platform information

print("Platform:", sys.platform)


# Python executable location

print("Python Executable:", sys.executable)


# Number of command-line arguments

print("Command Line Arguments:", sys.argv)


# ============================================================
# SYS MODULE - PRACTICE
# ============================================================

# Example of command-line arguments:
#
# python Day20.py Hello Python
#
# sys.argv contains:
# [script_name, Hello, Python]


if len(sys.argv) > 1:
    print("Arguments provided:")

    for argument in sys.argv:
        print(argument)
else:
    print("No command-line arguments provided")


# ============================================================
# 4. PLATFORM MODULE
# ============================================================

import platform

# Operating system

print("Operating System:", platform.system())

# OS release

print("OS Release:", platform.release())

# OS version

print("OS Version:", platform.version())

# Machine type

print("Machine:", platform.machine())

# Processor

print("Processor:", platform.processor())

# Python implementation

print("Python Implementation:", platform.python_implementation())


# ============================================================
# PLATFORM MODULE - PRACTICE
# ============================================================

print("System Information")
print("------------------")
print("System:", platform.system())
print("Machine:", platform.machine())
print("Processor:", platform.processor())


# ============================================================
# 5. COLLECTIONS MODULE
# ============================================================

import collections


# ------------------------------------------------------------
# Counter
# ------------------------------------------------------------

# Counter counts the occurrences of elements.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

count = collections.Counter(numbers)

print("Counter:", count)


# Count characters

text = "programming"

character_count = collections.Counter(text)

print("Character Count:", character_count)


# Most common elements

print("Most Common:", character_count.most_common(3))


# ------------------------------------------------------------
# defaultdict
# ------------------------------------------------------------

# defaultdict provides a default value when a key
# does not exist.

student_marks = collections.defaultdict(int)

student_marks["Math"] = 90
student_marks["Python"] = 95

print("Math:", student_marks["Math"])
print("Python:", student_marks["Python"])
print("Java:", student_marks["Java"])


# ------------------------------------------------------------
# namedtuple
# ------------------------------------------------------------

# namedtuple allows us to create tuple-like objects
# with named fields.

Student = collections.namedtuple(
    "Student",
    ["name", "age", "course"]
)

student = Student("Navya", 22, "CSD")

print("Name:", student.name)
print("Age:", student.age)
print("Course:", student.course)


# ------------------------------------------------------------
# deque
# ------------------------------------------------------------

# deque stands for double-ended queue.

numbers = collections.deque([1, 2, 3])

numbers.append(4)
numbers.appendleft(0)

print("Deque:", numbers)

numbers.pop()
numbers.popleft()

print("After removal:", numbers)


# ============================================================
# COLLECTIONS - PRACTICE
# ============================================================

# Find frequency of characters

text = "hello world"

frequency = collections.Counter(text)

print("Character Frequency:")

for char, count in frequency.items():

    if char != " ":
        print(char, ":", count)


# ============================================================
# 6. ITERTOOLS MODULE
# ============================================================

import itertools


# ------------------------------------------------------------
# count()
# ------------------------------------------------------------

# count() creates an infinite sequence.

counter = itertools.count(1)

print("Count:", next(counter))
print("Count:", next(counter))
print("Count:", next(counter))
print("Count:", next(counter))


# ------------------------------------------------------------
# cycle()
# ------------------------------------------------------------

# cycle() repeats elements continuously.

colors = itertools.cycle(["Red", "Green", "Blue"])

for i in range(6):
    print("Color:", next(colors))


# ------------------------------------------------------------
# repeat()
# ------------------------------------------------------------

# repeat() repeats the same value.

values = itertools.repeat("Python", 3)

for value in values:
    print(value)


# ------------------------------------------------------------
# chain()
# ------------------------------------------------------------

# chain() combines multiple iterables.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = itertools.chain(list1, list2)

print("Combined:", list(combined))


# ------------------------------------------------------------
# combinations()
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

result = itertools.combinations(numbers, 2)

print("Combinations:")

for combination in result:
    print(combination)


# ------------------------------------------------------------
# permutations()
# ------------------------------------------------------------

numbers = [1, 2, 3]

result = itertools.permutations(numbers, 2)

print("Permutations:")

for permutation in result:
    print(permutation)


# ============================================================
# ITERTOOLS - PRACTICE
# ============================================================

# Generate combinations of letters

letters = ["A", "B", "C", "D"]

result = itertools.combinations(letters, 2)

print("Letter Combinations:")

for combination in result:
    print(combination)


# Generate permutations

result = itertools.permutations(letters, 2)

print("Letter Permutations:")

for permutation in result:
    print(permutation)


# ============================================================
# MINI PRACTICE PROBLEMS
# ============================================================


# Problem 1: Find factorial using math

n = 6

print("Factorial:", math.factorial(n))


# Problem 2: Count frequency of numbers

numbers = [1, 1, 2, 2, 2, 3, 4, 4]

frequency = collections.Counter(numbers)

print("Frequency:", frequency)


# Problem 3: Generate random numbers

for i in range(5):
    print("Random:", random.randint(1, 50))


# Problem 4: Generate combinations

numbers = [1, 2, 3, 4]

for combination in itertools.combinations(numbers, 2):
    print("Combination:", combination)


# Problem 5: Display system information

print("System:", platform.system())
print("Python:", platform.python_version())


# ============================================================
# END OF DAY 20
# ============================================================
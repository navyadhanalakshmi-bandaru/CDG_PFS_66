# ============================================================
# Day 19: Modules
# ============================================================
# SubTopics:
# 1. Introduction to Modules
# 2. Types of Modules
# 3. User Defined Modules
# 4. Import Statements


# ============================================================
# 1. INTRODUCTION TO MODULES
# ============================================================

# A module is a Python file (.py) containing code such as
# functions, variables, and classes.
#
# Modules help us:
# - Reuse code
# - Organize programs
# - Avoid writing the same code repeatedly
# - Make large projects easier to maintain


# Example:
#
# math is a built-in Python module.
#
# We can import it and use its functions.


import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Value of pi:", math.pi)


# ============================================================
# 2. TYPES OF MODULES
# ============================================================

# There are mainly three categories:
#
# 1. Built-in / Standard Library Modules
# 2. User-defined Modules
# 3. Third-party Modules


# ------------------------------------------------------------
# 2.1 STANDARD LIBRARY MODULES
# ------------------------------------------------------------

# Python provides many modules as part of its standard library.

import math
import random
import datetime


# math module

print("Square root:", math.sqrt(16))
print("Factorial:", math.factorial(5))


# random module

number = random.randint(1, 100)

print("Random number:", number)


# datetime module

current_date = datetime.date.today()

print("Today's date:", current_date)


# ------------------------------------------------------------
# 2.2 USER-DEFINED MODULES
# ------------------------------------------------------------

# A module created by the programmer is called
# a user-defined module.
#
# Example:
#
# Suppose we create a file named:
#
# calculator.py
#
# The file can contain:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# Then another Python file can import calculator.py.


# ============================================================
# 3. USER DEFINED MODULES
# ============================================================

# Create a separate file called:
#
# calculator.py
#
# Put the following code inside calculator.py:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
#
# Then use the module in Day19.py.


# Import the user-defined module

# import calculator
#
# print(calculator.add(10, 20))
# print(calculator.subtract(20, 10))
# print(calculator.multiply(5, 4))
# print(calculator.divide(20, 5))


# ============================================================
# 4. IMPORT STATEMENTS
# ============================================================

# There are different ways to import modules.


# ------------------------------------------------------------
# 4.1 import module
# ------------------------------------------------------------

import math

print("Using import:")
print(math.sqrt(36))


# ------------------------------------------------------------
# 4.2 from module import function
# ------------------------------------------------------------

from math import sqrt

print("Using from import:")
print(sqrt(49))


# ------------------------------------------------------------
# 4.3 Import multiple functions
# ------------------------------------------------------------

from math import sqrt, factorial

print("Square root:", sqrt(64))
print("Factorial:", factorial(5))


# ------------------------------------------------------------
# 4.4 import module with alias
# ------------------------------------------------------------

import math as m

print("Using alias:")
print(m.sqrt(81))


# ------------------------------------------------------------
# 4.5 from module import function with alias
# ------------------------------------------------------------

from math import factorial as fact

print("Factorial:", fact(5))


# ============================================================
# PRACTICE WITH DIFFERENT STANDARD MODULES
# ============================================================


# ------------------------------------------------------------
# random module
# ------------------------------------------------------------

import random

print("Random integer:", random.randint(1, 10))


# Random choice

names = ["Navya", "Rahul", "Anil", "Priya"]

print("Random name:", random.choice(names))


# ------------------------------------------------------------
# datetime module
# ------------------------------------------------------------

import datetime

today = datetime.date.today()

print("Today:", today)


# ------------------------------------------------------------
# os module
# ------------------------------------------------------------

import os

print("Current working directory:")
print(os.getcwd())


# ============================================================
# USER-DEFINED MODULE PRACTICE
# ============================================================

# Create another file named:
#
# operations.py
#
# Add the following code:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def square(a):
#     return a * a
#
#
# Then in Day19.py:
#
# import operations
#
# print(operations.add(10, 20))
# print(operations.subtract(20, 10))
# print(operations.multiply(5, 4))
# print(operations.square(6))


# ============================================================
# __name__ == "__main__"
# ============================================================

# When a Python file is run directly,
# __name__ becomes "__main__".
#
# Example:
#
# if __name__ == "__main__":
#     print("This file is being executed directly")


if __name__ == "__main__":
    print("Day 19 module file executed directly")


# ============================================================
# END OF DAY 19
# ============================================================
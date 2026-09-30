# ============================================================
# Day 15: Functions and Arguments
# ============================================================
# SubTopics:
# 1. Functions Introduction
# 2. User Defined Functions
# 3. Types of Functions
# 4. Function Syntax
# 5. Return Statements
# 6. Positional Arguments
# 7. Default Arguments


# ============================================================
# 1. FUNCTIONS INTRODUCTION
# ============================================================

# A function is a reusable block of code that performs
# a specific task.

# Example:

def greet():
    print("Hello, Welcome to Python!")


# Calling the function
greet()


# ============================================================
# 2. USER DEFINED FUNCTIONS
# ============================================================

# A function created by the programmer is called
# a user-defined function.

def welcome():
    print("Welcome to Python Programming")


welcome()


# Function with a simple calculation

def add_numbers():
    a = 10
    b = 20
    print("Sum:", a + b)


add_numbers()


# ============================================================
# 3. TYPES OF FUNCTIONS
# ============================================================

# Type 1: Built-in Function

print("Hello")
length = len("Python")
print("Length:", length)


# Type 2: User-defined Function

def message():
    print("This is a user-defined function")


message()


# Type 3: Function with arguments

def add(a, b):
    print("Addition:", a + b)


add(10, 20)


# Type 4: Function with return value

def multiply(a, b):
    return a * b


result = multiply(5, 4)
print("Multiplication:", result)


# ============================================================
# 4. FUNCTION SYNTAX
# ============================================================

# Syntax:
#
# def function_name(parameters):
#     statements
#     return value


def square(n):
    return n * n


print("Square:", square(5))


# Function to check even or odd

def check_even_odd(n):

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(10))


# ============================================================
# 5. RETURN STATEMENTS
# ============================================================

# Return sends a value back to the place where
# the function was called.

def addition(a, b):
    return a + b


result = addition(15, 25)

print("Result:", result)


# Return multiple values

def calculate(a, b):
    return a + b, a - b, a * b


sum_value, difference, product = calculate(10, 5)

print("Sum:", sum_value)
print("Difference:", difference)
print("Product:", product)


# ============================================================
# 6. POSITIONAL ARGUMENTS
# ============================================================

# In positional arguments, values are passed according
# to the position of the parameters.

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Navya", 22)


# Another example

def introduce(name, course, college):
    print("Name:", name)
    print("Course:", course)
    print("College:", college)


introduce("Navya", "CSE", "Veltech")


# ============================================================
# 7. DEFAULT ARGUMENTS
# ============================================================

# A default argument has a predefined value.
# If no value is passed, the default value is used.

def greet_user(name="Student"):
    print("Hello", name)


greet_user()
greet_user("Navya")


# Another example

def employee(name, role="Software Developer"):
    print("Name:", name)
    print("Role:", role)


employee("Navya")
employee("Rahul", "Python Developer")


# ============================================================
# PRACTICE PROBLEMS
# ============================================================

# Problem 1: Find the square of a number

def find_square(n):
    return n * n


print("Square:", find_square(8))


# Problem 2: Find the largest of two numbers

def largest(a, b):

    if a > b:
        return a
    else:
        return b


print("Largest:", largest(25, 15))


# Problem 3: Check whether a number is positive or negative

def check_number(n):

    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


print(check_number(-10))


# Problem 4: Calculate simple interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print("Simple Interest:", simple_interest(10000, 5, 2))


# Problem 5: Calculate area of a rectangle

def rectangle_area(length, width):
    return length * width


print("Area:", rectangle_area(10, 5))


# ============================================================
# END OF DAY 15
# ============================================================
# ============================================================
# Day 16: Scope and Recursion
# ============================================================
# SubTopics:
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope
# 4. Built-in Scope
# 5. LEGB Rule
# 6. Pass by Value
# 7. Pass by Reference
# 8. Recursive Functions


# ============================================================
# 1. LOCAL SCOPE
# ============================================================

# A variable created inside a function has local scope.
# It can be accessed only inside that function.

def local_example():
    x = 10
    print("Local variable:", x)


local_example()


# ============================================================
# 2. ENCLOSING SCOPE
# ============================================================

# Enclosing scope occurs when a function is defined
# inside another function.

def outer_function():

    x = 20

    def inner_function():
        print("Enclosing variable:", x)

    inner_function()


outer_function()


# Using nonlocal keyword

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)


outer()


# ============================================================
# 3. GLOBAL SCOPE
# ============================================================

# A variable created outside all functions has global scope.

x = 100


def global_example():
    print("Global variable:", x)


global_example()

print("Outside function:", x)


# Using global keyword

count = 0


def increase_count():
    global count
    count += 1


increase_count()
increase_count()

print("Count:", count)


# ============================================================
# 4. BUILT-IN SCOPE
# ============================================================

# Built-in scope contains names provided by Python.
#
# Examples:
# print()
# len()
# max()
# min()
# sum()
# type()
# range()


numbers = [10, 20, 30, 40]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Type:", type(numbers))


# ============================================================
# 5. LEGB RULE
# ============================================================

# Python searches for a variable in this order:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in


x = "Global"


def outer():

    x = "Enclosing"

    def inner():

        x = "Local"

        print("Value:", x)

    inner()


outer()


# LEGB example without local variable

x = "Global"


def outer_example():

    x = "Enclosing"

    def inner_example():
        print(x)

    inner_example()


outer_example()


# ============================================================
# 6. PASS BY VALUE
# ============================================================

# Python uses object references.
# For immutable objects such as integers, changing the
# parameter inside the function does not change the original
# variable.


def change_value(x):

    x = 50
    print("Inside function:", x)


a = 10

change_value(a)

print("Outside function:", a)


# ============================================================
# 7. PASS BY REFERENCE
# ============================================================

# Python does not have traditional pass-by-reference.
# However, when a mutable object such as a list is passed,
# its contents can be modified inside the function.


def add_element(numbers):

    numbers.append(40)


numbers = [10, 20, 30]

add_element(numbers)

print("List after function call:", numbers)


# Another example

def update_list(items):

    items[0] = 100


items = [10, 20, 30]

update_list(items)

print("Updated list:", items)


# ============================================================
# 8. RECURSIVE FUNCTIONS
# ============================================================

# A recursive function is a function that calls itself.
#
# A recursive function should have:
# 1. Base condition
# 2. Recursive call


# Example 1: Print numbers from 1 to 5

def print_numbers(n):

    if n > 5:
        return

    print(n)
    print_numbers(n + 1)


print_numbers(1)


# Example 2: Print numbers from 5 to 1

def reverse_numbers(n):

    if n == 0:
        return

    print(n)
    reverse_numbers(n - 1)


reverse_numbers(5)


# Example 3: Sum of numbers from 1 to n

def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("Sum:", sum_numbers(5))


# Example 4: Factorial using recursion

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial:", factorial(5))


# Example 5: Fibonacci using recursion

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci:", fibonacci(6))


# ============================================================
# RECURSIVE PRACTICE PROBLEMS
# ============================================================

# Problem 1: Sum of digits

def digit_sum(n):

    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


print("Digit Sum:", digit_sum(12345))


# Problem 2: Power of a number

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print("Power:", power(2, 5))


# Problem 3: Reverse a string

def reverse_string(text):

    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]


print("Reversed:", reverse_string("Python"))


# Problem 4: Count digits using recursion

def count_digits(n):

    if n == 0:
        return 0

    return 1 + count_digits(n // 10)


print("Number of digits:", count_digits(123456))


# ============================================================
# END OF DAY 16
# ============================================================
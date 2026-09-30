# ============================================================
# Day 13: Patterns and Problems
# ============================================================
# SubTopics:
# 1. Nested Loops
# 2. Loop Problems
# 3. Star Patterns
# 4. Number Patterns


# ============================================================
# 1. NESTED LOOPS
# ============================================================

# Example 1: Print rows and columns

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Example 2: Print a 3 x 3 matrix

for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()


# Example 3: Multiplication tables from 1 to 5

for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# ============================================================
# 2. LOOP PROBLEMS
# ============================================================

# Problem 1: Count digits in a number

n = int(input("Enter a number: "))

count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        n //= 10
        count += 1

print("Number of digits:", count)


# Problem 2: Sum of digits

n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits:", total)


# Problem 3: Reverse a number

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse:", reverse)


# Problem 4: Check palindrome

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# ============================================================
# 3. STAR PATTERNS
# ============================================================

# Pattern 1:
# *
# * *
# * * *
# * * * *

for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Pattern 2:
# * * * *
# * * *
# * *
# *

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Pattern 3:
# *
# * *
# * * *
# * * * *

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 4:
#       *
#     * *
#   * * *
# * * * *

for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()


# Pattern 5: Square
# * * * *
# * * * *
# * * * *
# * * * *

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# Pattern 6: Hollow square
# * * * *
# *     *
# *     *
# * * * *

for i in range(1, 5):
    for j in range(1, 5):
        if i == 1 or i == 4 or j == 1 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ============================================================
# 4. NUMBER PATTERNS
# ============================================================

# Pattern 1:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Pattern 2:
# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()


# Pattern 3:
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Pattern 4:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# Pattern 5:
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

for i in range(1, 5):
    for j in range(1, 5):
        print(i + j - 1, end=" ")
    print()
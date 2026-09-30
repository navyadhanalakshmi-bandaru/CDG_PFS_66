# ============================================================
# Day 14: Patterns and Problems
# ============================================================
# SubTopics:
# 1. Pyramid Patterns
# 2. Name Printing Patterns


# ============================================================
# 1. PYRAMID PATTERNS
# ============================================================

# Pattern 1: Right Half Pyramid
#
# *
# * *
# * * *
# * * * *
# * * * * *

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Pattern 2: Inverted Right Half Pyramid
#
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Pattern 3: Full Pyramid
#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
print()

# Pattern 4: Inverted Full Pyramid
#
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range(n, 0, -1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
print()

# Pattern 5: Hollow Pyramid
#
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
print()

# Pattern 6: Diamond Pattern
#
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
print()

# ============================================================
# 2. NAME PRINTING PATTERNS
# ============================================================

# Pattern 7: Print name vertically

name = "NAVYA"

for char in name:
    print(char)
print()

# Pattern 8: Print name horizontally

name = "NAVYA"

for char in name:
    print(char, end=" ")


print()


# Pattern 9: Print name 5 times

name = "NAVYA"

for i in range(5):
    print(name)
print()

# Pattern 10: Print each character with its position

name = "NAVYA"

for i in range(len(name)):
    print(i + 1, name[i])
print()

# Pattern 11: Increasing name pattern
#
# N
# NA
# NAV
# NAVY
# NAVYA

name = "NAVYA"

for i in range(1, len(name) + 1):
    print(name[:i])
print()

# Pattern 12: Decreasing name pattern
#
# NAVYA
# NAVY
# NAV
# NA
# N

name = "NAVYA"

for i in range(len(name), 0, -1):
    print(name[:i])
print()

# Pattern 13: Repeated character pattern
#
# N
# A A
# V V V
# Y Y Y Y
# A A A A A

name = "NAVYA"

for i in range(len(name)):
    for j in range(i + 1):
        print(name[i], end=" ")
    print()
print()

# Pattern 14: Full name pyramid

name = "NAVYA"

for i in range(1, len(name) + 1):

    for j in range(len(name) - i):
        print(" ", end=" ")

    for j in range(i):
        print(name[j], end=" ")

    print()
# Day 11: While Loops and Nested Loops
# SubTopics:
# 1. While Loop
# 2. While with Else


# ============================================================
# 1. WHILE LOOP
# ============================================================

# Example 1: Print numbers from 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1


# Example 2: Print even numbers from 2 to 10

i = 2

while i <= 10:
    print(i)
    i += 2


# Example 3: Print numbers in reverse

i = 5

while i >= 1:
    print(i)
    i -= 1


# Example 4: Sum of numbers from 1 to 5

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum:", total)


# ============================================================
# 2. WHILE WITH ELSE
# ============================================================

# Example 1: While loop with else

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed")


# Example 2: Print numbers and execute else

i = 1

while i <= 3:
    print("Number:", i)
    i += 1
else:
    print("The while loop has ended")


# Example 3: While with else and break

i = 1

while i <= 5:
    print(i)

    if i == 3:
        break

    i += 1
else:
    print("Loop completed successfully")

# Note:
# The else block will NOT execute when the while loop
# is terminated using break.
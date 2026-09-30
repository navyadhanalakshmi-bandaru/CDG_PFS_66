# ============================================================
# Day 12: While Loops and Nested Loops
# ============================================================
# SubTopics:
# 1. Iteration Practice
# 2. Loop-based Logical Problems


# ============================================================
# 1. ITERATION PRACTICE
# ============================================================

# 1. Print numbers from 1 to 10

i = 1

while i <= 10:
    print(i)
    i += 1


# 2. Print numbers from 10 to 1

i = 10

while i >= 1:
    print(i)
    i -= 1


# 3. Print even numbers from 1 to 20

i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# 4. Print odd numbers from 1 to 20

i = 1

while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1


# 5. Print multiplication table

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# ============================================================
# 2. LOOP-BASED LOGICAL PROBLEMS
# ============================================================

# 6. Count digits in a number

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n //= 10
    count += 1

print("Number of digits:", count)


# 7. Sum of digits

n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits:", total)


# 8. Reverse a number

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse:", reverse)


# 9. Check palindrome number

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


# 10. Count even and odd digits

n = int(input("Enter a number: "))

even_count = 0
odd_count = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)


# 11. Find the largest digit

n = int(input("Enter a number: "))

largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n //= 10

print("Largest digit:", largest)


# 12. Find the smallest digit

n = int(input("Enter a number: "))

smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n //= 10

print("Smallest digit:", smallest)


# ============================================================
# NESTED WHILE LOOP
# ============================================================

# 13. Print a square pattern

i = 1

while i <= 4:
    j = 1

    while j <= 4:
        print("*", end=" ")
        j += 1

    print()
    i += 1


# 14. Print a triangle pattern

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print("*", end=" ")
        j += 1

    print()
    i += 1


# 15. Print numbers using nested loops

i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(j, end=" ")
        j += 1

    print()
    i += 1
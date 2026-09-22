
# Day 10: Python Control Statements
# Topics: For Loop, For-Else, Break, Continue, Pass, Assert

# 1. FOR Loop
# Program to print numbers from 1 to 10

print("\n--- 1. FOR Loop ---")

for i in range(1, 11):
    print(i)


# 2. FOR Loop with ELSE
# Program to execute else after the loop completes

print("\n--- 2. FOR with ELSE ---")

for i in range(1, 6):
    print(i)
else:
    print("Loop completed")


# 3. BREAK Statement
# Program to stop the loop when number reaches 5

print("\n--- 3. BREAK ---")

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 4. CONTINUE Statement
# Program to skip printing the number 5

print("\n--- 4. CONTINUE ---")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 5. PASS Statement
# Program to use pass as a placeholder

print("\n--- 5. PASS ---")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# 6. ASSERT Keyword
# Program to check whether a number is positive

print("\n--- 6. ASSERT ---")

n = int(input("Enter a positive number: "))

assert n > 0, "Number must be positive"

print("Valid positive number:", n)


# 7. Print Even Numbers
# Program to print even numbers from 1 to 20

print("\n--- 7. Even Numbers ---")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 8. Print Odd Numbers
# Program to print odd numbers from 1 to 20

print("\n--- 8. Odd Numbers ---")

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# 9. FOR Loop with BREAK
# Program to find the first number divisible by 7

print("\n--- 9. First Number Divisible by 7 ---")

for i in range(1, 101):
    if i % 7 == 0:
        print("First number divisible by 7:", i)
        break


# 10. FOR Loop with CONTINUE
# Program to skip multiples of 3

print("\n--- 10. Skip Multiples of 3 ---")

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# 11. FOR Loop with ELSE and BREAK
# Program to search for a number in a list

print("\n--- 11. Search a Number ---")

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

for i in numbers:
    if i == target:
        print("Number found")
        break
else:
    print("Number not found")


# 12. Multiplication Table
# Program to print the multiplication table of a number

print("\n--- 12. Multiplication Table ---")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 13. Sum of First N Natural Numbers
# Program to calculate the sum using a for loop

print("\n--- 13. Sum of Natural Numbers ---")

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# 14. Count Digits
# Program to count digits in a positive integer

print("\n--- 14. Count Digits ---")

n = input("Enter a positive integer: ")

count = 0

for i in n:
    if i.isdigit():
        count += 1

print("Number of digits:", count)


# 15. ASSERT with Marks
# Program to validate marks between 0 and 100

print("\n--- 15. Assert with Marks ---")

marks = int(input("Enter marks between 0 and 100: "))

assert 0 <= marks <= 100, "Invalid marks"

print("Valid marks:", marks)


# 1. FOR LOOP WITH A STRING
# Iterates through each character in the string.
text = "Python"

for char in text:
    print(char)


# 2. FOR LOOP WITH A LIST
# Iterates through each item in the list.
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# 3. FOR LOOP WITH A TUPLE
# Iterates through each item in the tuple.
colors = ("red", "green", "blue")

for color in colors:
    print(color)


# 4. FOR LOOP WITH A SET
# Iterates through each item in the set.
# Set iteration order is not guaranteed.
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)


# 5. FOR LOOP WITH A DICTIONARY
# By default, iterates through dictionary keys.
student = {"name": "Navya", "age": 21, "course": "Python"}

for key in student:
    print(key)


# 6. FOR LOOP WITH DICTIONARY VALUES
# values() gives the values from the dictionary.
for value in student.values():
    print(value)


# 7. FOR LOOP WITH DICTIONARY ITEMS
# items() gives each key-value pair as a tuple.
for key, value in student.items():
    print(key, ":", value)


# 8. FOR LOOP WITH RANGE
# range(1, 6) generates numbers from 1 to 5.
for num in range(1, 6):
    print(num)


# 9. FOR LOOP WITH A LIST OF STRINGS
# Iterates through each name.
names = ["Navya", "Ravi", "Priya"]

for name in names:
    print("Hello", name)


# 10. FOR LOOP WITH A NESTED LIST
# Iterates through each inner list, then each item.
matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for num in row:
        print(num)


# 11. FOR LOOP WITH ENUMERATE
# enumerate() gives both the index and the item.
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)


# 12. FOR LOOP WITH ZIP
# zip() combines items from two iterables.
names = ["Navya", "Ravi", "Priya"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, "scored", mark)


# 13. FOR LOOP WITH A STRING AND CONDITION
# Prints only vowels from the string.
word = "education"

for char in word:
    if char in "aeiou":
        print(char)


# 14. FOR LOOP WITH A LIST AND CONDITION
# Prints only even numbers.
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print(num)


# 15. FOR LOOP WITH A RANGE AND STEP
# Prints even numbers from 2 to 10.
for num in range(2, 11, 2):
    print(num)


# End of Day 10
print("\nDay 10 completed!")


# Day 4: Python Operators and Formatting

# 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. Comparison Operators
print("\n--- Comparison Operators ---")

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 3. Assignment Operators
print("\n--- Assignment Operators ---")

x = 10
x += 5
print("After +=:", x)

x -= 3
print("After -=:", x)

x *= 2
print("After *=:", x)

x /= 4
print("After /=:", x)

x = 10
x %= 3
print("After %=:", x)


# 4. Logical Operators
print("\n--- Logical Operators ---")

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)


# 5. Membership Operators
print("\n--- Membership Operators ---")

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" not in fruits)


# 6. Identity Operators
print("\n--- Identity Operators ---")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)


# 7. Bitwise Operators
print("\n--- Bitwise Operators ---")

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# 8. Input Formatting
print("\n--- Input Formatting ---")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# 9. Output Formatting
print("\n--- Output Formatting ---")

name = "Navya"
age = 21
marks = 95.5678

print("Name: {}, Age: {}, Marks: {}".format(name, age, marks))


# 10. Modulo Formatting
print("\n--- Modulo Formatting ---")

name = "Navya"
age = 21
marks = 95.5678

print("Name: %s" % name)
print("Age: %d" % age)
print("Marks: %.2f" % marks)

print("Name: %s, Age: %d, Marks: %.2f" % (name, age, marks))


# 11. F-Strings
print("\n--- F-Strings ---")

name = "Navya"
age = 21
marks = 95.5678

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My marks are {marks:.2f}")

print(f"Next year, I will be {age + 1} years old")


# 12. Dot Format Method
print("\n--- Dot Format Method ---")

name = "Navya"
age = 21
marks = 95.5678

print("My name is {}".format(name))
print("I am {} years old".format(age))
print("My marks are {:.2f}".format(marks))

print("Name: {0}, Age: {1}".format(name, age))
print("Age: {1}, Name: {0}".format(name, age))

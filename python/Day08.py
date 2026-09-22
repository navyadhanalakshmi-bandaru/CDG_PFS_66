
# Day 8: Python Conditional Statements

# 1. IF Statement

print("--- IF Statement ---")

age = 20

if age >= 18:
    print("You are eligible to vote")


# 2. IF-ELSE Statement

print("\n--- IF-ELSE Statement ---")

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. ELIF Statement

print("\n--- ELIF Statement ---")

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Nested Conditions

print("\n--- Nested Conditions ---")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You are eligible to vote")
    else:
        print("Please bring your ID")
else:
    print("You are not eligible to vote")


# 5. Real-Time Example 1: Positive, Negative, or Zero

print("\n--- Number Checking ---")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# 6. Real-Time Example 2: Student Grade Calculator

print("\n--- Grade Calculator ---")

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")


# 7. Real-Time Example 3: Login System

print("\n--- Login System ---")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "navya":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")


# 8. Real-Time Example 4: ATM Withdrawal

print("\n--- ATM Withdrawal ---")

balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Enter a valid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

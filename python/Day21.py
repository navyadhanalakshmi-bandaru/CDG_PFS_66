# ============================================================
# Day 21: Built-in Module Practice
# ============================================================
# SubTopics:
# 1. Real-time Examples
# 2. Random Password Generator
# 3. ATM Example


# ============================================================
# 1. REAL-TIME EXAMPLES
# ============================================================

# Python modules are useful in real-world applications.
#
# Examples:
# - Random module -> Password generation, games
# - Math module -> Calculations
# - Datetime module -> Date and time applications
# - Collections module -> Counting and data processing
# - Sys module -> Command-line applications


# Example: Random number generation

import random

random_number = random.randint(1, 100)

print("Random Number:", random_number)


# Example: Current date and time

import datetime

current_time = datetime.datetime.now()

print("Current Date and Time:", current_time)


# Example: Mathematical calculation

import math

number = 64

print("Square Root:", math.sqrt(number))


# ============================================================
# 2. RANDOM PASSWORD GENERATOR
# ============================================================

import random
import string


# Generate a random password

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)


# ------------------------------------------------------------
# Password Generator using a function
# ------------------------------------------------------------

def generate_password(length):

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter password length again: "))

if length > 0:
    print("New Password:", generate_password(length))
else:
    print("Password length must be greater than 0")


# ============================================================
# 3. ATM EXAMPLE
# ============================================================

# This is a simple ATM simulation.
#
# Operations:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit


balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))


if entered_pin == pin:

    print("\nLogin Successful")

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")

        choice = int(input("Enter your choice: "))


        # Check Balance

        if choice == 1:

            print("Current Balance:", balance)


        # Deposit

        elif choice == 2:

            amount = float(input("Enter deposit amount: "))

            if amount > 0:

                balance += amount

                print("Deposit Successful")
                print("Updated Balance:", balance)

            else:

                print("Invalid amount")


        # Withdraw

        elif choice == 3:

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:

                print("Invalid amount")

            elif amount > balance:

                print("Insufficient Balance")

            else:

                balance -= amount

                print("Withdrawal Successful")
                print("Remaining Balance:", balance)


        # Exit

        elif choice == 4:

            print("Thank you for using the ATM")
            break


        # Invalid choice

        else:

            print("Invalid choice. Please try again.")


else:

    print("Incorrect PIN")


# ============================================================
# ATM USING FUNCTIONS
# ============================================================

def check_balance(balance):

    print("Current Balance:", balance)


def deposit(balance, amount):

    if amount > 0:

        balance += amount

        print("Deposit Successful")

    else:

        print("Invalid Amount")

    return balance


def withdraw(balance, amount):

    if amount <= 0:

        print("Invalid Amount")

    elif amount > balance:

        print("Insufficient Balance")

    else:

        balance -= amount

        print("Withdrawal Successful")

    return balance


# Example

atm_balance = 5000

check_balance(atm_balance)

atm_balance = deposit(atm_balance, 2000)

check_balance(atm_balance)

atm_balance = withdraw(atm_balance, 1000)

check_balance(atm_balance)


# ============================================================
# MINI PRACTICE
# ============================================================

# Generate a 6-digit OTP

otp = ""

for i in range(6):
    otp += str(random.randint(0, 9))

print("Generated OTP:", otp)


# Generate a random username

names = ["Navya", "Rahul", "Anil", "Priya"]

username = random.choice(names)

number = random.randint(100, 999)

print("Random Username:", username + str(number))


# ============================================================
# END OF DAY 21
# ============================================================
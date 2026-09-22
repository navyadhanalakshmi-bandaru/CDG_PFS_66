# Check whether a number is even or odd

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program to check whether a number is positive, negative, or zero

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Program to find the greatest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greatest:", a)
elif b > a:
    print("Greatest:", b)
else:
    print("Both numbers are equal")

# Program to find the greatest among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

# Program to check whether a year is a leap year

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
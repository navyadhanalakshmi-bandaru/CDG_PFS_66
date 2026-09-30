# ==========================================
# DAY 25 - INTRODUCTION TO OOPs
# ==========================================

# 1. WHAT IS OOPs?
# OOPs = Object-Oriented Programming
# It is a programming approach based on Classes and Objects.
#
# Main concepts of OOPs:
# Class, Object, Attributes, Methods, etc.


# ==========================================
# 2. CLASSES
# ==========================================

# A class is a blueprint/template for creating objects.

class Student:
    pass


# ==========================================
# 3. OBJECTS
# ==========================================

# An object is an instance of a class.

student1 = Student()
student2 = Student()

print(student1)
print(student2)


# ==========================================
# 4. ATTRIBUTES
# ==========================================

# Attributes are the properties/data of an object.

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Navya", 21, "CSE")
student2 = Student("Rahul", 22, "CSE")

print("\nStudent Details:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)

print("\nStudent 2 Details:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Course:", student2.course)


# ==========================================
# 5. METHODS
# ==========================================

# Methods are functions defined inside a class.
# They describe the behavior of an object.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def study(self):
        print(self.name, "is studying Python")


student1 = Student("Navya", 21)

print("\nMethods:")
student1.display()
student1.study()


# ==========================================
# EXAMPLE: CAR
# ==========================================

class Car:

    # Attributes
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method
    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

    # Method
    def start(self):
        print(self.brand, "car is starting")


car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print("\nCar 1:")
car1.display()
car1.start()

print("\nCar 2:")
car2.display()
car2.start()


# ==========================================
# PRACTICE
# ==========================================

# Create a class Employee with:
# Attributes:
# name
# salary
# department
#
# Methods:
# display()
# work()

class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

    def work(self):
        print(self.name, "is working")


employee1 = Employee("Navya", 30000, "IT")

employee1.display()
employee1.work()
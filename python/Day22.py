# ============================================================
# Day 22: Exception Handling and File Operations
# ============================================================
# SubTopics:
# 1. Try
# 2. Except
# 3. Else
# 4. Finally
# 5. File Open
# 6. Read
# 7. Write
# 8. Append
# 9. Close


# ============================================================
# 1. TRY
# ============================================================

# try block contains code that may produce an error.

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except:
    print("Invalid input")


# ============================================================
# 2. EXCEPT
# ============================================================

# except handles the error that occurs in the try block.

try:
    a = 10
    b = 0

    result = a / b

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# Example: ValueError

try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid number")


# ============================================================
# MULTIPLE EXCEPT BLOCKS
# ============================================================

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# ============================================================
# 3. ELSE
# ============================================================

# else executes when there is NO exception.

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Division successful")
    print("Result:", result)


# ============================================================
# 4. FINALLY
# ============================================================

# finally executes whether an exception occurs or not.

try:

    number = int(input("Enter a number: "))

    print("Number:", number)

except ValueError:

    print("Invalid input")

finally:

    print("This block always executes")


# Example: try + except + else + finally

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:

    print("Invalid input")

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Result:", result)

finally:

    print("Program execution completed")


# ============================================================
# 5. FILE OPEN
# ============================================================

# open() is used to open a file.
#
# Syntax:
#
# open("filename", "mode")
#
# Common modes:
#
# r -> Read
# w -> Write
# a -> Append
# x -> Create


file = open("sample.txt", "w")

file.write("Hello, Python!")

file.close()


# ============================================================
# 6. READ
# ============================================================

# Reading the complete file

file = open("sample.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()


# Reading a specific number of characters

file = open("sample.txt", "r")

content = file.read(5)

print("First 5 characters:", content)

file.close()


# readline() reads one line

file = open("sample.txt", "r")

line = file.readline()

print("First Line:", line)

file.close()


# readlines() reads all lines into a list

file = open("sample.txt", "r")

lines = file.readlines()

print("Lines:", lines)

file.close()


# ============================================================
# 7. WRITE
# ============================================================

# "w" mode writes data to a file.
# If the file already contains data, it will be replaced.

file = open("write_example.txt", "w")

file.write("Python Programming\n")
file.write("Learning File Operations\n")
file.write("Day 22 Practice")

file.close()

print("Data written successfully")


# ============================================================
# 8. APPEND
# ============================================================

# "a" mode adds data at the end of the file.
# Existing data is not removed.

file = open("write_example.txt", "a")

file.write("\nThis line was added using append.")

file.close()

print("Data appended successfully")


# ============================================================
# 9. CLOSE
# ============================================================

# close() is used to close an opened file.

file = open("close_example.txt", "w")

file.write("File closing example")

file.close()

print("File closed successfully")


# ============================================================
# FILE OPERATIONS USING WITH
# ============================================================

# The with statement automatically closes the file.
#
# This is recommended instead of manually using close().


with open("student.txt", "w") as file:

    file.write("Name: Navya\n")
    file.write("Course: CSD\n")


with open("student.txt", "r") as file:

    content = file.read()

    print(content)


# ============================================================
# FILE PRACTICE PROBLEMS
# ============================================================


# Problem 1: Write student details

with open("student_details.txt", "w") as file:

    file.write("Name: Navya\n")
    file.write("Course: Computer Science\n")
    file.write("Language: Python\n")


# Problem 2: Read student details

with open("student_details.txt", "r") as file:

    data = file.read()

    print("Student Details:")
    print(data)


# Problem 3: Append another student

with open("student_details.txt", "a") as file:

    file.write("\nName: Rahul\n")
    file.write("Course: Computer Science\n")


# Problem 4: Count lines in a file

with open("student_details.txt", "r") as file:

    lines = file.readlines()

    print("Number of lines:", len(lines))


# Problem 5: Count words in a file

with open("student_details.txt", "r") as file:

    content = file.read()

    words = content.split()

    print("Number of words:", len(words))


# ============================================================
# EXCEPTION HANDLING WITH FILE OPERATIONS
# ============================================================

try:

    file = open("sample.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:

    print("File not found")

finally:

    try:
        file.close()
    except:
        pass


# ============================================================
# PRACTICE: SAFE FILE READING
# ============================================================

filename = input("Enter filename to read: ")

try:

    with open(filename, "r") as file:

        content = file.read()

        print("\nFile Content:")
        print(content)

except FileNotFoundError:

    print("The file does not exist")

except PermissionError:

    print("You do not have permission to access this file")


# ============================================================
# END OF DAY 22
# ============================================================
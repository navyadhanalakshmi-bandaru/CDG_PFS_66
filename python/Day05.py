
# Day 5: Python Strings

# 1. Introduction to Strings

# Strings are sequences of characters enclosed in quotes.
name = "Navya"
language = 'Python'
message = """Welcome to Python
String Programming"""

print("Name:", name)
print("Language:", language)
print("Message:", message)
print("Type:", type(name))


# 2. String Operations

print("\n--- String Operations ---")

s1 = "Hello"
s2 = "Python"

# Concatenation
print("Concatenation:", s1 + " " + s2)

# Repetition
print("Repetition:", s1 * 3)

# Length
print("Length:", len(s2))

# Membership
print("Is 'P' present:", "P" in s2)
print("Is 'z' absent:", "z" not in s2)

# String comparison
print("Comparison:", "apple" == "apple")

# Accessing characters using index
word = "Python"
print("First character:", word[0])
print("Last character:", word[-1])


# 3. String Methods

print("\n--- String Methods ---")

text = "  python programming  "

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Strip:", text.strip())

sentence = "I love Java"
print("Replace:", sentence.replace("Java", "Python"))

fruits = "apple,banana,mango"
print("Split:", fruits.split(","))

words = ["Python", "is", "easy"]
print("Join:", " ".join(words))

sample = "Python Programming"
print("Find:", sample.find("Pro"))
print("Count:", sample.count("m"))
print("Starts with:", sample.startswith("Python"))
print("Ends with:", sample.endswith("ing"))

print("Is alphabetic:", "Python".isalpha())
print("Is numeric:", "12345".isdigit())
print("Is alphanumeric:", "Python123".isalnum())
print("Is lowercase:", "python".islower())
print("Is uppercase:", "PYTHON".isupper())


# 4. String Slicing

print("\n--- String Slicing ---")

text = "PythonProgramming"

# string[start:stop]
print("First six characters:", text[0:6])

# From beginning to index 6
print("Beginning:", text[:6])

# From index 6 to the end
print("From index 6:", text[6:])

# Every second character
print("Step slicing:", text[::2])

# Reverse the string
print("Reversed:", text[::-1])

# Negative indexing
print("Last three characters:", text[-3:])

# Extract a specific portion
print("Substring:", text[6:17])


# Day 3: Python Data Types and Type Conversions

# 1. Integer (int)
a = 10
print("Integer:", a)
print(type(a))


# 2. Float (float)
b = 10.5
print("Float:", b)
print(type(b))


# 3. String (str)
c = "Python"
print("String:", c)
print(type(c))


# 4. Boolean (bool)
d = True
print("Boolean:", d)
print(type(d))


# 5. List
my_list = [10, 20, 30]
print("List:", my_list)
print(type(my_list))


# 6. Tuple
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)
print(type(my_tuple))


# 7. Set
my_set = {10, 20, 30}
print("Set:", my_set)
print(type(my_set))


# 8. Dictionary
my_dict = {"name": "Navya", "age": 21}
print("Dictionary:", my_dict)
print(type(my_dict))


# 9. Type Conversions
print("\n--- Type Conversions ---")

# Integer to float
x = 10
print(float(x))

# Float to integer
y = 10.8
print(int(y))

# Integer to string
z = 100
print(str(z))

# String to integer
num = "25"
print(int(num))

# String to float
price = "99.5"
print(float(price))

# Integer to boolean
print(bool(1))
print(bool(0))


# 10. Multiple Type Conversions
num1 = 10
num2 = 20.5

result = num1 + num2

print("Result:", result)
print("Result Type:", type(result))

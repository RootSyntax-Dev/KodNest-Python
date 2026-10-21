# Day - 1 of Learning Python

name = "Vinay"
age = 23
print(name)
print(id(name))
print(type(name))

print("Hello Python", end=" - ")
print("I am 21 years old")

print("Hello Python \nThank you Python")

# my name is Vinay and age is 23 str + str
print("My name is " + name + " age is ", age)
print("My name is " + name + " age is " + str(age))

# String Formating ()f strings
print(f"My name is {name} and age is {age}")

# Day - 2 of Learning Python

# single - line comments
"""
multi line
comments
"""

a = 10
a = 20
c = 30
# a, b, c = 10, 20, 30
# print(a, b, c)

a = b = c = 10
print(a, b, c)

a, b, c = "Abhi", "Ram", "Sai"
print(b)
print(a + b + c)

x, y, z = 30, 4, 8
print(x + z) # - 38
print(a + str(x)) # - Abhi30
print(b + c) # - RamSai
print(a, x) # - Abhi30
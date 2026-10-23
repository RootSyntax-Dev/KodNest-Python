# -------------------------
# Defining a function
# -------------------------

def greet():
    print("Hello Programmers!")
# Calling a function
greet()

# def to add 2 numbers?
def add():
    a = 10
    b = 20
    c = a + b
    print(c)
# Calling a function
add()

# def to find Square of a number?
def square():
    a = 5
    res = a * a
    print(res)
# Calling a function
square()

# Defining a function to greet().
def greet():
    name = "Abhi"
    print("Good Morning", name)
# Calling a function
greet()

# def to find largest number among 3 numbers?
def largest():
    a = 10
    b = 20
    c = 30
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
# Calling a function
largest()

# def to find num is even or odd?
def even_or_odd():
    a = 10
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
# Calling a function
even_or_odd()

# def to find Smallest number amoung 3 numbers?
def smallest():
    a = 10
    b = 20
    c = 30
    if a < b and a < c:
        print(a)
    elif b < a and  b < c:
        print(b)
    else:
        print(c)
# Calling a function
smallest()

# --------------------------- 
# Types of functions
# ---------------------------

# 1. no input & no output
def square():
    a = 5 * 5
    print(a)

square()

# 2. no input but return the output
def square():
    n = 5 * 5
    return n

print(square())

# 3. input but no return output
def square(a):
    res = a * a
    print(res)

square(5)

# 4. input and return the output
def square(a):
    res = a * a
    return res

print(square(5))
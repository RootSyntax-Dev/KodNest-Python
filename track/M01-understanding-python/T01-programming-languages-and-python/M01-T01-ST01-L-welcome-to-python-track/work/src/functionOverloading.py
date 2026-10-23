# 1. default arguments
def add(a, b=0, c=0):
    return a + b + c
print(add(10))
print(add(10, 20))
print(add(10, 20, 30))

# 2. Arbitrary arguments (var-args) using with * operator.
# here *args accepts 0 to n number of arguments.
# you can change the args keyword to any other word like *a or *b or *c
def add(*args):
    total = 0
    for i in args:
        total = total + i # same as total += i
    return total

print(add(10))
print(add(10, 20))
print(add(10, 20, 30, 40))

# kwargs - 0 to n arguments can be passed  --> dictionary.add
def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')} ", end = "")
    print(f"age is {kwargs.get('age')} ", end = "")
    print(f"city is {kwargs.get('city')} ")

stu_info(name = "Abhi", age = 20, city = "Hyderabad")

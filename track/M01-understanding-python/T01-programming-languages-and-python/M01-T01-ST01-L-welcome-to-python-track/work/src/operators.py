# Arithmetic operators ->
print(2 + 3) # 5 
print(2 - 3) # -1 
print(2 * 3) # 6 
print(10 / 3) # 3.3333333333333335 #Division
print(10 // 3) # 3 #Floor Division
print(10 % 3) # 1 #Modulus
print(2 ** 3) # 8 #Exponent or power

# Comparison operators -> boolean T/F
print(10 == 11) # False 
print(10 != 11) # True
print(10 > 11) # False 
print(10 < 11) # True 
print(10 >= 11) # False 
print(10 <= 11) # True 

# Assignment operators ->
a = 10 
print(a) # 10
a += 10  # a + 10 = 20
print(a) # 20
a -= 10  # a - 10 = 10
print(a) # 10
a *= 10  # a * 10 = 100
print(a) # 100
a /= 10  # a / 10 = 10.0
print(a) # 10.0
a %= 10  # a % 10 = 0.0
print(a) # 0.0
a **= 2  # a ** 2 = 0.0
print(a) # 0.0
a = 5    # 5
a //= 2  # a // 2 = 2
print(a) # 2

# Logical operators ->
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) # True
a = (5 > 4) and (2 < 3) # True
a = (5 > 4) or (2 > 3)  # True
a = not(5 > 4)  # False

# identity operators ->
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a != b) # False
print(a is b) # False
print(a is not b) # True

# membership operators ->
a = [1,2,3,4,5]
print(1 in a) # True
print(6 in a) # False
print(1 not in a) # False
print(6 not in a) # True

# Bitwise operators -> operate on binary values
a = 2 # 0010
b = 3 # 0011
print(a & b) # 0010 = 2 #Bitwise AND
print(a | b) # 0011 = 3 #Bitwise OR
print(a ^ b) # 0001 = 1 #Bitwise XOR
a = 5
print(~ a) # -6  (~a = -(a+1))
print(~ (-a)) # 4 (~a = (-a - 1 = 1))
print(a << b) # 100000 = 16 #Bitwise Left Shift
print(a >> b) # 0000 = 0 #Bitwise Right Shift

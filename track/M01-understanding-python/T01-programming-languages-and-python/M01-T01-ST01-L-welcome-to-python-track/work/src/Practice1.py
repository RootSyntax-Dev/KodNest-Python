num = int(input("Enter a number: "))

if num < 0:
    print("Number is negative")
elif num > 0:
    print("Number is positive")
else:
    print("Number is zero")

# Program 2:
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to donate blood.")
else:
    print("Not eligible to donate blood.")

# Program 3:
temp = int(input("Enter temperature: "))

if temp > 30:
    print("Hot Day")
else:
    print("Cool Day")

# Program 4:
attended = int(input("Enter a attended classes: "))
total_classes = int(input("Enter total classes: "))
if attended >= 0.75 * total_classes:
    print("Eligible to sit in exam")
else:
    print("Not Eligible to sit in exam")

# Program 5: 
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Program 6:
age = int(input("Enter a age: "))

if age > 18:
    print("You can apply driving license.")
else:
    print("You can't apply driving license.")

# Program 7:
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a Leap year")

# Program 8:
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num1 > num2:
    print("Number 1 is greater than Number 2") 
elif num2 > num1:
    print("Number 2 is greater than Number 1")
else:
    print("Both numbers are equal.")

# Program 9:
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Fail")
    
# Program 10:
elec_usage = int(input("Enter Electricity Usage in units: "))

if elec_usage > 500:
    print("Usage High")
elif elec_usage >= 301 and elec_usage <= 500:
    print("Usage Medium")
elif elec_usage >= 101 and elec_usage <= 300:
    print("Usage Low")
else:
    print("Usage Very Low")

# Program 11:
marks = int(input("Enter your marks: "))
income = int(input("Enter your family income: "))
if marks >= 85 and income < 300000:
    print("You are eligible for the scholarship.")
else:
    print("Not eligible for the scholarship.")

# Program 12:
username = str(input("Enter username: "))
password = str(input("Enter password: "))

if username == "admin" and password == "admin":
    print("Login successful")
else:
    print("Login failed")

# Program 13:
num = int(input("Enter Day number: "))
if num == 1:
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
else:
    print("Invalid day number.")

# Program 14:
month = int(input("Enter Month number: "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Summer")
elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Rainy")
elif month == 10 or month == 11:
    print("Autumn")
else:
    print("You entered an Invalid Month number.")

# Program 15:
for i in range(20):
    print(i)

# Program 16:
num = int(input("Enter a number: "))

for i in range(10):
    print(num ," x ",i+1," = ", num * (i + 1))

# Program 17:
for i in range(10, 0, -1):
    print(i)

# Program 18:
num = int(input("Enter a number: "))
fact = 1
for i in range(num):
    fact = fact * (i+1)
print("Factorial of", num, "is:", fact)

# Program 19:
for i in range(1, 21):
    if i == 16:
        break
    print(i)

# Program 20:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 5
for i in number:
    if i == num:
        print(i, "Present in the list.")
        break

# Program 21:
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# Program 22:
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)

# Program 23:
def largest(num1, num2):
  if num1 > num2:
    print("Largest number is:", num1)
  elif num2 > num1:
    print("Largest number is:", num2)
  else:
    print("Both numbers are equal.")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

largest(num1, num2)

# Program 24:
def display():
    pass

display()
print("Program 1 Completed!")

# Program 25:
class Student():
    pass

s1 = Student()
print("Program 2 Completed!")
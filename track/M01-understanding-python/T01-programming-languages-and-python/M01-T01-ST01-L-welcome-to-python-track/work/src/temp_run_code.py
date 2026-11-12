def find_anagram(str1, str2):
    if len(str1) != len(str2):
        return "Not Anagram"
    
    for ch in str1:
        count1 = 0
        count2 = 0
        
        for i in str1:
            if i == ch:
                count1 += 1
        
        for j in str2:
            if j == ch:
                count2 += 1
    
        if count1 != count2:
            return "Not Anagram"

    return "Anagram"

str1 = "listen"
str2 = "silent"

print(find_anagram(str1, str2))


# Revise the left problems ->

# ================ 05/11/2026 =================
n = int(input())

while n > 0:
  print(n)
  n = n - 1

n = int(input())
for i in range(1, n + 1):
  if i % 2 == 0:
    print(i)
  else:
    continue

n = int(input())
for i in range(1, n + 1):
  if i % 2 != 0:
    print(i)
  else:
    continue

n = int(input())
total = 0
for i in range(1, n + 1):
  total = total + i

print(total)

n = int(input())

for i in range(1, 11):
  print(n, "X", i, "=", n*i)

n = int(input())
target = int(input())
count = 0

for i in range(1, n + 1):
  if i % target == 0:
    count += 1
    print(i)
  else:
    continue

print(f"Total number are divisible by {target} is: {count}")

n = int(input())
total = 0

for i in range(1, n + 1):
  if i % 2 == 0:
    total += i
  else:
    continue

print(total)

n = int(input())
total = 0

for i in range(1, n + 1):
  square = i * i
  total = total + square

print(total)

n = int(input())
count = 0

while n > 0:
  digit = n % 10
  count += 1
  n = n // 10

print("total digits are:", count)

n = int(input())
total = 0

while n > 0:
  digit = n % 10
  total = total + digit
  n = n // 10

print("Sum of all digits:", total)

n = int(input())
reverse = 0

while n > 0:
  digit = n % 10
  reverse = (reverse * 10) + digit
  n = n // 10

print("reverse digit:", reverse)

n = int(input())
origin = n
reverse = 0

while n > 0:
  digit = n % 10
  reverse = (reverse * 10) + digit
  n = n // 10

if reverse == origin:
  print("Palindrom")
else:
  print("Not Palindrom")

n = int(input())
largest = float("-inf")

while n > 0:
  digit = n % 10
  if digit > largest:
    largest = digit
  n = n // 10

print("Largest digit is:", largest)

n = int(input())
smallest = float("+inf")

while n > 0:
  digit = n % 10
  if digit < smallest:
    smallest = digit
  n = n // 10

print("Smallest digit is:", smallest)

n = int(input())
even = 0
odd = 0

while n > 0:
  digit = n % 10
  if digit % 2 == 0:
    even += 1
  else:
    odd += 1
  n = n // 10

print("total even:", even)
print("total odd:", odd)

n = int(input())
origin = n
total = 0
count = len(str(n))

while n > 0:
  digit = n % 10
  arm = digit ** count
  total = total + arm
  n = n // 10

if total == origin:
  print("Armstrong")
else:
  print("Not Armstrong")


# Right-Angle Triangle Pattern.
n = int(input("enter the value of rows: "))
for i in range(n):
    for j in range(0, i + 1):
        print("*", end="")
    print()

# Hollow Rectangle Pattern.
rows = int(input("Enter rows: "))
colm = int(input("Enter columns: "))
for i in range(rows):
    for j in range(colm):
        if i == 0 or i == rows - 1 or j == 0 or j == colm - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Cross Pattern.
rows = int(input("Enter rows: "))
colm = int(input("Enter columns: "))

for i in range(rows):
    for j in range(colm):
        if i == 1 or j == 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Alphabets Piramid Pattern.
rows = int(input("Enter rows: "))

for i in range(0, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()

# Diamond Pattern
'''
       *
     * * *
   * * * * *
   * * * * *
     * * *
       *
'''
rows = int(input("Enter rows: "))

# Upper half
for i in range(1, rows + 1):
    for j in range(rows - i):
        print("  ", end="")
    for j in range(2 * i - 1):
        print("* ", end="")
    print()

# Lower half
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print("  ", end="")
    for j in range(2 * i - 1):
        print("* ", end="")
    print()

#  Hollow diamond pattern:
'''
       *
     *   *
   *       *
   *       *
     *   *
       *
'''
n = int(input("Enter rows: "))

# Upper part-
for i in range(1, n + 1):
  for j in range(n - i):
    print(" ", end='')

  for j in range(1, 2 * i):
    if j == 1 or j == 2 * i -1:
      print("*", end='')
    else:
      print(" ", end='')
  print()
  
# Lower part-
for i in range(n, 0, -1):
  for j in range(n - i):
    print(" ", end='')

  for j in range(1, 2 * i):
    if j == 1 or j== 2 * i - 1:
      print("*", end='')
    else:
      print(" ", end='')
  print()

# Digit Right-Angle Triangle:
'''
1
1 2
1 2 3
1 2 3 4
'''
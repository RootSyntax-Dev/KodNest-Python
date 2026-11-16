
# Lists

nums = [1, 2, 3, 4, 5]

print(nums)        # Print the complete list
print(type(nums)) # <class 'list'>
print(nums[2])    # Access element using index (3)


# List Constructor - list()

nums = list((1, 2, 3, 4, 5, 3))

print(nums)
print(type(nums)) # <class 'list'>


# Modifying List Elements

names = ["Vinay", "Ravi", "Bobby"]

names[1] = "Ram"  # Update element at index 1

print(names)
print(type(names))


# List Methods

names = ["Vinay", "Ravi", "Bobby"]

# 1. append() - Add one element at the end
names.append("Ram")
print(names)  # ['Vinay', 'Ravi', 'Bobby', 'Ram']

# 2. extend() - Add multiple elements
names.extend(["Charlie", "Sita"])
print(names)

# 3. insert() - Add element at a specific index
names.insert(2, "Rahul")
print(names)

# 4. remove() - Remove the specified element
names.remove("Ravi")
print(names)

# 5. pop() - Remove and return element (last by default)
names.pop()
print(names)

# 6. clear() - Remove all elements
names.clear()
print(names)  # []

# 7. index() - Return the index of an element
names = ["Vinay", "Ravi", "Bobby", "Ravi"]
print(names.index("Bobby"))  # 2

# 8. count() - Count occurrences of an element
print(names.count("Ravi"))   # 2

# 9. sort() - Sort elements in ascending order
n = [5, 7, 8, 2, 1]
n.sort()
print(n)  # [1, 2, 5, 7, 8]

# Sort in descending order
n.sort(reverse=True)
print(n)  # [8, 7, 5, 2, 1]

# 10. reverse() - Reverse the existing order
n = [1, 2, 3, 4, 5]
n.reverse()
print(n)  # [5, 4, 3, 2, 1]

# 11. copy() - Create a shallow copy of the list
original = [10, 20, 30]
new_list = original.copy()

print(original)
print(new_list)

# replace one color with two colors using slice assignment

colors = ["red", "green", "yellow", "blue", "black"]
colors[1:2] = ["white","purple"] # slice assignment
print(colors)
# Deleting a List

names = ["Vinay", "Ravi", "Bobby"]

del names  # Delete the complete list

# print(names)  # NameError: names is not defined


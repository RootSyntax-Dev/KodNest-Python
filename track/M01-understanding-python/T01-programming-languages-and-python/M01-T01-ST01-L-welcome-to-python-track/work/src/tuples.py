# ── Tuple: ordered, immutable, allows duplicates ──────────────────────────────
nums = (1, 2, 3, 4, 5)
print(nums, type(nums))

# Indexing & Slicing — same rules as lists (0-based, [start:stop])
stu_info = ("Gamana", True, 8.18, 23)
print(stu_info)
print(stu_info[3])       # last element → 23
print(stu_info[0:3])     # slice → ("Gamana", True, 8.18)

# Repetition operator (*) — repeats the tuple n times
name = ("vinay",) * 3
print(name)
print(type(name))

# ── Tuple Constructor ──────────────────────────────────────────────────────────
# tuple() converts any iterable (list, string, etc.) into a tuple
lst = [1, 2, 3, 4]
print(lst, type(lst))
rgb = tuple(lst)         # list → tuple
print(rgb, type(rgb))

rgb = tuple(["r", "e", "d"])
print(rgb)
print(type(rgb))

# ── Workaround: add an element to a tuple ─────────────────────────────────────
# Tuples are immutable, so convert to list → append → back to tuple if needed
x = (1, 2, 3)
y = list(x)
y.append(4)             # append works on the list copy
print(y)

# ── Concatenation & Removal ────────────────────────────────────────────────────
# += concatenates two tuples (creates a new tuple internally)
x = (1, 2, 3, 4)
z = (10, 20, 30)
print(z)
x += z                  # x is now (1, 2, 3, 4, 10, 20, 30)
print(x)
y = list(x)             # convert to list for mutable operations
print(y)

# ── Iterating over a tuple ────────────────────────────────────────────────────
z = (10, 11, 12, 10)
for i in range(len(z)):
    print(z[i])

# ── Tuple Methods (only 2 built-in) ───────────────────────────────────────────
print(z.count(10))      # count() → number of times 10 appears
print(z.index(10))      # index() → first occurrence index of 10
print(z.index(10, 2))   # index(value, start) → search from index 2 onwards

# ── Tuple Unpacking ───────────────────────────────────────────────────────────
# Assign each element directly to named variables (must match count)
emp = ("Gamana", 23, "Developer")
print(emp, type(emp))
(name, age, role) = emp
print(name)
print(age)
print(role)

# ── Extended Unpacking with * (star/splat) ────────────────────────────────────
# *b collects all middle elements into a list
s = (2, 3, 4, 5, 6)
(a, *b, c) = s          # a=2, b=[3,4,5], c=6
print(a)
print(b)
print(c)

# ── Built-in Functions on Tuples ──────────────────────────────────────────────
t = (10, 20, 30, 40, 50)

print(len(t))           # number of elements
print(max(t))           # largest value
print(min(t))           # smallest value
print(sum(t))           # sum of all elements
print(sorted(t))        # returns a sorted LIST (tuple stays unchanged)
print(any(t))           # True if at least one element is truthy
print(all(t))           # True if ALL elements are truthy
print(10 in t)          # membership test → True/False

# ── Tuple Operators ───────────────────────────────────────────────────────────
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)          # concatenation → (1, 2, 3, 4)
print(t1 * 2)           # repetition  → (1, 2, 1, 2)

# del removes the variable binding; the tuple itself is garbage-collected
del t

# rename -> alisis
stu_info = ["Ram", 23]
stu = stu_info

print(stu)
print(stu_info)
print(stu is stu_info)

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x + y)
print(x, y)
print(x is y)
print(x == y)
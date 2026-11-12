# Inbuild string methods - single program
s = "  KodNest Technologies 123  "

print("Original string:", s)

# Case Conversition method
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())

#Searching & Counting
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))

# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))

# Start & End Check
print("startswith('  kod'):", s.startswith("  kod"))
print("endswith('123  '):", s.endswith("123  "))

# Split & join
words = s.split()
print("split():", words)
print("join():", "-".join(words))

# Strip Spaces
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())

# Checking methods
print("isalpha():", s.isalpha())
print("isdigit():", s.isdigit())
print("isalnum():", s.isalnum())

# Length
print("Length of string:", len(s))
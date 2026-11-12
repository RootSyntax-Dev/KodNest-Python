# ============================================================
# Variable Scope in Python (Global vs Local Variables)
# ============================================================

# ------------------------------------------------------------
# 1. Using Global and Local Variables with 'global' Keyword
# ------------------------------------------------------------
c = 30  # Global variable (accessible anywhere in the file)

def add():
    global a      # Declares 'a' as a global variable inside the function
    a = 10        # Global variable (assigned value using the 'global' keyword)
    b = 20        # Local variable (accessible only inside this function)
    print(a + b)  # Prints sum of global variable 'a' and local variable 'b'
    print(c)      # Accesses and prints global variable 'c'

# Calling the function
add()


# ------------------------------------------------------------
# 2. Variable Shadowing (Local Variable with Same Name as Global)
# ------------------------------------------------------------
x = 100  # Global variable

def display():
    x = 50                # Local variable (shadows the global 'x' inside display())
    print("Local x:", x)  # Prints the local variable 'x'

# Calling the function
display()
print("Global x:", x)     # Prints the global variable 'x' (remains unchanged)


# ------------------------------------------------------------
# 3. Reading Global Variable Inside a Function & Reassigning
# ------------------------------------------------------------
x = 10  # Global variable

def display():
    print(x)  # Accesses and prints global variable 'x'
    print(x)  # Accesses and prints global variable 'x'

# Calling the function
display()

x = 30    # Reassigning/updating the global variable 'x'
print(x)  # Prints the updated global variable 'x'
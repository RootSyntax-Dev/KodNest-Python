# Recuesive function.
def count(n):
  if n == 0: # this is a Base-case
    return
  print(n)
  count(n-1)

count(5)

# factorial number.
def fact_number(n):
  if n == 0 or n == 1: # this is a Base-case
    return 1
  else:
    return n * fact_number(n - 1)

print(fact_number(5))

# print Fibonacci Series.
def fib(n):
    if n == 0: # Base-case
        return 0
    elif n == 1: # Base-case
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(10)) # its print 11th fibonacci number. Because starts with 0


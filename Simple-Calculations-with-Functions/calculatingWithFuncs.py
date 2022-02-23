'''
Date: 08/2021

@author Filip J. Cierkosz
'''

# Make simple math calculations using functions.

# Digits.
zero = lambda f=None: f(0) if (f) else 0
one = lambda f=None: f(1) if (f) else 1
two = lambda f=None: f(2) if (f) else 2
three = lambda f=None: f(3) if (f) else 3
four = lambda f=None: f(4) if (f) else 4
five = lambda f=None: f(5) if (f) else 5
six = lambda f=None: f(6) if (f) else 6
seven = lambda f=None: f(7) if (f) else 7
eight = lambda f=None: f(8) if (f) else 8
nine = lambda f=None: f(9) if (f) else 9

# Mathematical operations.
# Addition.
def add(b): return lambda a: a+b
# Subtraction.
def sub(b): return lambda a: a-b
# Multiplication
def mult(b): return lambda a: a*b
# Division.
def div(b): return lambda a: int(a/b)

# Test harness.
print(six(mult(nine())))     # returns 54
print(zero(sub(seven())))    # returns -7
print(two(add(four())))      # returns 6
print(nine(div(three())))    # returns 3

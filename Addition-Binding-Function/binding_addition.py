'''
Binding function for performing addition

Date: 06/2021

Author: Filip J. Cierkosz
'''

from functools import partial

# Addition of 5 numbers implementing a binding function.
def add(a,b,c,d,e):
    return a+b+c+d+e

# Test harness.
add_one = partial(add, 1)
add_two = partial(add_one, 2)
add_three = partial(add_two, 3)
add_four = partial(add_three, 4)
print(add_four(5))

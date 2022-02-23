'''
Date: 06/2021

@author Filip J. Cierkosz
'''

from functools import partial

# Addition of 5 numbers implementing a binding function.
def add(a,b,c,d,e):
    return a+b+c+d+e

# Test harness.
addOne = partial(add, 1)
addTwo = partial(addOne, 2)
addThree = partial(addTwo, 3)
addFour = partial(addThree, 4)
print(addFour(5))

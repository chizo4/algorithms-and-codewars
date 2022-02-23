'''
Date: 05/2021

@author Filip J. Cierkosz
'''

# Implementation of chain adding function.
class add(int):
    def __call__(self, n):
        return add(self+n)

# Test harness.
print(add(1)(2)(3))
print(add(1)(2)(3)(400)(5)(6)(-100)(0))
print(add(12))
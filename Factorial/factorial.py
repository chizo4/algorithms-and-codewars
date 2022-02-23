'''
Date: 07/2021

@author Filip J. Cierkosz
'''

import sys

# The default recursion is about 1000. It can be set higher manually.
sys.setrecursionlimit(4000)

# Function to recursively get the factioral of a number.
def factorial(n):
    if (n<0): return None
    elif (n==0 or n==1): return 1
    else: return n*factorial(n-1)

# Test harness.
# A separate datafile is created to write the result of the factorial
# function, since the number might be huge.
print(factorial(3000), file=open("factorialWrite.txt", "w"))

'''
Simple array subtraction

Date: 05/2021

Author: Filip J. Cierkosz
'''

def array_subtract(one, two):
    diff = []

    for el in one:
        if (not el in two):
            diff.append(el)

    return diff

# Test harness.
print(array_subtract([1,2,2,3,3,4,6,6,6],[1,3,2,4]))
'''
The QuickSort algorithm.

quickSort.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

def quickSort(arr):
    if (len(arr)<=1):
        return arr

    pivot = arr[-1]
    lessThanPivot = []
    greaterThanPivot = []
    
    for el in arr[:-1]:
        if (el<=pivot):
            lessThanPivot.append(el)
        else:
            greaterThanPivot.append(el)

    return quickSort(lessThanPivot)+[pivot]+quickSort(greaterThanPivot)

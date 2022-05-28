'''
The QuickSort algorithm.

quick_sort.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

def quick_sort(arr):
    if (len(arr)<=1):
        return arr

    pivot = arr[-1]
    less_than_pivot = []
    greater_than_pivot = []
    
    for el in arr[:-1]:
        if (el<=pivot):
            less_than_pivot.append(el)
        else:
            greater_than_pivot.append(el)

    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)

'''
Sort only odd numbers in the array so that all 
the even elements are left untouched.

sort_only_odd.py

Date: 06/2021

Author: Filip J. Cierkosz
'''

def sort_odd(arr):
    arr_odd_sort = sorted([i for i in arr if (i%2==1)])
    index = 0

    # Replace all the odd elements in the original array with the 
    # sorted ones.
    for i in range(len(arr)):
        if (arr[i]%2==1):
            arr[i] = arr_odd_sort[index]
            index += 1 

    return arr

'''
The MergeSort algorithm.

mergeSort.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

def divide(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return left, right


def merge(left, right):
    arr = []
    i = 0
    j = 0

    while (i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while (i<len(left)):
        arr.append(left[i])
        i += 1

    while (j<len(right)):
        arr.append(right[j])
        j += 1

    return arr

def mergeSort(arr):
    '''
    Sort an array in ascending order.

    1. Divide: Find the midpoint of the array, then divide into subarrays.
    2. Conquer: Recursively sort the subarrays.
    3. Combine: Merge the sorted subarrays into one final sorted array.

    The algorithm takes O(n log n) time.
    '''

    if (len(arr)<=1):
        return arr

    leftArr, rightArr = divide(arr)
    left = mergeSort(leftArr)
    right = mergeSort(rightArr)

    return merge(left, right)

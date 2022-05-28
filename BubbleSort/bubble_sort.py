'''
The BubbleSort algorithm.

bubble_sort.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

def bubble_sort(arr):
    i = len(arr)-1

    while (i>0):
        j = 0

        while (j<i):
            if (arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

            j += 1

        i -= 1

    return arr

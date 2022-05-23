'''
The BubbleSort algorithm.

bubbleSort.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

def bubbleSort(arr):
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

'''
Date: 06/2021

@author Filip J. Cierkosz
'''

# Function to sort only odd numbers in the array so that all the even
# elements are left untouched.
def sortArr(arr):
    # Create an array of sorted odd numbers from the input array.
    arrOddSort = sorted([i for i in arr if (i%2==1)])
    index = 0

    # Replace all the odd elements in the original array with the 
    # sorted ones.
    for i in range(len(arr)):
        if (arr[i]%2==1):
            arr[i] = arrOddSort[index]
            index += 1 

    # Return the appropriately sorted array.
    return arr

# Test harness.
print(sortArr([101,1,2,3,6,86,81,23]))
print(sortArr([7,3,5,2,2,4,1,0,6]))

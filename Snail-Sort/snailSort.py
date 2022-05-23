'''
Date: 01/2022

@author Filip J. Cierkosz
'''

import numpy as np

# Function to perform the snail sort algorithm on an array. The function
# returns a modified version of the input array so that it is arranged from
# outermost elements to the middle element, traveling clockwise.
def snail(arrIn):
    if (len(arrIn)<2):
        return arrIn[0]
    else:
        arrSnail = np.empty(int(len(arrIn[0])**2), dtype=int)
        currIndex = 0

        rowUp = 0
        colRight = len(arrIn[0])-1
        rowBottom = len(arrIn)-1
        colLeft = 0

        # Repeat as long as the index of the left column does not exceed 
        # the index of the right column, and the upper row does not exceed
        # the index of the bottom row. The rules are straightforward - 
        # retrieve the values following the order while iteration:
        # upper row->right column->bottom row->left column (if needed, repeat).
        while (rowUp<=rowBottom and colLeft<=colRight):
            # Append all the elements from the upper row of the array.
            for i in range(colLeft, colRight+1):
                arrSnail[currIndex] = arrIn[rowUp][i]
                currIndex += 1
            # Increment the row, i.e. go one row down.
            rowUp += 1

            # Append all the elements from the right column.
            for i in range(rowUp, rowBottom+1):
                arrSnail[currIndex] = arrIn[i][colRight]
                currIndex += 1 
            # Decrement the column, i.e. go one column to the left.
            colRight -= 1

            # Append all the elements from the bottom row of the array.
            if (rowUp<=rowBottom):
                for i in range(colRight, colLeft-1, -1):
                    arrSnail[currIndex] = arrIn[rowBottom][i]
                    currIndex += 1
            # Decrement the row, i.e. go one row up.
            rowBottom -= 1

            # Append all the elements from the left column of the array.
            if (colLeft<=colRight):
                for i in range(rowBottom, rowUp-1, -1):
                    arrSnail[currIndex] = arrIn[i][colLeft]
                    currIndex += 1
            # Increment the column, i.e. go one column to the right.
            colLeft += 1

        return arrSnail

# Test harness.
arrZero = [[]]
arrOne = [[1]]
arrTwo = np.reshape([1,2,3,8,9,4,7,6,5], (3,3))
arrThree = np.reshape([i for i in range(1,26)], (5, 5))
arrFour = np.reshape([i for i in range(1,82)], (9,9))

print(snail(arrZero))
print(snail(arrOne))
print(snail(arrTwo))
print(snail(arrThree))
print(snail(arrFour))

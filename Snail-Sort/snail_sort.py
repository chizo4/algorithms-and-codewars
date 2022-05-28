'''
Perform the snail sort algorithm on an array. The function 
returns a modified version of the input array so that it is
arranged from outermost elements to the middle element, 
traveling clockwise.

snail_sort.py

Date: 01/2022

Author: Filip J. Cierkosz
'''

import numpy as np

def snail(arr_in):
    if (len(arr_in)<2):
        return arr_in[0]
    else:
        arr_snail = np.empty(int(len(arr_in[0])**2), dtype=int)
        curr_index = 0

        row_up = 0
        col_right = len(arr_in[0])-1
        row_bottom = len(arr_in)-1
        col_left = 0

        # Repeat as long as the index of the left column does not exceed 
        # the index of the right column, and the upper row does not exceed
        # the index of the bottom row. The rules are straightforward - 
        # retrieve the values following the order while iteration:
        # upper row->right column->bottom row->left column (if needed, repeat).
        while (row_up<=row_bottom and col_left<=col_right):
            # Append all the elements from the upper row of the array.
            for i in range(col_left, col_right+1):
                arr_snail[curr_index] = arr_in[row_up][i]
                curr_index += 1
            # Increment the row, i.e. go one row down.
            row_up += 1

            # Append all the elements from the right column.
            for i in range(row_up, row_bottom+1):
                arr_snail[curr_index] = arr_in[i][col_right]
                curr_index += 1 
            # Decrement the column, i.e. go one column to the left.
            col_right -= 1

            # Append all the elements from the bottom row of the array.
            if (row_up<=row_bottom):
                for i in range(col_right, col_left-1, -1):
                    arr_snail[curr_index] = arr_in[row_bottom][i]
                    curr_index += 1
            # Decrement the row, i.e. go one row up.
            row_bottom -= 1

            # Append all the elements from the left column of the array.
            if (col_left<=col_right):
                for i in range(row_bottom, row_up-1, -1):
                    arr_snail[curr_index] = arr_in[i][col_left]
                    curr_index += 1
            # Increment the column, i.e. go one column to the right.
            col_left += 1

        return arr_snail

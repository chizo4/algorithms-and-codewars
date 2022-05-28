'''
Palindrome checker.

palindrome.py

Date: 03/2022

Author: Filip J. Cierkosz
'''

from dequeue import Dequeue

def is_palindrome(in_str):
    # Instantiate and populate the dequeue using 
    # the chars of the input string.
    dq = Dequeue()
    [dq.add_back(c) for c in in_str]

    while (dq.get_size()>=2):
        # Remove and get the first and last element 
        # from the Dequeue.
        first = dq.remove_front()
        last = dq.remove_back()
        
        # If they are not the same, it is not a palindrome!
        if (first!=last): 
            return False

    return True

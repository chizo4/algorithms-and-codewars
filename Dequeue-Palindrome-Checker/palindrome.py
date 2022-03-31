'''
Palindrome checker.

palindrome.py

Date: 03/2022

Author: Filip J. Cierkosz
'''

from dequeue import Dequeue

def isPalindrome(inStr):
    # Instantiate and populate the dequeue using 
    # the chars of the input string.
    dq = Dequeue()
    [dq.addBack(c) for c in inStr]

    while (dq.getSize()>=2):
        # Remove and get the first and last element 
        # from the Dequeue.
        first = dq.removeFront()
        last = dq.removeBack()
        
        # If they are not the same, it is not a palindrome!
        if (first!=last): return False

    return True

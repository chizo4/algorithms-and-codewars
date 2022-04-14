'''
Palindrome checker using recursion.

palindrome.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

def checkPalindrome(s):
    if (len(s)<=1):
        return True
    elif (s[0]==s[-1] and len(s)==2):
        return True
    elif (s[0]==s[-1] and len(s)>2):
        return checkPalindrome(s[1:-1])

    return False

'''
Testing for palindrome checker.

test_palindrome.py

Date: 03/2022

Author: Filip J. Cierkosz
'''

from palindrome import is_palindrome
import unittest

# Unit test cases for palindrome checker function.
class TestIsPalindrome (unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('mom'))
        self.assertFalse(is_palindrome('nba'))
        self.assertTrue(is_palindrome('civic'))
        self.assertFalse(is_palindrome('nothing'))
        self.assertFalse(is_palindrome('palindrome'))
        self.assertFalse(is_palindrome('testet'))
        self.assertTrue(is_palindrome('level'))

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
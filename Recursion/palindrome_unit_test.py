'''
Testing for recursive palindrome checker.

palindrome_unit_test.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from palindrome import check_palindrome
import unittest

# Unit test cases for recursive palindrome checker function.
class TestIsPalindrome (unittest.TestCase):
    def test_check_palindrome(self):
        self.assertTrue(check_palindrome('aibohphobia'))
        self.assertTrue(check_palindrome('mom'))
        self.assertFalse(check_palindrome('nba'))
        self.assertTrue(check_palindrome('civic'))
        self.assertFalse(check_palindrome('nothing'))
        self.assertFalse(check_palindrome('palindrome'))
        self.assertFalse(check_palindrome('testet'))
        self.assertTrue(check_palindrome('level'))

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
'''
Testing for palindrome checker.

testPalindrome.py

Date: 03/2022

Author: Filip J. Cierkosz
'''

from palindrome import isPalindrome
import unittest

# Unit test cases for palindrome checker function.
class TestIsPalindrome (unittest.TestCase):
    def testIsPalindrome(self):
        self.assertTrue(isPalindrome('mom'))
        self.assertFalse(isPalindrome('nba'))
        self.assertTrue(isPalindrome('civic'))
        self.assertFalse(isPalindrome('nothing'))
        self.assertFalse(isPalindrome('palindrome'))
        self.assertFalse(isPalindrome('testet'))
        self.assertTrue(isPalindrome('level'))

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
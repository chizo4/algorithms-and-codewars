'''
Testing for recursive palindrome checker.

testPalindrome.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from palindrome import checkPalindrome
import unittest

# Unit test cases for recursive palindrome checker function.
class TestIsPalindrome (unittest.TestCase):
    def testCheckPalindrome(self):
        self.assertTrue(checkPalindrome('aibohphobia'))
        self.assertTrue(checkPalindrome('mom'))
        self.assertFalse(checkPalindrome('nba'))
        self.assertTrue(checkPalindrome('civic'))
        self.assertFalse(checkPalindrome('nothing'))
        self.assertFalse(checkPalindrome('palindrome'))
        self.assertFalse(checkPalindrome('testet'))
        self.assertTrue(checkPalindrome('level'))

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
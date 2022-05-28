'''
Test cases for the algorithm.

unit_test.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from sort_only_odd import sort_odd
import unittest

class TestSortOnlyOdd (unittest.TestCase):
    def test_one(self):
        res = sort_odd([2,4,3,1])
        self.assertEqual(res, [2,4,1,3])

    def test_two(self):
        res = sort_odd([5,7,9,3,1,8])
        self.assertEqual(res, [1,3,5,7,9,8])

    def test_three(self):
        res = sort_odd([0,2,4,6,7])
        self.assertEqual(res, [0,2,4,6,7])

# Run all the cases.
if (__name__=='__main__'):
    unittest.main()
'''
Test cases for the snail sort algorithm.

snail_sort_unit_test.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from snail_sort import snail
import numpy as np
import unittest

class TestSnailSort(unittest.TestCase):
    def test_case_one(self):
        arr = [[]]
        res = snail(arr)
        self.assertEqual(res, [])

    def test_case_two(self):
        arr = [[1]]
        res = snail(arr)
        self.assertEqual(res, [1])

    def test_case_three(self):
        arr = np.reshape([1,2,3,8,9,4,7,6,5], (3,3))
        res = snail(arr)
        equal = (res==np.asarray([i for i in range(1,10)])).all()
        self.assertTrue(equal)

    def test_case_four(self):
        arr = np.reshape([i for i in range(1,26)], (5,5))
        res = snail(arr)
        equal = (res==np.asarray([1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13])).all()
        self.assertTrue(equal)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
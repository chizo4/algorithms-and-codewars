'''
Test cases for QuickSort.

quick_sort_unit_test.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from quick_sort import quick_sort
from numpy import random
import unittest

class TestQuickSort (unittest.TestCase):
    # Test 10 random sample arrays in one run.
    def test_rand_arr(self):
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = quick_sort(arr.copy())
            arr.sort()
            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

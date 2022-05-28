'''
Test cases for MergeSort algorithm.

merge_sort_unit_test.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from merge_sort import merge_sort
from numpy import random
import unittest

class TestMergeSort (unittest.TestCase):
    # Tes 10 random sample arrays.
    def test_rand_arr(self):
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = merge_sort(arr.copy())
            arr.sort()

            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

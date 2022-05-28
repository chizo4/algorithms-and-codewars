'''
Test cases for the implementation of BubbleSort algorithm.

bubble_sort_unit_test.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from bubble_sort import bubble_sort
from numpy import random
import unittest

class TestBubbleSort (unittest.TestCase):
    def test_rand_arr(self):
        # Tes 10 random sample arrays.
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = bubble_sort(arr.copy())
            arr.sort()

            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

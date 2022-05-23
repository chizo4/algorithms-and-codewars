'''
Test cases for QuickSort.

quickSortUnitTest.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from quickSort import quickSort
from numpy import random
import unittest

class TestQuickSort (unittest.TestCase):
    # Tes 10 random sample arrays.
    def testRandArr(self):
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = quickSort(arr.copy())
            arr.sort()

            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

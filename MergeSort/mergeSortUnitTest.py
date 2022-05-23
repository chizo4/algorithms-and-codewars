'''
Test cases for MergeSort.

mergeSortUnitTest.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from mergeSort import mergeSort
from numpy import random
import unittest

class TestMergeSort (unittest.TestCase):
    # Tes 10 random sample arrays.
    def testRandArr(self):
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = mergeSort(arr.copy())
            arr.sort()

            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

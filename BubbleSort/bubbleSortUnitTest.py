'''
Test cases for BubbleSort.

bubbleSortUnitTest.py

Date: 04/2022

Author: Filip J. Cierkosz
'''

from bubbleSort import bubbleSort
from numpy import random
import unittest

class TestBubbleSort (unittest.TestCase):
    def testRandArr(self):
        # Tes 10 random sample arrays.
        for i in range(10):
            arr = [random.randint(1000000) for i in range(1000)]
            res = bubbleSort(arr.copy())
            arr.sort()

            self.assertEqual(res, arr)

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()

'''
Test cases.

unit_test_date.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from date_by_day import get_date
import unittest

class TestGetDate (unittest.TestCase):
    def test_one(self):
        date = get_date(41, False)
        res = 'February, 10'
        self.assertEqual(date, res)

    def test_two(self):
        date = get_date(60, False)
        res = 'March, 1'
        self.assertEqual(date, res)

    def test_three(self):
        date = get_date(60, True)
        res = 'February, 29'
        self.assertEqual(date, res)

    def test_four(self):
        date = get_date(365, False)
        res = 'December, 31'
        self.assertEqual(date, res)

    def test_five(self):
        date = get_date(100, True)
        res = 'April, 9'
        self.assertEqual(date, res)

    def test_six(self):
        date = get_date(366, True)
        res = 'December, 31'
        self.assertEqual(date, res)

# Run test cases.
if (__name__=='__main__'):
    unittest.main()
'''
Test cases for PIN guesser.

guesser_pin_unit_test.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from guesser_pin import crack
import hashlib
import unittest

class TestPinGuesser (unittest.TestCase):
    def test_one(self):
        orig_pin = '12345'
        hash_sample = hashlib.md5(orig_pin.encode("utf-8")).hexdigest()
        res = crack(hash_sample)
        self.assertEqual(res, orig_pin)

    def test_two(self):
        orig_pin = '00000'
        hash_sample = hashlib.md5(orig_pin.encode("utf-8")).hexdigest()
        res = crack(hash_sample)
        self.assertEqual(res, orig_pin)

    def test_three(self):
        orig_pin = '69069'
        hash_sample = hashlib.md5(orig_pin.encode("utf-8")).hexdigest()
        res = crack(hash_sample)
        self.assertEqual(res, orig_pin)

# Run cases.
if (__name__=='__main__'):
    unittest.main()
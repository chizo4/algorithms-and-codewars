'''
Test cases for password guesser.

password_guesser_unit_test.py

Date: 05/2022

Author: Filip J. Cierkosz

(NB: Running the cases takes a while.)
'''

from password_guesser import password_cracker
from hashlib import sha1
import unittest

class TestPasswordGuesser (unittest.TestCase):
    def test_sample_one(self):
        hash_one = sha1('tests'.encode()).hexdigest()
        res = password_cracker(hash_one, 6)
        self.assertEqual(res, 'tests')

    def test_sample_two(self):
        hash_two = sha1('fuc'.encode()).hexdigest()
        res = password_cracker(hash_two, 4)
        self.assertEqual(res, 'fuc')

    def test_sample_three(self):
        hash_three = sha1('tests'.encode()).hexdigest()
        res = password_cracker(hash_three, 2)
        self.assertEqual(res, 'There are no matches to the hash.')

    def test_sample_four(self):
        hash_four = sha1('longer'.encode()).hexdigest()
        res = password_cracker(hash_four, 7)
        self.assertEqual(res, 'longer')

# Run the test cases.
if (__name__=='__main__'):
    unittest.main()
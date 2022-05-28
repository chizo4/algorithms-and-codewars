'''
valid_ip_unit_test.py

Date: 02/2022

Author: Filip J. Cierkosz
'''

from valid_ip import check_ip_validity
import unittest

# Unit test cases for the IP validation function.
class TestValidIP (unittest.TestCase):
    def test_valid_ip_one(self):
        self.assertTrue(check_ip_validity('120.44.55.66'))

    def test_valid_ip_two(self):
        self.assertFalse(check_ip_validity('a,b.c.d'))

    def test_valid_ip_three(self):
        self.assertFalse(check_ip_validity('a.b.c.d'))

    def test_valid_ip_four(self):
        self.assertFalse(check_ip_validity('$.1.2.3'))

    def test_valid_ip_five(self):
        self.assertFalse(check_ip_validity('999.1.1.1'))

    def test_valid_ip_six(self):
        self.assertFalse(check_ip_validity('33.333.23.1'))

    def test_valid_ip_seven(self):
        self.assertTrue(check_ip_validity('1.2.3.4'))

    def test_valid_ip_eight(self):
        self.assertTrue(check_ip_validity('120.44.55.66'))

    def test_valid_ip_nine(self):
        self.assertFalse(check_ip_validity('10,.13.2.1'))

    def test_valid_ip_ten(self):
        self.assertFalse(check_ip_validity('100.1300.2.1'))

    def test_valid_ip_eleven(self):
        self.assertFalse(check_ip_validity('10.13.2.1.2'))

    def test_valid_ip_twelve(self):
        self.assertFalse(check_ip_validity('111...111.11.1'))

    def test_valid_ip_thirteen(self):
        self.assertFalse(check_ip_validity('111.111..111.11'))

    def test_valid_ip_fourteen(self):
        self.assertTrue(check_ip_validity('255.255.255.255'))
   
# Run all the test cases.
if (__name__=='__main__'):
    unittest.main()

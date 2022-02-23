'''
Date: 02/2022

@author Filip J. Cierkosz
'''

from validIP import checkIPValidity
import unittest

# Unit test cases for the IP validation function.
class TestValidIP (unittest.TestCase):
    def testValidIP(self):
        self.assertTrue(checkIPValidity('120.44.55.66'))
        self.assertFalse(checkIPValidity('a,b.c.d'))
        self.assertFalse(checkIPValidity('a.b.c.d'))
        self.assertFalse(checkIPValidity('a.1.2.3'))
        self.assertFalse(checkIPValidity('999.1.1.1'))
        self.assertFalse(checkIPValidity('33.333.23.1'))
        self.assertTrue(checkIPValidity('1.2.3.4'))
        self.assertTrue(checkIPValidity('120.44.55.66'))
        self.assertFalse(checkIPValidity('10,.13.2.1'))
        self.assertFalse(checkIPValidity('100.1300.2.1'))
        self.assertFalse(checkIPValidity('10.13.2.1.2'))
        self.assertFalse(checkIPValidity('111...111.11.1'))
        self.assertFalse(checkIPValidity('111.111..111.11'))
        self.assertTrue(checkIPValidity('255.255.255.255'))

if (__name__=='__main__'):
    unittest.main()

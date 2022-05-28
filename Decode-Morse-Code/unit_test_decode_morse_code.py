'''
Test cases for decoding the Morse Code.

unit_test_decode_morse_code.py

Date: 05/2022

Author: Filip J. Cierkosz
'''

from decode_morse_code import decode_morse
import unittest

class TestDecodeMorse(unittest.TestCase):
    def test_one(self):
        msg = decode_morse('.----  - . ... - .. -. --.  - .... .  -.-. --- -.. .')
        res = '1 TESTING THE CODE'
        self.assertEqual(msg, res)

    def test_two(self):
        msg = decode_morse('.--. -.-- - .... --- -.')
        res = 'PYTHON'
        self.assertEqual(msg, res)

    def test_three(self):
        msg = decode_morse('.--- .- ...- .-')
        res = 'JAVA'
        self.assertEqual(msg, res)

# Run all test cases.
if (__name__=='__main__'):
    unittest.main()
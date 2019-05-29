#!/usr/bin/env python

import unittest

from lcd_modules.lcd_display import LCDDisplay

#  '._.',   '...',   '._.',   '._.',   '...',   '._.',   '._.',   '._.',   '._.,'   '._.',
#  '|.|',   '..|',   '._|',   '._|',   '|_|',   '|_.',   '|_.',   '..|',   '|_|,'   '|_|',
#  '|_|',   '..|',   '|_.',   '._|',   '..|',   '._|',   '|_|',   '..|',   '|_|,'   '..|'

ZERO_DIGIT = [
            ' _ ',
            '| |',
            '|_|'
        ]
NINE_DIGIT = [
            ' _ ',
            '|_|',
            '  |'
        ]

class BaseTestCase(unittest.TestCase):
    """ Class to test the display module """

    dispay = LCDDisplay()

    def test_digits_length(self):
        value = self.dispay.get_digits('')
        self.assertEqual(len(value), 0)

        value = self.dispay.get_digits('1')
        self.assertEqual(len(value), 1)

        value = self.dispay.get_digits('1234')
        self.assertEqual(len(value), 4)

    def test_sigle_digit_value(self):
        value = self.dispay.get_digits('0')
        self.assertEqual(value[0].d, ZERO_DIGIT)
        value = self.dispay.get_digits('9')
        self.assertEqual(value[0].d, NINE_DIGIT)

    def test_multi_digit_value(self):
        value = self.dispay.get_digits('09')
        self.assertEqual(value[0].d, ZERO_DIGIT)
        self.assertEqual(value[1].d, NINE_DIGIT)

    def test_digits_to_print(self):
        expected_line =  " _       _ \n" 
        expected_line += "|_|   | | |\n"
        expected_line += "  |   | |_|\n"
        value = self.dispay.get_digits('910')
        #TODO line = self.dispay.prepare_to_print(value)
        #TODO self.assertEqual(line, expected_line)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
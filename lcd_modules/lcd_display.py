""" Class to transform digits into LCD format """

from lcd_modules.lcd_digit import digit

class LCDDisplay():
    """ Class to digit trasformation """

    @staticmethod
    def get_digits(values):
        digits = []
        if len(values) > 0:
            for value in values:
                digits.append(digit(value))
        return digits

    @staticmethod
    def prepare_to_print():
        raise NotImplementedError()
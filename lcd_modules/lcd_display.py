""" Class to transform digits into LCD format """

from lcd_modules.lcd_digit import Digit, MIN_RESOLUTION

class LCDDisplay():
    """ Class to digit trasformation """

    case_resolution = MIN_RESOLUTION
    
    def __init__(self, res = MIN_RESOLUTION):
        self.case_resolution = res

    def get_digits(self, values):
        digits = []
        if len(values) > 0:
            for value in values:
                digits.append(Digit(value, self.case_resolution))
        return digits

    def prepare_to_print(self):
        raise NotImplementedError()
""" Class to transform digits into LCD format """

from lcd_modules.lcd_digit import Digit, MIN_RESOLUTION

class LCDDisplay():
    """ Class to digit trasformation """

    frame_resolution = None
    
    def __init__(self, res = MIN_RESOLUTION):
        self.frame_resolution = res

    def get_digits(self, values):
        """ Transform the given string values into array of Digit objects  with lcd format """
        digits = []
        if len(values) > 0:
            for value in values:
                digits.append(Digit(value, self.frame_resolution))
        return digits

    def prepare_to_display(self, digits):
        """ Transform the Digit array into a readable string to print on display """
        line = ""
        size = len(digits)
                line += item.d[idx]
                # Check if is the last element
                if i == size-1:
                    line += '\n'
                else:
                    line += ' '

        return line
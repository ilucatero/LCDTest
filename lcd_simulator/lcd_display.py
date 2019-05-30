""" Class to transform digits into LCD format """

from lcd_simulator.lcd_digit import Digit, MIN_RESOLUTION, EMPTY_SPACE

class LCDDisplay():
    """ Class to digit trasformation """

    frame_resolution = None
    empty_space = None

    def __init__(self, res=MIN_RESOLUTION, empty_space=EMPTY_SPACE):
        self.frame_resolution = res
        self.empty_space = empty_space

    def get_digits(self, values):
        """ Transform the given string values into array of Digit objects  with lcd format """
        digits = []
        if values:
            for value in values:
                digits.append(Digit(value, self.frame_resolution, self.empty_space))
        return digits

    def prepare_to_display(self, digits):
        """ Transform the Digit array into a readable string to print on display """
        line = ""
        size = len(digits)
        for idx in range(self.frame_resolution):
            for i, item in enumerate(digits):
                line += item.digit_val[idx]
                #Check if is the last element
                if i == size-1:
                    line += '\n'
                else:
                    line += ' '
        return line

    def get_line_to_display(self, values):
        """ Performs values transformation and line preparation to display  """
        digits = self.get_digits(values)
        return self.prepare_to_display(digits)

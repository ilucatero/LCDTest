""" Class to contain digits in LCD format """

MIN_RESOLUTION = 3
EMPTY_SPACE = " "
VALID_DIGITS = {
    '0' : [
        ' _ ',
        '| |',
        '|_|'
        ],
    '1' : [
        '   ',
        '  |',
        '  |'
        ],
    '2' : [
        ' _ ',
        ' _|',
        '|_ '
        ],
    '3' : [
        ' _ ',
        ' _|',
        ' _|'
        ],
    '4' : [
        '   ',
        '|_|',
        '  |'
        ],
    '5' : [
        ' _ ',
        '|_ ',
        ' _|'
        ],
    '6' : [
        ' _ ',
        '|_ ',
        '|_|'
        ],
    '7' : [
        ' _ ',
        '  |',
        '  |'
        ],
    '8' : [
        ' _ ',
        '|_|',
        '|_|'
        ],
    '9' : [
        ' _ ',
        '|_|',
        '  |'
        ],

}

class Digit():  #pylint: disable=R0903
    """ Class to contain digits in LCD format """
    digit_val = []
    def __init__(self, digit, resolution=MIN_RESOLUTION, empty_space=" "): #pylint: disable=too-many-function-args
        self.digit_val = self._trasform(digit, empty_space)

        if resolution < MIN_RESOLUTION:
            raise RuntimeError(f'The resolution cannot be lower than : {MIN_RESOLUTION}')
        if resolution > MIN_RESOLUTION:
            self._update_digit_resolution(resolution)

    @staticmethod
    def _update_digit_resolution(resolution):
        # TODO update matrix resolution by adding _ if preceeded by one on X,
        # or | if preceeded by on on Y
        raise NotImplementedError()

    @staticmethod
    def _trasform(digit, new_empty_space):
        value = None
        try:
            value = VALID_DIGITS[digit]
        except: #pylint: disable=W0702
            value = VALID_DIGITS['0']

        if new_empty_space != EMPTY_SPACE:
            for i, item in enumerate(value):
                value[i] = item.replace(EMPTY_SPACE, new_empty_space)

        return value

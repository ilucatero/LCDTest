""" Class to contain digits in LCD format """

MIN_RESOLUTION = 3
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
            '| |',
            '|_|'
        ],
    '3' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '4' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '5' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '6' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '7' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '8' : [
            ' _ ',
            '| |',
            '|_|'
        ],
    '9' : [
            ' _ ',
            '| |',
            '|_|'
        ],

}

class digit():
    d = []
    def __init__(self, digit, resolution = MIN_RESOLUTION):
        self.d = self._trasform(digit)

        if resolution < MIN_RESOLUTION:
            raise RuntimeError(f'The resolution cannot be lower than : {MIN_RESOLUTION}')
        elif resolution > MIN_RESOLUTION:
            self._update_digit_resolution(resolution)

    def _update_digit_resolution(self, resolution):
        #TODO update matrix resolution by adding _ if preceeded by one on X, or | if preceeded by on on Y
        raise NotImplementedError()

    def _trasform(self, digit):
        try:
            return VALID_DIGITS[digit]
        except:
            return VALID_DIGITS['0']
        
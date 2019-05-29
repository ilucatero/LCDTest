""" Script to transform digits into LCD format """

#from collectors.metric_collector import MetricCollector        

VALID_DIGIT = {
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
    '9' : [
            ' _ ',
            '|_|',
            '  |'
        ]
}

class digit():
    d = []
    def __init__(self, digit):
        self.d = self._trasform(digit)

    def _trasform(self, digit):
        try:
            return VALID_DIGIT[digit]
        except:
            return VALID_DIGIT['0']
        


class LCDDisplay():
    """ Class to digit trasformation """

    @staticmethod
    def get_digits(values):
        digits = []
        if len(values) > 0:
            for value in values:
                digits.append(digit(value))
        return digits
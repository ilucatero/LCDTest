#!/usr/bin/env python

""" Main script that runs the Lcd Display simulator """

from lcd_simulator.lcd_display import LCDDisplay

def main():
    """ Runs the Lcd Display simulator asking the user the values to display """
    qit = False

    empty_frame = input('What the character to use as empty frame on display? \
                    \nValid options:\n  (space)\n  .\nYour choice:')
    if not empty_frame in [' ', '.']:
        print("The given value is not valid!\nExiting...")
        qit = True

    while not qit:
        value = input("What number you want to display? [q - to quit] ")
        if value != 'q':
            # check input contains only numbers (including left zeros)
            try:
                int(value)
            except ValueError:
                print("That's not an int!")

            dispay = LCDDisplay(empty_space=empty_frame)
            line = dispay.get_line_to_display(value)
            print(line)
        else:
            qit = True
            print("by-bye!")

if __name__ == "__main__":
    main()

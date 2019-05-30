#!/usr/bin/env python

from lcd_simulator.lcd_display import LCDDisplay

def main():
    quit = False
    while not quit:
        value = input("What number you want to display? [q - to quit] ")
        if value != 'q':
            # check input contains only numbers (including left zeros)
            try:
                int(value)
            except ValueError:
                print("That's not an int!")

            dispay = LCDDisplay()
            line = dispay.get_line_to_display(value)
            print(line)
        else:
            quit = True
            print("by-bye!")

if __name__ == "__main__":
    main()
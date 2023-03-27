"""
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.
"""


import itertools
def get_pins(observed):
    adjacent = {
        '1': ['2', '1', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2','3', '6'],
        '4': ['1','5', '4','7'],
        '5' : ['2', '4','5', '6', '8'],
        '6' : ['3', '5','6','9'],
        '7' : ['4','7','8'],
        '8' : ['5', '7','8','9', '0'],
        '9' : ['6' ,'9','8'],
        '0' : ['8','0']
    }
    # gets all the adjacent digits of every number in observed
    adj_num = [adjacent[digit] for digit in observed]
    
    # itertools.product multiplies each string value to another, creating a combination of numbers
    combination = list(itertools.product(*adj_num)) # insert all values in adj_num and create a combination
    
    return [''.join(pins) for pins in combination]
    

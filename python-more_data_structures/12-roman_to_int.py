#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    res = 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in range(0, len(roman_string)):
        if x > 0 and roman[roman_string[x]] > roman[roman_string[x - 1]]:
            res += roman[roman_string[x]] - 2 * roman[roman_string[x - 1]]
        else:
            res += roman[roman_string[x]]
    return res

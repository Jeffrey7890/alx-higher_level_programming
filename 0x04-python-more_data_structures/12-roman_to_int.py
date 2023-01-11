#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    ROMAN_NUMERAL_STD = {
        'M': 1000,
        'C': 100,
        'X': 10,
        'I': 1,
        'D': 500,
        'L': 50,
        'V': 5
    }

    SUM = 0
    length = len(roman_string)
    for i in range(length):
        rchr = roman_string[i]
        value = ROMAN_NUMERAL_STD[rchr]
        if rchr == 'I' and i < length - 1:
            nchr = roman_string[i + 1]
            if nchr == 'V' or nchr == 'X':
                SUM = SUM - value
            elif rchr == nchr:
                SUM = SUM + value
            i += 1
            value = ROMAN_NUMERAL_STD[roman_string[i]]
        else:
            SUM = SUM + value
    return (SUM)

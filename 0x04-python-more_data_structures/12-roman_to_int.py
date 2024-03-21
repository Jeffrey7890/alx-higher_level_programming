#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    ROMAN = {
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
    if length > 2:
        if roman_string[0] not in ROMAN or roman_string[1] not in ROMAN:
            return (0)
        if ROMAN[roman_string[0]] < ROMAN[roman_string[1]]:
            return (0)

    for i in range(length):
        rchr = roman_string[i]
        if rchr not in ROMAN:
            return (0)
        value = ROMAN[rchr]
        if rchr == 'I' and i < length - 1:
            nchr = roman_string[i + 1]
            if nchr == 'V' or nchr == 'X':
                SUM = SUM - value
            elif rchr == nchr:
                SUM = SUM + value
            i += 1
            value = ROMAN[roman_string[i]]
        else:
            SUM = SUM + value
    return (SUM)

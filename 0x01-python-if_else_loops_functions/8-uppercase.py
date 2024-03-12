#!/usr/bin/python3
def isalpha(c):
    return((97 <= c) and (c <= 122))


def uppercase(str):
    str += '\n'
    for c in str:
        if isalpha(ord(c)):
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print(c, end='')

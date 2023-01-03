#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    length = len(str)
    if (n > length or n < 0):
        return(str)
    for i in range(len(str)):
        if (str[i] != str[n]):
            cpy += str[i]
    return (cpy)

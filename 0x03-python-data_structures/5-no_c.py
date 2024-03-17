#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        c_strs = "cC"
        result = ""
        for ch in my_string:
            if ch not in c_strs:
                result = result + ch
        return (result)

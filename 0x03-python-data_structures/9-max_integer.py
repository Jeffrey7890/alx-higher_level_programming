#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        length = len(my_list)
        if length > 0:
            high = my_list[0]
            for i in my_list:
                if high < i:
                    high = i
            return (high)
    return (None)

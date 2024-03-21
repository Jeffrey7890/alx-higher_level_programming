#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return (None)

    s_my_list = set(my_list)
    ssum = 0

    for i in s_my_list:
        ssum += i
    return (ssum)

#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list)
    if length > 0:
        for i in range(length):
            print("{}".format(my_list[i]))

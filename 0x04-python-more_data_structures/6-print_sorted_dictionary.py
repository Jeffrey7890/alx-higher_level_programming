#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is None):
        return (None)

    sorted_dictionary = sorted(a_dictionary)

    for i in sorted_dictionary:
        print("{}: {}".format(i, a_dictionary[i]))

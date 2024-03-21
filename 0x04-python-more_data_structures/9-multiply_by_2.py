#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = {}
        for key in a_dictionary.keys():
            new_dict[key] = a_dictionary[key] * 2
        return (new_dict)

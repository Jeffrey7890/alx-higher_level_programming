#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        if idx < 0 or idx > len(my_list) - 1:
            return (my_list)
        my_list_cpy = my_list.copy()
        my_list_cpy[idx] = element
        return (my_list_cpy)

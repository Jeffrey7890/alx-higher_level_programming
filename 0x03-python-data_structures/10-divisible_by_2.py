#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        even = []
        for i in my_list:
            if i % 2 == 0:
                even.append(True)
            else:
                even.append(False)
        return (even)
    return (None)

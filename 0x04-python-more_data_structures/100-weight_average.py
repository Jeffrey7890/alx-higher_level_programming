#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return (None)

    weighted_av = 0
    ssum = 0
    for tup_i in my_list:
        weighted_av = weighted_av + (tup_i[0] * tup_i[1])
        ssum = ssum + tup_i[1]

    weighted = weighted_av / ssum
    return (weighted)

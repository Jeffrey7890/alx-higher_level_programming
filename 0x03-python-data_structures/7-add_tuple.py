#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None:
        return (tuple_b)
    if tuple_b is None:
        return (tuple_a)
    if tuple_a is not None and tuple_b is not None:
        length = len(tuple_a), len(tuple_b)

        if length == (0, 0):
            return (0, 0)
        if length == (1, 0):
            return (tuple_a[0], 0)
        if length == (0, 1):
            return (0, tuple_b[0])
        if length == (0, 2):
            return (tuple_b)
        if length == (2, 0):
            return (tuple_a)
        if length == (1, 1):
            return (tuple_a[0], tuple_b[0])
        if length == (1, 2):
            return (tuple_a[0] + tuple_b[0], tuple_b[1])
        if length == (2, 1):
            return (tuple_a[0] + tuple_b[0], tuple_a[1])
        if length == (2, 2):
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

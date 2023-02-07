#!/usr/bin/python3
"""compares instances of class"""


def is_same_class(obj, a_class):
    """checks if obj is an instance
        of a_class
    """
    return (type(obj) is a_class)

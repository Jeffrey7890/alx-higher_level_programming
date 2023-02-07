#!/usr/bin/python3
"""Returns a lists of availalbe atrributes
    and methods of an object"""


def lookup(obj):
    """Returns a list of attributes in obj"""
    return (dir(obj))

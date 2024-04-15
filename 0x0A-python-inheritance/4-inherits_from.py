#!/usr/bin/python3
"""Module issubclasss"""


def inherits_from(obj, a_class):
    """uses issubclass men"""
    return (issubclass(type(obj), a_class))

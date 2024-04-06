#!/usr/bin/python3
"""
    Module of function ````say_my_name()```

    the ```say_my_name()``` function prints out the first
    and last name of a person, it raises TypeError if any
    of both arguments are not strings'

"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Attribute
    =========
        first_name:
            a string of persons first name

        last_name:
            string of persons last name

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

#!/usr/bin/python3
"""module to add two integer together

    ```add_integer``` take two argument of type
    float or integer, and raise error if is other wise

    This performs integer addition on int or float
    arguments.

"""


def add_integer(a, b=98):
    """add_integer

    sums two integeters or floats together
    raises TypeError if a or b are not integer or floats

    Returns: their sum

    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

#!/usr/bin/python3
"""Empty class men"""


class BaseGeometry:
    """Repreents an emtpy class
        for alx"""

    def area(self):
        """Raise error for alx"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

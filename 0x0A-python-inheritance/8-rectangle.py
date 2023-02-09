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
            raise TypeError("{} must be an intger".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

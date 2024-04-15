#!/usr/bin/python3
"""Square subclass of Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle
        grandchild of BaseRectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """area of a square"""
        return (self.__size ** 2)

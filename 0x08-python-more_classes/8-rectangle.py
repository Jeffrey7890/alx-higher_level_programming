#!/usr/bin/python3
"""Module to represent a Rectangle
    This module shows an example
    of how to use setters, getters
    with @property wrapper function
"""


class Rectangle:
    """Rectangle class

        This clcass reprsents a rectangle shape

        Attribute
        =========
        width: must be an integer and must be greater
                than zero

        height: must be an int and >= 0, else rasies
        value error, or typeerror

        area:
            returns the area of the rectangle

        perimeter:
            returns the e perimeter of the rectangle
            if width or height is 0 it returns zero

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @property
    def height(self):
        return (self.__height)

    @property
    def width(self):
        return (self.__width)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if isinstance(rect1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect2, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect1.area() > rect2.area():
            return (rect1)
        elif rect1.area() < rect2.area():
            return (rect2)
        elif rect1.area() == rect2.area():
            return (rect1)

    def __str__(self):
        string = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

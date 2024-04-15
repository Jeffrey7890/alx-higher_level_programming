#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry
        with private attributes
        width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Gets the area of rectangle
            width * height
        """
        return (self.__width * self.__height)

    def __str__(self):
        """string representation
            of Rectangle width/height
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

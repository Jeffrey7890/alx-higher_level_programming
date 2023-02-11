#!/usr/bin/python3
"""Module Rectangle"""


if __name__ == "__main__":
    from base import Base

else:
    from models.base import Base


class Rectangle(Base):
    """Rectangle class inherites from
        Base class

        Attributes
        ==========

        width: private attribute, decimal

        height: prviate attribute, decimal

        x: point, in x coordinate
        y: point, in y coordinate

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self._validate_wh(width, "width")
        self.__width = width

        self._validate_wh(height, "height")
        self.__height = height

        self._validate_xy(x, "x")
        self.__x = x

        self._validate_xy(y, "y")
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self._validate_wh(value, "width")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self._validate_wh(value, "height")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self._validate_xy(value, "x")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self._validate_xy(value, "y")
        self.__y = value

    def _validate_wh(self, value, name):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def _validate_xy(self, value, name):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return (self.__width * self.__height)

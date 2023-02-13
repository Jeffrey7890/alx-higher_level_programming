#!/usr/bin/python3
"""Module Rectangle"""


from .base import Base


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
        """initialation of class

            Attribtues:
            ==========
            width:
                width of the rectangle, must be integer
                and must be > 0,
            height:
                height of the rectangle must be integer
                and must be > 0, else raise
                ValueError
            x:
                x position of the x coordinate
                must be >= 0
            y:
                y position of the y coordinate
                must be >= 0

            _validate_xy:
                function to validate the values of
                the x and y class variables

            _validate_wh:
                function to validate the values of the
                width and height class varibles

            update:
                function to update each class variable,
                accept any number of args and **kwargs
        """

        super().__init__(id)

        self._validate_wh(width, "width")
        self.width = width

        self._validate_wh(height, "height")
        self.height = height

        self._validate_xy(x, "x")
        self.x = x

        self._validate_xy(y, "y")
        self.y = y

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
        """validate the width and height values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def _validate_xy(self, value, name):
        """validate the x and y values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def __str__(self):
        """string representations"""
        string = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
        string += str(self.y) + " - " + str(self.width)
        string += "/" + str(self.height)

        return (string)

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints out the shape with '#'"""
        print("\n" * self.y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update the class variables"""
        if len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']

            for i in range(len(args)):
                self.__setattr__(attributes[i], args[i])
        else:
            for key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """returns the class variables in a dictionary"""
        result = {}
        result["width"] = self.width
        result["height"] = self.height
        result["id"] = self.id
        result["x"] = self.x
        result["y"] = self.y
        return (result)

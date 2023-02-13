#!/usr/bin/python3


"""Model square class"""


from .rectangle import Rectangle


class Square(Rectangle):
    """square subclass of Rectangle
        superclasss
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialization function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (string)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self._validate_wh(value, "width")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update for square class"""
        if len(args) > 0:
            attributes = ['id', 'width', 'x', 'y']
            for i in range(len(args)):
                self.__setattr__(attributes[i], args[i])

        else:
            for key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """function to convert square class
            attribute to dictionary
        """
        result = {}
        result['size'] = self.width
        result['id'] = self.id
        result['x'] = self.x
        result['y'] = self.y
        return (result)

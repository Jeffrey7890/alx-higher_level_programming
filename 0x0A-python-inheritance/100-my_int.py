#!/usr/bin/python3
"""Square subclass of int"""



class MyInt(int):
    """MyInt subclass of int class"""
    
    def __init__(self, x):
        int.__init__(x)
        self.__x = x

    def __eq__(self, x):
        if (x == self.__x):
            return(False)
        return (True)

    def __ne__(self, x):
        if (x != self.__x):
            return (False)
        return (True)


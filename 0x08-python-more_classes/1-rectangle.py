#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ class rectangle """

    def __init__(self, width=0, height=0):
        """ init method """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ returns width """
        return self.__width

    @property
    def height(self):
        """ returns height """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

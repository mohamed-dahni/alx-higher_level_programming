#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ class rectangle """

    def __init__(self, width=0, height=0):
        """ init method """
        self._width = width
        self._height = height

    @property
    def width(self):
        """ returns width """
        return self._width

    @width.setter
    def width(self, value):
        """ sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ returns height """
        return self._height

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ class rectangle """
    
    def __init__(self, width=0, height=0):
        """ init method """
        self._width = width
        self._height = height

    def width(self):
        """ returns width """
        return self._width

    def width(self, width):
        """ sets width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    def height(self):
        """ returns height """
        return self._height

    def height(self, height):
        """ sets height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

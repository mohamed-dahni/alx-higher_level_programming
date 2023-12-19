#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        Prints the square with the # character by iterating over
        the size of the square.
        """
        if self.__size == 0:
            return
        for i in range(self.__size):
            print("#" * self.__size)


    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

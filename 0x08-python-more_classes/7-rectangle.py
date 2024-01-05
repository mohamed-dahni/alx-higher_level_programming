#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """ class rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init method """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """ returns area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """ returns string representation of Rectangle """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ returns string representation of Rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message when the object is destroyed """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

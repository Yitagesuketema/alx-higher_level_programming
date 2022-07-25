#!/usr/bin/python3
# 2-rectangle.py
# Yitagesu K Areda
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.
        Args:
            windth (int) : The width of the Rectangle.
            height(int)  :The height of a Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def width(self):
        """Get/Set the height of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """ Return the area of a Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return the perimeter of a Rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

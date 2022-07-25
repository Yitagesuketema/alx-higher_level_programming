#!/usr/bin/python3
# 0-rectangle.py
# Yitagesu K Areda
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """ Instantiation of a class"""
    def width(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError
            print("width must be an integer")
        elif value <= 0:
            raise ValueError
            print("width must be >=0")
        else:
            self.width = value

    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError
            print("height must be an integer")
        elif value <= 0:
            raise ValueError
            print("height must be >=0")
        else:
            self.height = value

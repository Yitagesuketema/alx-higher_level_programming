#!/usr/bin/python3
""" Define a class base """


class base:
    __nb_objects = 0
    """define constructor function"""

    def __init__(self, id=None):
        if (id is not None):
            id = self.__nb_objects
        else:
            self.__nb_objects += 1

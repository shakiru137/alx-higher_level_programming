#!/usr/bin/python3
""" This is the base module """


class Base:
    """ Private class attribute """
    __nb_objects = 0
    """ The class constructor """
    def __init__(self, id=None):
        if id is not None:
            """ Public instance attribute """
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

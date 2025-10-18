#!/usr/bin/python3
"""
Module to check if an object inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class is not a_class

#!/usr/bin/python3
"""
Module to check if an object is an instance of a class
or inherits from it.
"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of or inherits from a_class."""
    return isinstance(obj, a_class)

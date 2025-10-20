#!/usr/bin/python3
"""
Module that provides a function to safely add attributes to objects.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr_name (str): The name of the attribute.
        attr_value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")

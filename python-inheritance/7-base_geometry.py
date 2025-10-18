#!/usr/bin/python3
"""
Module that defines a base class for geometry objects.
"""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


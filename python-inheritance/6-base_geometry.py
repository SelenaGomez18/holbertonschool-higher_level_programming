#!/usr/bin/python3
"""
Module that defines a base class for geometry objects.
"""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

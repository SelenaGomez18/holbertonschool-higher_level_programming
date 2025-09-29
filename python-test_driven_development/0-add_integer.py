#!/usr/bin/python3
"""
This module defines the function add_integer
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number (int or float)
        b: second number (int or float, default = 98)
    Returns:
        The integer addition of a and b
    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b

#!/usr/bin/python3
"""Defines a rebel integer class."""


class MyInt(int):
    """MyInt has == and != inverted."""

    def __eq__(self, other):
        """Return True if values are not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True if values are equal."""
        return super().__eq__(other)

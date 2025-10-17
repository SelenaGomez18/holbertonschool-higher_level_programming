#!/usr/bin/python3
"""
Module defines a MyList class that extends list.
"""


class MyList(list):
    """Class that prints a sorted version of the list."""
    def print_sorted(self):
        print(sorted(self))

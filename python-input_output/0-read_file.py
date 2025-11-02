#!/usr/bin/python3
"""Module for reading and printing a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")

#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        append = f.write(text)
        return append

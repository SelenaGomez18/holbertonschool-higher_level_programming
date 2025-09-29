#!/usr/bin/python3
"""
This module defines a function that prints a text
with two new lines after each '.', '?' or ':' character.
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' or ':' character.

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".:?":
            print(text[:i + 1].strip())
            print()
            text = text[i + 1:]
            i = 0
        else:
            i += 1

    if text.strip():
        print(text.strip())

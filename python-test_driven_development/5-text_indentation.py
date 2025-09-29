#!/usr/bin/python3
"""
This module contains the function text_indentation
that prints a text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        ch = text[i]
        print(ch, end="")
        if ch in ".?:":
            print("\n")
            # saltar espacios después del símbolo
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

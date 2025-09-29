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

    text = text.strip()
    i = 0
    length = len(text)
    while i < length:
        start = i
        # Move forward until we find a punctuation
        while i < length and text[i] not in ".?:":
            i += 1
        # If we found a punctuation, include all consecutive punctuations
        if i < length and text[i] in ".?:":
            # include this punctuation
            i += 1
            # Include consecutive punctuation marks as well
            while i < length and text[i] in ".?:":
                i += 1
            # print the slice from start to i, stripped
            print(text[start:i].strip())
            print()
        else:
            # No punctuation found until end, print rest
            print(text[start:].strip())
            break
        # Skip any spaces after punctuation
        while i < length and text[i] == ' ':
            i += 1

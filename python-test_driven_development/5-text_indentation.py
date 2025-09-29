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
    n = len(text)
    buffer = ""
    delimiters = {'.', '?', ':'}

    while i < n:
        char = text[i]
        buffer += char

        if char in delimiters:
            # Look ahead to group trailing delimiters (like '?!:' or '...') with current
            j = i + 1
            while j < n and text[j] in delimiters:
                buffer += text[j]
                j += 1
            i = j - 1  # update i to last delimiter in group

            print(buffer.strip())
            print()  # two new lines (one from print, one extra)
            buffer = ""

            # skip all spaces after delimiter group
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue

        i += 1

    # Print remaining text without extra newline at end
    if buffer.strip():
        print(buffer.strip(), end='')

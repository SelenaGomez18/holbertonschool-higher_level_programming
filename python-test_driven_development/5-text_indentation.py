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
    start = 0

    for i, char in enumerate(text):
        if char in ".:?":
            print(text[start:i+1].strip())
            print()  # salto extra para dos líneas en total
            start = i + 1

    # Imprime el resto, sin línea vacía extra al final
    rest = text[start:].strip()
    if rest:
        print(rest, end='')

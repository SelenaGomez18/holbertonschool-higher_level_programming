#!/usr/bin/python3
"""
Print text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    buffer = ""

    for ch in text:
        buffer += ch
        if ch in delimiters:
            print(buffer.strip())  # imprimimos la parte
            print()                # salto doble
            buffer = ""

    # Si quedó algo pendiente, lo imprimimos SIN salto final
    if buffer.strip():
        print(buffer.strip(), end="")

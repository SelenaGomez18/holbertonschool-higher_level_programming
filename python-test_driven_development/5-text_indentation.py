#!/usr/bin/python3
"""
Print text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    buffer = ""

    for ch in text:
        buffer += ch
        if ch in delimiters:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip(), end="")

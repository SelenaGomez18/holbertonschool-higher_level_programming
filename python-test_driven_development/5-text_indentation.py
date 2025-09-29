#!/usr/bin/python3
"""
5-text_indentation module
Print text with 2 new lines after ., ? and : characters.
This module provides the text_indentation function.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)
    buf = ''

    while i < n:
        ch = text[i]
        # If we hit a delimiting character, append it, print buffer trimmed,
        # print an extra blank line, reset buffer and skip following spaces.
        if ch in '.?:':
            buf += ch
            print(buf.strip())
            print()
            buf = ''
            i += 1
            # skip all spaces after the punctuation to avoid leading spaces
            while i < n and text[i] == ' ':
                i += 1
            continue

        # Skip leading spaces for a new line (avoid spaces at start)
        if ch == ' ' and buf == '':
            i += 1
            continue

        buf += ch
        i += 1

    # Print any remaining text (no extra blank line afterwards)
    if buf:
        print(buf.strip(), end='')

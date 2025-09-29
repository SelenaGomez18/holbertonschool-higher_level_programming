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
    buf = []

    while i < n:
        ch = text[i]

        # if delimiter found, flush buffer + print blank line then skip spaces
        if ch in ".?:":
            buf.append(ch)
            line = ''.join(buf).strip()
            print(line)   # print sentence (adds newline)
            print()       # extra blank line
            buf = []
            i += 1
            # skip all spaces after punctuation to avoid leading spaces on next line
            while i < n and text[i] == ' ':
                i += 1
            continue

        # avoid leading spaces in a new buffer
        if ch == ' ' and not buf:
            i += 1
            continue

        buf.append(ch)
        i += 1

    # print any remaining text (no extra blank line after last fragment)
    if buf:
        print(''.join(buf).strip())

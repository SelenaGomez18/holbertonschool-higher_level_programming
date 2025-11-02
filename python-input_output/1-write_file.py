#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
        return num

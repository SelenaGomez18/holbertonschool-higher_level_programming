#!/usr/bin/python3
def uppercase(str):

    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = ord(c) - 32
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(c), end="")
    print()

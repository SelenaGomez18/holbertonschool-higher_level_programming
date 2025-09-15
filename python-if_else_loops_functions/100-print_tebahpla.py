#!/usr/bin/python3
for i in range(122, 96, -1):  # Rango de z (122) a A (65)
    if (122 - i) % 2 == 0:  # Alterna entre minúsculas y mayúsculas
        print(chr(i), end="")
    else:
        print(chr(i - 32), end="")

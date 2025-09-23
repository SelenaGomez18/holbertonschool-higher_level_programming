#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_val = dict([
        ('I', 1), ('V', 5), ('X', 10), ('L', 50),
        ('C', 100), ('D', 500), ('M', 1000)
    ])
    count = 0
    for x in range(len(roman_string)):
        current = roman_val[roman_string[x]]
        if x + 1 < len(roman_string):
            next_val = roman_val[roman_string[x + 1]]
        else:
            next_val = 0
        if current < next_val:
            count -= current
        else:
            count += current
    return count

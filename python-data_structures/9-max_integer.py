#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    big_value = my_list[0]
    for current in my_list:
        big_value = current if current > big_value else big_value
    return big_value

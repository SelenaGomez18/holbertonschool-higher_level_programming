#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")


#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom Python object using pickle.
"""

import pickle


class CustomObject:
    """A simple class representing a custom object with basic attributes."""

    def __init__(self, name, age, is_student):
        """Initialize object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Args:
            filename (str): Name of the file to save the object.
        Returns:
            None
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            # If any error occurs during serialization, print and return None
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.
        Args:
            filename (str): Name of the file to load the object from.
        Returns:
            CustomObject instance or None if file not found or corrupted.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError):
            return None
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None

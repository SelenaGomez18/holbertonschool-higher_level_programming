#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        root = ET.Element("data")

        # Add each key-value pair as a sub-element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception as e:
        print(f"Error during XML serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized dictionary, or None if failed.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except ET.ParseError:
        print("Error parsing the XML file.")
        return None
    except Exception as e:
        print(f"Unexpected error during XML deserialization: {e}")
        return None

#!/usr/bin/env python3
"""Basic serialization utilities for Holberton task 00."""

import json
from typing import Any, Dict


def serialize_and_save_to_file(data: Dict[str, Any], filename: str) -> None:
    """
    Serialize a Python dictionary to JSON and save it to filename.
    Overwrites the file if it exists.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_and_deserialize(filename: str) -> Dict[str, Any]:
    """
    Load JSON from filename and return the deserialized Python dictionary.
    Raises FileNotFoundError if file doesn't exist, JSONDecodeError on invalid JSON,
    and TypeError if the JSON root is not a dict.
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("JSON content is not a dictionary")

    return data

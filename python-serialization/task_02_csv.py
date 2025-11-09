#!/usr/bin/env python3
"""
Module that converts CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file into JSON format and saves it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # CSV file does not exist
        return False
    except Exception as e:
        # Any other unexpected error
        print(f"Error converting CSV to JSON: {e}")
        return False

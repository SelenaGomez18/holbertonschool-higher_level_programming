#!/usr/bin/python3
"""Reads from standard input and computes metrics.

This script reads lines from stdin in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

It computes:
  - Total file size
  - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)

It prints the metrics every 10 lines and after a keyboard interruption (CTRL + C).
"""

import sys

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_size = 0
count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        count += 1
        parts = line.split()

        # Procesar tamaño del archivo
        try:
            total_size += int(parts[-1])
        except (ValueError, IndexError):
            pass

        # Procesar código de estado
        try:
            status = int(parts[-2])
            if status in status_codes:
                status_codes[status] += 1
        except (ValueError, IndexError):
            pass

        if count % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

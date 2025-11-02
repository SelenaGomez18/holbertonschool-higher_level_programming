#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
total file size and count of status codes.
Prints stats every 10 lines and at keyboard interruption.
"""
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise

    print_stats()

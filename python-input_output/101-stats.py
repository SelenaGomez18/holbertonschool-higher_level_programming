#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
Prints stats every 10 lines and at keyboard interruption.
"""

import sys

# Diccionario con los códigos de estado esperados
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
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 2:
            continue

        # Validar y obtener tamaño y código de estado
        try:
            size = int(parts[-1])
            status = int(parts[-2])
        except (ValueError, IndexError):
            continue

        # Sumar tamaño total
        total_size += size

        # Contar códigos válidos
        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        # Imprimir cada 10 líneas
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Imprimir al finalizar la entrada
print_stats()

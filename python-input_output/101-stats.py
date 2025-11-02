#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

# Diccionario para contar códigos de estado
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

total_size = 0  # Tamaño total de archivo
count = 0       # Contador de líneas procesadas

def print_stats():
    """Imprime las estadísticas acumuladas."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()

        # Validar que tenga al menos 2 elementos al final (status y size)
        if len(parts) >= 2:
            try:
                # El tamaño de archivo está al final
                total_size += int(parts[-1])
            except (ValueError, IndexError):
                pass

            try:
                # El código de estado está en la penúltima posición
                status = int(parts[-2])
                if status in status_codes:
                    status_codes[status] += 1
            except (ValueError, IndexError):
                pass

        # Cada 10 líneas imprimimos las estadísticas
        if count % 10 == 0:
            print_stats()

    # Si se acaba la entrada sin interrupción, imprimir estadísticas finales
    print_stats()

except KeyboardInterrupt:
    # Si se presiona Ctrl+C, imprimir estadísticas antes de salir
    print_stats()
    raise


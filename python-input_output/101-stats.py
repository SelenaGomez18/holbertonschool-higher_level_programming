#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of each status code
"""
import sys

# Diccionario con los posibles códigos de estado y su contador
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

total_size = 0  # Suma total de tamaños de archivo
count = 0       # Número de líneas leídas

def print_stats():
    """Prints accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        parts = line.split()

        # Verificar que la línea tenga el formato correcto
        if len(parts) >= 7:
            # Últimos dos valores son código y tamaño
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            # Actualizar total del tamaño
            total_size += size

            # Si el código es válido, actualizar el contador
            if status in status_codes:
                status_codes[status] += 1

        count += 1

        # Cada 10 líneas imprime estadísticas
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Si el usuario presiona Ctrl+C, muestra estadísticas finales antes de salir
    print_stats()
    raise

# Imprimir estadísticas finales al terminar la lectura
print_stats()

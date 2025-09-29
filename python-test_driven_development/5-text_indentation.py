#!/usr/bin/python3
"""
Print text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # 1. Elimina cualquier espacio en blanco al inicio o al final del texto.
    text = text.strip()

    # 2. Reemplaza los delimitadores por el formato deseado: <delimitador> + 2 \n
    for delimiter in ".?:":
        # Reemplazamos <delimitador> + <cualquier número de espacios> con <delimitador>\n\n
        # Esto asegura que se manejen correctamente los espacios después del delimitador.

        # Primero, agregamos los dos saltos de línea.
        text = text.replace(delimiter, delimiter + "\n\n")

    # 3. Imprime el texto final, limpiando el exceso de espacios.
    lines = text.split('\n')

    # Imprime cada línea, asegurándote de que no haya espacios en blanco al inicio.
    for i, line in enumerate(lines):
        if line.strip() != "":
            # Usa 'print' para la línea de texto.
            print(line.strip(), end="")

        # Agrega el salto de línea que el 'split' eliminó, excepto al final.
        if i < len(lines) - 1:
            print()

# NOTA: En la implementación más simple de Holberton, se suele usar la iteración.
# Aquí está la solución basada en la iteración, que es más parecida a tu enfoque original
# y más directa, *eliminando el doble salto de línea*.
# ---
# V2: Solución de Bucle Limpia (más cerca de tu lógica):

def text_indentation_v2(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Elimina los espacios antes y después
    text = text.strip()
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        # Si encuentra un delimitador, añade los saltos de línea y se salta los espacios
        if text[i] in ".?:":
            print(result.strip())
            print() # Imprime el segundo \n (la línea en blanco)
            result = ""

            # Avanza el índice para saltarse los espacios después del delimitador.
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            # Detenemos la iteración forzando el continue de afuera
            continue

        i += 1

    # Imprime cualquier texto restante sin un delimitador
    if result.strip():
        print(result.strip(), end="")
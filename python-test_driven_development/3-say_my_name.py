#!/usr/bin/python3
"""
Módulo 3-say_my_name

Contiene la función say_my_name que imprime el nombre completo dado.
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime My name is <first_name> <last_name>.

    Args:
        first_name (str): Primer nombre.
        last_name (str): Apellido (opcional).

    Raises:
        TypeError: Si first_name o last_name no son cadenas de texto.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())

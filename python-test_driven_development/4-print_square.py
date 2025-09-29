def print_square(size):
    """
    Imprime un cuadrado hecho con el caracter '#'.

    Args:
        size (int): tamaño del lado del cuadrado.

    Raises:
        TypeError: si size no es un entero.
        ValueError: si size es menor que 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

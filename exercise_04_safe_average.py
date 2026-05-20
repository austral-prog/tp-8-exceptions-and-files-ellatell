def safe_average(filename):
    """
    Lee un archivo y retorna el promedio de los números válidos.
    """

    suma = 0
    cantidad = 0

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                try:
                    numero = float(linea)

                    suma += numero
                    cantidad += 1

                except ValueError:
                    pass

    if cantidad == 0:
        raise ValueError("no valid numbers")

    return suma / cantidad

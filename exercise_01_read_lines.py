def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas.
    """
    
    lineas = []

    with open(filename, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea != "":
                lineas.append(linea)

    return lineas

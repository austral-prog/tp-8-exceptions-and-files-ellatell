def csv_to_dict(filename):
    """
    Lee un archivo CSV y retorna una lista de diccionarios.
    """

    personas = []

    with open(filename, "r") as archivo:

        lineas = archivo.readlines()

    if len(lineas) <= 1:
        return []

    header = lineas[0].strip().split(",")

    for linea in lineas[1:]:

        linea = linea.strip()

        if linea != "":

            valores = linea.split(",")

            fila = {}

            for i in range(len(header)):

                clave = header[i]
                valor = valores[i].strip()

                if clave == "age":
                    valor = int(valor)

                fila[clave] = valor

            personas.append(fila)

    return personas

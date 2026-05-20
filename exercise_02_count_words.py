def count_words(filename):
    """
    Lee un archivo y retorna un diccionario palabra -> cantidad.
    """

    conteo = {}

    with open(filename, "r") as archivo:
        texto = archivo.read()

    palabras = texto.split()

    for palabra in palabras:
        palabra = palabra.lower()

        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo

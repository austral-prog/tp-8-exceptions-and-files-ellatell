def find_longest_word(filename):
    """
    Retorna la palabra más larga de un archivo.
    """

    with open(filename, "r") as archivo:

        texto = archivo.read()

    palabras = texto.split()

    if len(palabras) == 0:
        raise ValueError("file has no words")

    palabra_mas_larga = palabras[0]

    for palabra in palabras:

        if len(palabra) > len(palabra_mas_larga):

            palabra_mas_larga = palabra

    return palabra_mas_larga

def grades_stats(filename):
    """
    Lee un archivo y retorna estadísticas de notas por estudiante.
    """

    estadisticas = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                estudiante, notas = linea.split(":")

                notas = notas.split(",")

                lista_notas = []

                for nota in notas:
                    lista_notas.append(float(nota))

                promedio = sum(lista_notas) / len(lista_notas)

                maximo = max(lista_notas)

                minimo = min(lista_notas)

                estadisticas[estudiante] = (promedio, maximo, minimo)

    return estadisticas

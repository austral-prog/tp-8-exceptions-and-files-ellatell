def read_sales(filename):
    """
    Lee un archivo con ventas y agrupa los valores por producto.
    """

    ventas = {}

    with open(filename, "r") as archivo:
        contenido = archivo.read()

    registros = contenido.split(";")

    for registro in registros:

        if registro != "":

            producto, valor = registro.split(":")

            valor = float(valor)

            if producto in ventas:
                ventas[producto].append(valor)
            else:
                ventas[producto] = [valor]

    return ventas


def process_sales(data):
    """
    Imprime ventas totales y promedio por producto.
    """

    for producto in data:

        total = sum(data[producto])

        promedio = total / len(data[producto])

        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

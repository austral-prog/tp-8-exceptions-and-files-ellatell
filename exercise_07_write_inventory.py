def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo.
    """

    with open(filename, "w") as archivo:

        items_ordenados = sorted(inventory)

        for item in items_ordenados:

            cantidad = inventory[item]

            archivo.write(f"{item}:{cantidad}\n")

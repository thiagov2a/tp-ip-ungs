import random


def lectura():
    lista_productos = []

    with open("productos.txt", "r") as f:
        for linea in f:
            producto, precio_economico, precio_premium = linea.strip().split(",")
            lista_productos.append(
                [producto, int(precio_economico), int(precio_premium)]
            )

    return lista_productos


def buscar_producto(lista_productos):
    producto = random.choice(lista_productos)
    rand = random.randint(1, 2)
    tipo_precio = "(económico)" if rand == 1 else "(premium)"
    return [producto[0], tipo_precio, producto[rand]]


def obtener_producto(lista_productos, margen):
    producto_principal = buscar_producto(lista_productos)
    cont = 0

    while cont < 2:
        producto_candidato = buscar_producto(lista_productos)
        if producto_candidato != producto_principal:
            if (
                producto_principal[2] == producto_candidato[2]
                or abs(producto_principal[2] - producto_candidato[2]) <= margen
            ):
                cont += 1

    return producto_principal


def es_precio_valido(precio, lista_productos, margen):
    cont = 0

    for producto in lista_productos:
        if precio == producto[2] or abs(precio - producto[2]) <= margen:
            cont += 1

    return cont >= 3


def procesar(producto_principal, producto_candidato, margen):
    if (
        producto_principal[2] == producto_candidato[2]
        or abs(producto_principal[2] - producto_candidato[2]) <= margen
    ):
        return producto_principal[2]
    else:
        return 0


def obtener_productos_aleatorios(producto, lista_productos, margen):
    productos_seleccionados = []
    cont = 0

    while cont < 2:
        producto_candidato = buscar_producto(lista_productos)
        if producto_candidato != producto:
            if (
                producto_candidato[2] == producto[2]
                or abs(producto_candidato[2] - producto[2]) <= margen
            ):
                productos_seleccionados.append(producto_candidato)
                cont += 1

    cont = 0

    while cont < 3:
        producto_candidato = buscar_producto(lista_productos)
        if producto_candidato != producto:
            productos_seleccionados.append(producto_candidato)
            cont += 1

    random.shuffle(productos_seleccionados)
    productos_seleccionados.insert(0, producto)

    return productos_seleccionados

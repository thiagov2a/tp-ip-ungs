import random


def lectura():
    lista_productos = []

    with open("productos.txt", "r") as f:  # Abre el archivo de texto
        for linea in f:
            # Separa y guarda los datos por comas
            producto, precio_economico, precio_premium = linea.strip().split(",")

            # Agrega la línea a la lista
            lista_productos.append(
                [producto, int(precio_economico), int(precio_premium)]
            )

    return lista_productos


def buscarProducto(lista_productos):
    # Elige un producto aleatorio de la lista
    producto = random.choice(lista_productos)

    # Elige un valor aleatorio entre 1 y 2
    rand = random.randint(1, 2)

    # Agrega el tipo de precio dependiendo del valor aleatorio
    tipo_precio = "(económico)" if rand == 1 else "(premium)"

    # Devuelve el producto, el tipo de precio y el valor
    return [producto[0], tipo_precio, producto[rand]]


# Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    producto_principal = buscarProducto(lista_productos)
    cont = 0

    while cont < 2:
        producto_candidato = buscarProducto(lista_productos)
        if producto_candidato != producto_principal:
            if (
                producto_principal[2] == producto_candidato[2]
                or abs(producto_principal[2] - producto_candidato[2]) <= margen
            ):
                cont += 1

    return producto_principal


# Devuelve True si existe el precio recibido como parámetro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont = 0

    for producto in lista_productos:
        if precio == producto[2] or abs(precio - producto[2]) <= margen:
            cont += 1

    return cont >= 3


# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
# el producto
def procesar(producto_principal, producto_candidato, margen):
    if (
        producto_principal[2] == producto_candidato[2]
        or abs(producto_principal[2] - producto_candidato[2]) <= margen
    ):
        return producto_principal[2]
    else:
        return 0


# Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
# De manera aleatoria se deberá tomar el valor económico o el valor premium. Agregar al nombre '(económico)' o '(premium)'
# para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    # Inicializamos la lista de productos
    productos_seleccionados = []

    # Inicializamos el contador
    cont = 0
    # Elegimos 2 productos con el mismo precio o dentro del margen
    while cont < 2:
        # Elegimos un producto aleatorio
        producto_candidato = buscarProducto(lista_productos)
        # Si el producto elegido es distinto al producto principal, entonces lo agregamos a la lista
        if producto_candidato != producto:
            if (
                producto_candidato[2] == producto[2]
                or abs(producto_candidato[2] - producto[2]) <= margen
            ):
                productos_seleccionados.append(producto_candidato)
                cont += 1

    # Reiniciamos el contador
    cont = 0
    # Elegimos 3 productos aleatorios
    while cont < 3:
        # Elegimos un producto aleatorio
        producto_candidato = buscarProducto(lista_productos)
        # Si el producto elegido es distinto al producto principal, entonces lo agregamos a la lista
        if producto_candidato != producto:
            productos_seleccionados.append(producto_candidato)
            cont += 1

    # Mezclamos los productos
    random.shuffle(productos_seleccionados)

    # Agregamos el producto principal al índice 0
    productos_seleccionados.insert(0, producto)

    return productos_seleccionados

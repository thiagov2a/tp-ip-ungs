import random


# Lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    lista_productos = []

    # Abrir el archivo de texto
    with open("productos.txt", "r") as f:
        # Leer cada línea del archivo
        for linea in f:
            # Separar la línea en producto, precio_economico y precio_premium
            producto, precio_economico, precio_premium = linea.strip().split(",")
            # Agregar la lista de productos al final de la lista
            lista_productos.append(
                [producto, int(precio_economico), int(precio_premium)]
            )

    return lista_productos


# De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto,
# el segundo si es económico o premium y el tercero el precio.
def buscar_producto(lista_productos):
    # Elige un producto aleatorio de la lista
    producto = random.choice(lista_productos)

    # Elige un precio aleatorio
    rand = random.randint(1, 2)

    # Agrega el tipo de precio
    tipo_precio = "(económico)" if rand == 1 else "(premium)"

    return [producto[0], tipo_precio, producto[rand]]


# Elige el producto. Debe tener al menos dos productos con un valor similar.
def obtener_producto(lista_productos, margen):
    # Elige un producto aleatorio de la lista
    producto_principal = buscar_producto(lista_productos)
    cont = 0

    # Busca el producto candidato
    while cont < 2:
        # Elige un producto aleatorio de la lista
        producto_candidato = buscar_producto(lista_productos)

        # Si el producto candidato es distinto al producto principal
        if producto_candidato != producto_principal:
            # Si el precio del producto candidato es igual al precio del producto principal o está dentro del margen
            if (
                producto_principal[2] == producto_candidato[2]
                or abs(producto_principal[2] - producto_candidato[2]) <= margen
            ):
                cont += 1

    return producto_principal


# Devuelve True si existe el precio recibido como parámetro aparece al menos 3 veces. Debe considerar el Margen.
def es_precio_valido(precio, lista_productos, margen):
    cont = 0

    # Recorre la lista de productos
    for producto in lista_productos:
        # Si el precio es igual al precio del producto o está dentro del margen
        if precio == producto[2] or abs(precio - producto[2]) <= margen:
            cont += 1

    return cont >= 3


# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y agrega al carrito el producto. No agrega si eligió directamente el producto.
def procesar(producto_principal, producto_candidato, margen):
    # Si el precio del producto candidato es igual al precio del producto principal o está dentro del margen
    if (
        producto_principal[2] == producto_candidato[2]
        or abs(producto_principal[2] - producto_candidato[2]) <= margen
    ):
        # Agrega el producto al carrito
        return producto_principal
    else:
        # No agrega el producto al carrito
        return None


# Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
# De manera aleatoria se deberá tomar el valor económico o el valor premium. Agregar al nombre '(económico)' o '(premium)'
# para que sea mostrado en pantalla.
def obtener_productos_aleatorios(producto, lista_productos, margen):
    productos_seleccionados = []
    cont = 0

    # Busca 2 productos aleatorios que tengan el mismo precio o estén dentro del margen
    while cont < 2:
        # Elige un producto aleatorio de la lista
        producto_candidato = buscar_producto(lista_productos)
        # Si el producto candidato es distinto al producto principal y no está en la lista de productos candidatos
        if (
            producto_candidato != producto
            and productos_seleccionados.count(producto_candidato) == 0
        ):
            # Si el precio del producto candidato es igual al precio del producto principal o está dentro del margen
            if (
                producto_candidato[2] == producto[2]
                or abs(producto_candidato[2] - producto[2]) <= margen
            ):
                # Agrega el producto candidato a la lista de productos candidatos
                productos_seleccionados.append(producto_candidato)
                cont += 1

    # Reinicia el contador
    cont = 0
    # Busca 3 productos aleatorios
    while cont < 3:
        # Elige un producto aleatorio de la lista
        producto_candidato = buscar_producto(lista_productos)
        # Si el producto candidato es distinto al producto principal y no está en la lista de productos candidatos
        if (
            producto_candidato != producto
            and productos_seleccionados.count(producto_candidato) == 0
        ):
            # Agrega el producto candidato a la lista de productos candidatos
            productos_seleccionados.append(producto_candidato)
            cont += 1

    # Mezcla los productos candidatos
    random.shuffle(productos_seleccionados)
    # Agrega el producto principal al principio de la lista
    productos_seleccionados.insert(0, producto)

    return productos_seleccionados

from principal import *
from configuracion import *
import random
import math
from extras import *


# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    return [
        ["Arroz", 1001, 1037],
        ["Yerba mate", 4546, 4904],
        ["Televisor Smart", 2055, 2439],
        ["Aceite de cocina", 3674, 4783],
        ["Mouse", 1635, 3603],
        ["Monitor de computadora", 2782, 2870],
        ["Silla de oficina", 3174, 4391],
        ["Lavadora", 3720, 4197],
        ["Refrigerador", 3352, 4533],
        ["Smartphone", 2070, 2224],
        ["Laptop", 4650, 4854],
        ["Cafetera", 2358, 3646],
        ["Batidora", 183, 4401],
        ["Microondas", 4254, 4624],
    ]


# De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es económico
# o premium y el tercero el precio.
def buscar_producto(lista_productos):
    producto = ["Silla de oficina", "(premium)", 4391]
    return producto


# Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    producto = ["Silla de oficina", "(premium)", 4391]
    return producto


# Devuelve True si existe el precio recibido como parámetro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    return True


# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
# el producto
def procesar(producto_principal, producto_candidato, margen):
    return 0


# Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
# De manera aleatoria se deberá tomar el valor económico o el valor premium. Agregar al nombre '(económico)' o '(premium)'
# para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = [
        ["Monitor de computadora", "(premium)", 2870],
        ["Silla de oficina", "(económico)", 3174],
        ["Lavadora", "(premium)", 4197],
        ["Refrigerador", "(premium)", 4533],
        ["Laptop", "(económico)", 4650],
        ["Cafetera", "(económico)", 2358],
    ]
    return productos_seleccionados

#! /usr/bin/env python
import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesRESUELTAS import *
from extras import *


def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    carrito_compras = []  # premios acumulados por el jugador
    producto_candidato = ""

    # Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = obtener_producto(lista_productos, MARGEN)
    print(producto)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se deberá tomar el valor económico o el valor premium.
    # Agregar  '(económico)' o '(premium)' y el precio
    productos_en_pantalla = obtener_productos_aleatorios(
        producto, lista_productos, MARGEN
    )
    print(productos_en_pantalla)

    # dibuja la pantalla la primera vez
    dibujar(
        screen,
        productos_en_pantalla,
        producto,
        producto_candidato,
        carrito_compras,
        segundos,
    )

    while segundos > fps / 1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():
            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[
                        0 : len(producto_candidato) - 1
                    ]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el producto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla):
                        # procesamos el premio
                        premio = procesar(
                            producto, productos_en_pantalla[indice], MARGEN
                        )
                        # si hay un premio, lo agregamos al carrito de compras
                        if premio != None:
                            reproducir_efecto_de_sonido("success.wav")
                            carrito_compras.append(premio)
                            print(carrito_compras)
                        else:
                            reproducir_efecto_de_sonido("fail.wav")
                        producto_candidato = ""
                        # Elegir un producto
                        producto = obtener_producto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = obtener_productos_aleatorios(
                            producto, lista_productos, MARGEN
                        )
                    else:
                        producto_candidato = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(
            screen,
            productos_en_pantalla,
            producto,
            producto_candidato,
            carrito_compras,
            segundos,
        )

        pygame.display.flip()

    # Fin del juego
    if segundos <= 0:
        reproducir_efecto_de_sonido("win.ogg")
        dibujar_premios(screen, carrito_compras)

    while 1:
        # Esperar al usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
        pygame.display.flip()


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

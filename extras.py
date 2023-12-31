import random
import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if K_0 <= key and key <= K_9:
        return str(key - K_0)
    else:
        return ""


def reproducir_efecto_de_sonido(nombre_del_efecto):
    # Carga el sonido
    sonido = pygame.mixer.Sound("static/sounds/" + nombre_del_efecto)

    # Reproduce el sonido
    sonido.play()


def dibujar_fondo(screen):
    # Limpiar pantalla
    screen.fill(COLOR_FONDO)

    # Fondo
    imagen_fondo = pygame.image.load("static/img/background.jpg")

    # Posición de la esquina inferior derecha
    x = ANCHO - imagen_fondo.get_width()
    y = ALTO - imagen_fondo.get_height() - 70

    # Dibujar el fondo
    screen.blit(imagen_fondo, (x, y))


def dibujar_premios(screen, carrito_compras):
    dibujar_fondo(screen)

    defaultFont = pygame.font.Font(
        "static/fonts/PixelifySans-VariableFont_wght.ttf", 30
    )

    # Mensaje de fin de juego
    text = "Fin del juego"
    text_surface = defaultFont.render(text, True, COLOR_TEXTO)
    screen.blit(text_surface, (130, ALTO - (ALTO - 100)))

    # Mostrar los premios
    text = "Premios: " + str(len(carrito_compras)) + " productos"
    text_surface = defaultFont.render(text, True, COLOR_TEXTO)
    screen.blit(text_surface, (130, ALTO - (ALTO - 100) + 70))


def dibujar(
    screen,
    productos_en_pantalla,
    producto_principal,
    producto_candidato,
    carrito_compras,
    segundos,
):
    dibujar_fondo(screen)

    defaultFont = pygame.font.Font(
        "static/fonts/PixelifySans-VariableFont_wght.ttf", 24
    )
    defaultFontGrande = pygame.font.Font(
        "static/fonts/PixelifySans-VariableFont_wght.ttf", 30
    )

    # Linea del piso
    pygame.draw.line(screen, (255, 255, 255), (0, ALTO - 70), (ANCHO, ALTO - 70), 5)
    ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Productos: " + str(len(carrito_compras)), 1, COLOR_TEXTO)
    if segundos < 15:
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL
        )
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    # Dibujar los nombres de los productos uno debajo del otro
    x_pos = 130
    y_pos = ALTO - (ALTO - 100)

    pos = 0
    for producto in productos_en_pantalla:
        nombre_en_pantalla = str(pos) + " - " + producto[0] + " " + producto[1]
        if (
            producto[0] == producto_principal[0]
            and producto[1] == producto_principal[1]
        ):
            screen.blit(
                defaultFontGrande.render(nombre_en_pantalla, 1, COLOR_TIEMPO_FINAL),
                (x_pos, y_pos),
            )
        else:
            screen.blit(
                defaultFontGrande.render(nombre_en_pantalla, 1, COLOR_LETRAS),
                (x_pos, y_pos),
            )
        pos += 1
        y_pos += ESPACIO

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (600, 10))
    screen.blit(ren3, (10, 10))

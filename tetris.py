import pygame
import random

# Definimos los colores que utilizaremos en el juego
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definimos las medidas de cada bloque del tetris
ANCHO_BLOQUE = 30
ALTO_BLOQUE = 30

# Definimos la velocidad de caída de las piezas
VELOCIDAD_CAIDA = 10

# Definimos la clase de las piezas
class Pieza:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def mover(self, x, y):
        self.x += x
        self.y += y

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, [self.x, self.y, ANCHO_BLOQUE, ALTO_BLOQUE])

# Definimos la clase del juego
class Juego:
    def __init__(self):
        # Inicializamos Pygame
        pygame.init()

        # Definimos el tamaño de la pantalla
        self.pantalla = pygame.display.set_mode([10 * ANCHO_BLOQUE, 20 * ALTO_BLOQUE])

        # Definimos la fuente del texto que utilizaremos
        self.fuente = pygame.font.SysFont("Arial", 25)

        # Definimos las variables del juego
        self.tablero = [[0] * 10 for i in range(20)]
        self.pieza_actual = self.generar_pieza()
        self.siguiente_pieza = self.generar_pieza()
        self.puntuacion = 0
        self.juego_terminado = False

    def generar_pieza(self):
        piezas = [
            [Pieza(0, 0, ROJO), Pieza(ANCHO_BLOQUE, 0, ROJO), Pieza(ANCHO_BLOQUE * 2, 0, ROJO), Pieza(ANCHO_BLOQUE * 3, 0, ROJO)], # Pieza I
            [Pieza(ANCHO_BLOQUE, 0, VERDE), Pieza(0, ALTO_BLOQUE, VERDE), Pieza(ANCHO_BLOQUE, ALTO_BLOQUE, VERDE), Pieza(ANCHO_BLOQUE * 2, ALTO_BLOQUE, VERDE)], # Pieza S
            [Pieza(0, 0, AZUL), Pieza(ANCHO_BLOQUE, 0, AZUL), Pieza(ANCHO_BLOQUE, ALTO_BLOQUE, AZUL), Pieza(ANCHO_BLOQUE * 2, ALTO_BLOQUE, AZUL)], ]#

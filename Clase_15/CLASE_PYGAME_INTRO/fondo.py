import pygame

def crear_fondo(ancho,alto):
    imagen_background = pygame.image.load(r"Clase_15\CLASE_PYGAME_INTRO\03.jpg")
    imagen_background = pygame.transform.scale(imagen_background,(ancho,alto))
    dict_fondo = {}
    dict_fondo["surface"] = imagen_background
    return dict_fondo
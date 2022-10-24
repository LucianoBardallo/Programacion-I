import pygame

def crear_fondo(path,ancho,alto):
    imagen_background = pygame.image.load(path)
    imagen_background = pygame.transform.scale(imagen_background,(ancho,alto))
    dict_fondo = {}
    dict_fondo["surface"] = imagen_background
    return dict_fondo


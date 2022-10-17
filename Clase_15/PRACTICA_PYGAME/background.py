import pygame
import colores

def crear_fondo(ancho,alto):
    imagen_background = pygame.image.load(r"Clase_15\PRACTICA_PYGAME\Background.png")
    imagen_background = pygame.transform.scale(imagen_background,(ancho,alto))
    dict_fondo = {}
    dict_fondo["surface"] = imagen_background
    return dict_fondo

def crear_decoracion(x,y,ancho,alto):
    imagen_logo = pygame.image.load(r"Clase_15\PRACTICA_PYGAME\03.png")
    imagen_logo = pygame.transform.scale(imagen_logo,(ancho,alto))
    dict_logo = {}
    dict_logo["surface"] = imagen_logo
    dict_logo["rect"] = dict_logo["surface"].get_rect()
    dict_logo["rect"].x = x
    dict_logo["rect"].y = y
    return dict_logo
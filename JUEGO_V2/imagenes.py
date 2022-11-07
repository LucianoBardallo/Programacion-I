import pygame
from constantes import *

#IMAGEN
class Imagen:
    def __init__(self,path,ancho,alto,x,y):
        self.imagen_background = pygame.image.load(path)
        self.imagen_background = pygame.transform.scale(self.imagen_background,(ancho,alto))
        self.surface = self.imagen_background
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

# layer01 = Imagen(PATH_IMAGE + r"locations\forest\layer_01_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer02 = Imagen(PATH_IMAGE + r"locations\forest\layer_02_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer03 = Imagen(PATH_IMAGE + r"locations\forest\layer_03_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer04 = Imagen(PATH_IMAGE + r"locations\forest\layer_04_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer05 = Imagen(PATH_IMAGE + r"locations\forest\layer_05_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer06 = Imagen(PATH_IMAGE + r"locations\forest\layer_06_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer07 = Imagen(PATH_IMAGE + r"locations\forest\layer_07_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)

# def actualizar_pantalla(screen):
#     screen.blit(layer07.surface,layer07.rect)
#     screen.blit(layer06.surface,layer06.rect)
#     screen.blit(layer05.surface,layer05.rect)
#     screen.blit(layer04.surface,layer04.rect)
#     screen.blit(layer03.surface,layer03.rect)
#     screen.blit(layer02.surface,layer02.rect)
#     screen.blit(layer01.surface,layer01.rect)
import pygame
from configuraciones import *

#IMAGEN
class Imagen:
    def __init__(self,path,ancho,alto,x,y):
        self.imagen_fondo = pygame.image.load(path)
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ancho,alto))
        self.surface = self.imagen_fondo
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
    
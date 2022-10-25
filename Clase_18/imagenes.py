import pygame

#IMAGEN
class Imagen:
    def __init__(self,path,ancho,alto,x,y):
        self.imagen_background = pygame.image.load(path)
        self.imagen_background = pygame.transform.scale(self.imagen_background,(ancho,alto))
        self.surface = self.imagen_background
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
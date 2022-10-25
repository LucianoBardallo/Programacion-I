import pygame
from constantes import *

class Texto:
    def __init__(self,tamaño,texto,x,y):
        self.fuente = pygame.font.SysFont("Arial Narrow", tamaño)
        self.texto = self.fuente.render(texto,True,(0,0,0))
        self.rect = self.texto.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


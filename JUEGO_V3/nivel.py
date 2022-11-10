import pygame
from constantes import *

class Nivel:
    def __init__(self):
        self.scroll = 0

    def crear_paradax(self,path,cantidad):
        self.fondo_paradax = []
        for i in range(1,cantidad+1):
            self.imagen = pygame.image.load(path + "{0}.png".format(i)).convert_alpha()
            self.imagen = pygame.transform.scale(self.imagen,(ANCHO_VENTANA,ALTO_VENTANA))
            self.surface = self.imagen
            self.fondo_paradax.append(self.surface)
            
        self.fondo_width = self.fondo_paradax[0].get_width()

    def events(self,keys,speed):
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.scroll > 0):
            self.scroll -= speed

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and self.scroll < 4200):
            self.scroll += speed
        
    def draw_bg(self,screen,cantidad):
        for x in range(cantidad):
            for i in self.fondo_paradax:
                screen.blit(i,((x * self.fondo_width),0))
                #screen.blit(i,((x * self.fondo_width) - self.scroll * speed_scroll,0))
                #speed_scroll += 0.2

    
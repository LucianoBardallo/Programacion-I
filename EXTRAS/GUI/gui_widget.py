import pygame
from pygame.locals import *
from configuraciones import *

class Widget:
    def __init__(self,master_form,x,y,w,h,color_fondo,color_borde,imagen_fondo,texto,fuente,fuente_tamaño,fuente_color):
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_fondo = color_fondo
        self.color_borde = color_borde
        if imagen_fondo != None:
            self.imagen_fondo = pygame.image.load(imagen_fondo)
            self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(w, h)).convert_alpha()
        else:
            self.imagen_fondo = None
        self._texto = texto
        if(self._texto != None):
            pygame.font.init()
            self._fuente_sys = pygame.font.SysFont(fuente,fuente_tamaño)
            self._fuente_color = fuente_color

    def renderizar(self):
        
        self.superficie_esclava = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.superficie_esclava = self.superficie_esclava.get_rect()
        self.superficie_esclava.x = self.x
        self.superficie_esclava.y = self.y
        self.supuerficie_esclave_colision = pygame.Rect(self.superficie_esclava)
        self.supuerficie_esclave_colision.x += self.master_form.x
        self.supuerficie_esclave_colision.y += self.master_form.y

        if self.color_fondo:
            self.superficie_esclava.fill(self.color_fondo)
        
        if self.imagen_fondo:
            self.superficie_esclava.blit(self.imagen_fondo,(0,0))
        
        if(self._texto != None):
            image_text = self._fuente_sys.render(self._texto,True,self._fuente_color,self.color_fondo)
            self.superficie_esclava.blit(image_text,[
                self.superficie_esclava.width/2 - image_text.get_rect().width/2,
                self.superficie_esclava.height/2 - image_text.get_rect().height/2
            ])
            
        if self.color_borde:
            pygame.draw.rect(self.superficie_esclava, self.color_borde, self.superficie_esclava.get_rect(), 2)

    def actualizar(self):
        pass

    def dibujar(self):
        self.master_form.surface.blit(self.superficie_esclava,self.superficie_esclava)
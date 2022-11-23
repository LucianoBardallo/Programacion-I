import pygame
from pygame.locals import *
from gui_widget import Widget
from configuraciones import *


class BarraProgreso(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_fondo=CYAN,color_borde=(0,0,0),imagen_fondo=None,imagen_progreso=None,valor=1,valor_max=5):
        super().__init__(master,x,y,w,h,color_fondo,color_borde,imagen_fondo,None,None,None,None)
       
              
        self.superficie_elemento = pygame.image.load(imagen_progreso)
        self.superficie_elemento = pygame.transform.scale(self.superficie_elemento,(w/valor_max, h)).convert_alpha()

        self.valor=valor
        self.valor_max=valor_max
        self.renderizar()
        
    def renderizar(self):
        super().renderizar()
        for x in range(self.valor):
            self.superficie_esclava.blit(self.superficie_elemento, (x*self.w/self.valor_max, 0))

    def actualizar(self,lista_eventos):

        self.renderizar()

    


import pygame
from pygame.locals import *
from gui_widget import Widget
from configuraciones import *


class Boton(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_fondo=CYAN,color_borde=(255,0,0),imagen_fondo=None,texto="Button",fuente="Arial",fuente_tamaño=14,fuente_color=CYAN,click=None,click_parametro=None):
        super().__init__(master,x,y,w,h,color_fondo,color_borde,imagen_fondo,texto,fuente,fuente_tamaño,fuente_color)
        self.on_click = click
        self.on_click_param = click_parametro
        self.state = M_STATE_NORMAL
        self.renderizar()
        
    def renderizar(self):
        super().renderizar()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.superficie_esclava.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.superficie_esclava.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def actualizar(self,lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.supuerficie_esclave_colision.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if(self.supuerficie_esclave_colision.collidepoint(evento.pos)):
                    self.on_click(self.on_click_param)

        self.renderizar()

    


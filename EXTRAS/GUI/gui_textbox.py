import pygame
from pygame.locals import *
from gui_widget import Widget
from configuraciones import *


class Texto(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_fondo=(0,0,0),color_borde=CYAN,imagen_fondo=None,texto="Button",fuente="Arial",fuente_tamaño=14,fuente_color=CYAN,click=None,click_parametro=None):
        super().__init__(master,x,y,w,h,color_fondo,color_borde,imagen_fondo,texto,fuente,fuente_tamaño,fuente_color)
        self.on_click = click
        self.on_click_param = click_parametro
        self.estado = M_STATE_NORMAL
        self.escribir_bandera = False
        self.render()
        
    def render(self):
        super().render()
        if self.estado == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.estado == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self,lista_eventos):
        mousePos = pygame.mouse.get_pos()
        self.estado = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(self.escribir_bandera):
                self.estado = M_STATE_CLICK
            else:
                self.estado = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN :
                self.escribir_bandera = self.slave_rect_collide.collidepoint(evento.pos)
            if evento.type == pygame.KEYDOWN and self.escribir_bandera:
                if evento.key == pygame.K_RETURN:
                    self.escribir_bandera = False
                elif evento.key == pygame.K_BACKSPACE:
                    self._texto = self._texto[:-1]
                else:
                    self._texto += evento.unicode

        self.render()

    


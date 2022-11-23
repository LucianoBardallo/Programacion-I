import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Boton

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.x = x
        self.y = y

        if(self.color_background != None):
            self.surface.fill(self.color_background)
    
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
    def __init__(self,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Boton(master=self,x=100,y=50,w=200,h=50,color_fondo=(255,0,0),color_borde=(255,0,255),click=self.on_click_boton1,click_parametro="1234",texto="MENU",fuente="Verdana",fuente_tamaño=30,fuente_color=(0,255,0))
        self.boton2 = Boton(master=self,x=200,y=50,w=200,h=50,color_fondo=(255,0,0),color_borde=(255,0,255),click=self.on_click_boton1,click_parametro="8",texto="MENU 2",fuente="Verdana",fuente_tamaño=30,fuente_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        print("CLICK",parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.actualizar(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.dibujar()
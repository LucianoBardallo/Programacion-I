import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Boton
from configuraciones import *

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Boton(master=self,x=0,y=150,w=200,h=50,color_fondo=CYAN,color_borde=CYAN,click=self.on_click_boton1,click_parametro="form_menu_A",texto="ABRIR A",fuente="Verdana",fuente_tamaño=30,fuente_color=(0,0,0))
        self.boton2 = Boton(master=self,x=250,y=150,w=200,h=50,color_fondo=CYAN,color_borde=CYAN,click=self.on_click_boton1,click_parametro="form_menu_A",texto="MENU 2",fuente="Verdana",fuente_tamaño=30,fuente_color=(0,0,0))
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.actualizar(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.dibujar()
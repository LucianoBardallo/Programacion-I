import pygame
from pygame.locals import *
from configuraciones import *
from gui_form import Form
from gui_button import Boton
from gui_textbox import Texto
from gui_progressbar import BarraProgreso


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Boton(master=self,x=0,y=0,w=140,h=50,color_fondo=None,color_borde=None,imagen_fondo="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",click=self.on_click_boton1,click_parametro="form_menu_B",texto="SUMA +",fuente="Verdana",fuente_tamaño=30,fuente_color=(255,255,255))
        self.boton2 = Boton(master=self,x=0,y=60,w=140,h=50,color_fondo=None,color_borde=None,imagen_fondo="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",click=self.on_click_boton2,click_parametro="form_menu_B",texto="RESTA -",fuente="Verdana",fuente_tamaño=30,fuente_color=(255,255,255))
        self.boton3 = Boton(master=self,x=0,y=120,w=140,h=50,color_fondo=None,color_borde=None,imagen_fondo="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",click=self.on_click_boton3,click_parametro="form_menu_B",texto="MENU",fuente="Verdana",fuente_tamaño=30,fuente_color=(255,255,255))
              
        self.txt1 = Texto(master=self,x=200,y=50,w=240,h=50,color_background=None,color_borde=None,imagen_fondo="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",texto="Text",fuente="Verdana",fuente_tamaño=30,font_color=(0,0,0))
        self.pb1 = BarraProgreso(master=self,x=500,y=50,w=240,h=50,color_fondo=None,color_borde=None,imagen_fondo="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",imagen_progreso="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",valor = 3, valor_max=8)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.txt1,self.pb1]

    def on_click_boton1(self, parametro):
        self.pb1.valor += 1

    def on_click_boton2(self, parametro):
        self.pb1.valor -= 1
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
import pygame
import math
import tarjeta
import random
import textos
import imagenes
import musica
from constantes import *

class Tablero:
    def __init__(self):
        '''
        Crea una lista de tarjetas
        Recibe como parametro la cantidad de tarjetas
        Retorna un dict tablero
        '''
        self.lista_tarjetas = []
        self.tiempo = 0
        self.comienzo_juego = True
        i = 1
        for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
            for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
                if(i > CANTIDAD_TARJETAS_UNICAS):
                    tarjeta_test = tarjeta.Tarjeta("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
                else:
                    tarjeta_test = tarjeta.Tarjeta("0{0}.png".format(i),r"00.png",x,y)
                self.lista_tarjetas.append(tarjeta_test)
                i = i + 1
        
    def mezclar_posicion_tarjetas(self):
        lista_rectangulos = list(map(lambda tarjeta: tarjeta.rect, self.lista_tarjetas))
        random.shuffle(lista_rectangulos)

        for tarjeta, rectangulo in zip(self.lista_tarjetas, lista_rectangulos):
            tarjeta.rect = rectangulo    

    def update(self):
        '''
        verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
        Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
        '''
        tiempo_actual = pygame.time.get_ticks()
        if(tiempo_actual - self.tiempo > 2000 and self.tiempo > 0):
            self.tiempo = 0
            musica.Musica.reproducir_sonidos(r"Clase_17\recursos\equivocado.wav",0.1)
            lista_tarjetas = self.lista_tarjetas
            for aux_tarjeta in lista_tarjetas:
                if(aux_tarjeta.descubierto==False):
                    aux_tarjeta.visible=False
                    
        if(self.tiempo > 0):
            if(self.match()):
                self.tiempo = 0
                musica.Musica.reproducir_sonidos(r"Clase_17\recursos\clic.wav",0.1)

    def render(self,pantalla_juego):
        '''
        Dibuja todos los elementos del tablero en la superficie recibida como parametro
        Recibe como parametro el tablero
        '''
        lista_tarjetas = self.lista_tarjetas
        for tarjeta in lista_tarjetas:
            if(tarjeta.visible):
                pantalla_juego.blit(tarjeta.surface,tarjeta.rect)
            else:
                pantalla_juego.blit(tarjeta.surface_hide,tarjeta.rect)

    def update_background(self,pantalla,imagen,fase):
        if fase == "0":
            pantalla.blit(imagen.surface, [0,0])
        elif fase == "1":
            pantalla.blit(imagen.surface, [0,0])
        elif fase == "2":
            pantalla.blit(imagen.surface, [0,0])
            text = textos.Texto(int(ALTO_PANTALLA/15),"Juego completado",int(ANCHO_PANTALLA/5),int(ALTO_PANTALLA/2)-int(ALTO_PANTALLA/12))
            text2 = textos.Texto(int(ALTO_PANTALLA/15),"'ENTER' para reiniciar",int(ANCHO_PANTALLA/5),int(ALTO_PANTALLA/2))
            text3 = textos.Texto(int(ALTO_PANTALLA/15),"'ESC' para salir",int(ANCHO_PANTALLA/5),int(ALTO_PANTALLA/2)+int(ALTO_PANTALLA/12))
            pantalla.blit(text.texto,(text.rect))
            pantalla.blit(text2.texto,(text2.rect))
            pantalla.blit(text3.texto,(text3.rect))

    def colicion(self,pos_xy):
        '''
        verifica si existe una colicion alguna tarjetas del self y la coordenada recivida como parametro
        Recibe como parametro el tablero y una tupla (X,Y)
        Retorna el indice de la tarjeta que colisiono con la coordenada
        '''
        
        lista_tarjetas = self.lista_tarjetas
        if(self.cantidad_tarjetas_visibles_no_descubiertas() < 2):
            for aux_tarjeta in lista_tarjetas:
                if(aux_tarjeta.rect.collidepoint(pos_xy)):
                    aux_tarjeta.visible=True
                    musica.Musica.reproducir_sonidos(r"Clase_17\recursos\voltear.wav",0.1)
                    self.tiempo = pygame.time.get_ticks()

        icon_start = imagenes.Imagen(r"Clase_18\recursos\start.png",200,100,50,50)
        if(icon_start.rect.collidepoint(pos_xy)):
            return False

    def comprobar_juego(self):
        retorno = True
        for tarjeta in self.lista_tarjetas:
            if tarjeta.visible == False:
                retorno = False  
        return retorno

    def update_icon(self,pantalla,icon,posicion):
        pantalla.blit(icon.surface, posicion)

    def reiniciar_tablero(self,sonido):
        self.mezclar_posicion_tarjetas()
        pygame.mixer.Sound.stop(sonido)
        musica.Musica.reproducir_musica_principal(r"Clase_17\recursos\fondo.wav",0.1)
        for tarjeta in self.lista_tarjetas:
            tarjeta.descubierto = False
            tarjeta.visible = False

    def cantidad_tarjetas_descubiertas(self):
        cantidad = 0
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.descubierto):
                cantidad += 1
        return cantidad
     
    def cantidad_tarjetas_visibles_no_descubiertas(self):
        cantidad = 0
        for tarjeta in self.lista_tarjetas:
            if(tarjeta.visible and not tarjeta.descubierto):
                cantidad += 1
        return cantidad
        
    def match(self):
        for index_p in range(len(self.lista_tarjetas)):
            if(self.lista_tarjetas[index_p].visible and not self.lista_tarjetas[index_p].descubierto):
                aux_primer_tarjeta = self.lista_tarjetas[index_p]
                for index_s in range(index_p+1,len(self.lista_tarjetas)):
                    if(self.lista_tarjetas[index_s].visible and not self.lista_tarjetas[index_s].descubierto ):
                        aux_segunda_tarjeta = self.lista_tarjetas[index_s]
                        if(aux_primer_tarjeta.path_imagen == aux_segunda_tarjeta.path_imagen):
                            aux_primer_tarjeta.descubierto=True
                            aux_segunda_tarjeta.descubierto=True
                            return True
                        
        return False
        







import pygame
import math
import tarjeta
import random
import textos
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

def colicion(tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    
    lista_tarjetas = tablero.lista_tarjetas
    if(tarjeta.cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2):
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.rect.collidepoint(pos_xy)):
                aux_tarjeta.visible=True
                reproducir_sonidos(r"Clase_17\recursos\voltear.wav",0.1)
                tablero.tiempo = pygame.time.get_ticks()

def update(tablero):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    tiempo_actual = pygame.time.get_ticks()
    if(tiempo_actual - tablero.tiempo > 2000 and tablero.tiempo > 0):
        tablero.tiempo = 0
        reproducir_sonidos(r"Clase_17\recursos\equivocado.wav",0.1)
        lista_tarjetas = tablero.lista_tarjetas
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta.descubierto==False):
                aux_tarjeta.visible=False
    
    if(tablero.tiempo > 0):
        if(tarjeta.match(tablero.lista_tarjetas)):
            tablero.tiempo = 0
            reproducir_sonidos(r"Clase_17\recursos\clic.wav",0.1)

def update_background(pantalla,imagen,fase):
    if fase == "0":
        pantalla.blit(imagen.surface, [0,0])
    elif fase == "1":
        pantalla.blit(imagen.surface, [0,0])
    elif fase == "2":
        pantalla.blit(imagen.surface, [0,0])
        text = textos.Texto(int(ALTO_PANTALLA/10),"Juego completado",int(ANCHO_PANTALLA/2),int(ALTO_PANTALLA/2))
        text2 = textos.Texto(int(ALTO_PANTALLA/10),"Aprete 'Enter' para reiniciar",int(ANCHO_PANTALLA/2),int(ALTO_PANTALLA/2)+int(ALTO_PANTALLA/10))
        #text2 = font2.render("APRETE 'ENTER' PARA REINICIAR", True, (0,0,0))
        pantalla.blit(text.texto,(text.rect))
        pantalla.blit(text2.texto,(text2.rect))

def render(tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = tablero.lista_tarjetas
    for tarjeta in lista_tarjetas:
        if(tarjeta.visible):
            pantalla_juego.blit(tarjeta.surface,tarjeta.rect)
        else:
            pantalla_juego.blit(tarjeta.surface_hide,tarjeta.rect)

#MUSICA
def reproducir_sonidos(sonido,volumen):
    sound = pygame.mixer.Sound(sonido)
    sound.set_volume(volumen)
    pygame.mixer.Sound.play(sound)

def reproducir_musica_principal(sonido,volumen):
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play(-1)


#FUNCIONES
def comprobar_juego(tablero):
    retorno = True
    for tarjeta in tablero.lista_tarjetas:
        if tarjeta.visible == False:
            retorno = False  
    return retorno

def comienzo_juego(tablero):
    retorno = True
    for tarjeta in tablero.lista_tarjetas:
        if tarjeta.descubierto == True:
            retorno = False
    return retorno

def reiniciar_tablero(tablero,sonido):
    tablero.mezclar_posicion_tarjetas()
    pygame.mixer.Sound.stop(sonido)
    reproducir_musica_principal(r"Clase_17\recursos\fondo.wav",0.1)
    for tarjeta in tablero.lista_tarjetas:
        tarjeta.descubierto = False
        tarjeta.visible = False


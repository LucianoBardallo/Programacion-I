import pygame
import math
import tarjeta
from constantes import *

def init():
    '''
    Crea una lista de tarjetas
    Recibe como parametro la cantidad de tarjetas
    Retorna un dict tablero
    '''
    d_tablero = {}
    lista_tarjetas = []
    i = 1
    for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
        for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
            else:
                tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
            lista_tarjetas.append(tarjeta_test)
            i = i + 1
    d_tablero["l_tarjetas"] = lista_tarjetas
    d_tablero["tiempo_ultimo_destape"] = 0
    return d_tablero

def colicion(d_tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    
    lista_tarjetas = d_tablero["l_tarjetas"]
    if(tarjeta.cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2):
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta["rect"].collidepoint(pos_xy)):
                aux_tarjeta["visible"]=True
                reproducir_sonidos(r"Clase_17\recursos\voltear.wav",0.1)
                d_tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()

def update(d_tablero):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    tiempo_actual = pygame.time.get_ticks()
    if(tiempo_actual - d_tablero["tiempo_ultimo_destape"] > 1000 and d_tablero["tiempo_ultimo_destape"] > 0):
        d_tablero["tiempo_ultimo_destape"] = 0
        reproducir_sonidos(r"Clase_17\recursos\equivocado.wav",0.1)
        lista_tarjetas = d_tablero["l_tarjetas"]
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta["descubierto"]==False):
                aux_tarjeta["visible"]=False
    
    if(d_tablero["tiempo_ultimo_destape"] > 0):
        if(tarjeta.match(d_tablero["l_tarjetas"])):
            d_tablero["tiempo_ultimo_destape"] = 0
            reproducir_sonidos(r"Clase_17\recursos\clic.wav",0.1)

def update_background(pantalla,imagen,fase):
    if fase == "0":
        pantalla.blit(imagen["surface"], [0,0])
    elif fase == "1":
        pantalla.blit(imagen["surface"], [0,0])
    elif fase == "2":
        pantalla.blit(imagen["surface"], [0,0])
        font = pygame.font.SysFont("Arial Narrow", 150)
        text = font.render("JUEGO COMPLETADO", True, (0, 0, 0))
        pantalla.blit(text,(50,ALTO_PANTALLA/2+200))

def render(d_tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = d_tablero["l_tarjetas"]
    for tarjeta in lista_tarjetas:
        if(tarjeta["visible"]):
            pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
        else:
            pantalla_juego.blit(tarjeta["surface_hide"],tarjeta["rect"])

#MUSICA
def reproducir_sonidos(sonido,volumen):
    sound = pygame.mixer.Sound(sonido)
    sound.set_volume(volumen)
    pygame.mixer.Sound.play(sound)

def reproducir_musica_principal(sonido,volumen):
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play(-1)

#IMAGEN
def crear_imagen(path,ancho,alto,x,y):
    imagen_background = pygame.image.load(path)
    imagen_background = pygame.transform.scale(imagen_background,(ancho,alto))
    dict_fondo = {}
    dict_fondo["surface"] = imagen_background
    dict_fondo["rect"] = dict_fondo["surface"].get_rect()
    dict_fondo["rect"].x = x
    dict_fondo["rect"].y = y
    return dict_fondo

#FUNCIONES
def comprobar_juego(d_tablero):
    retorno = True
    for tarjeta in d_tablero["l_tarjetas"]:
        if tarjeta["descubierto"] == False:
            retorno = False  
    return retorno

def comienzo_juego(d_tablero):
    retorno = True
    for tarjeta in d_tablero["l_tarjetas"]:
        if tarjeta["descubierto"] == True:
            retorno = False
    return retorno

def reiniciar_tablero(d_tablero):
    for tarjeta in d_tablero["l_tarjetas"]:
        tarjeta["descubierto"] = False
        tarjeta["visible"] = False
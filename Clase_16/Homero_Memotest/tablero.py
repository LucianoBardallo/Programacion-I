import pygame, math, random, tarjeta
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

def colicion(tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    lista_tarjetas = tablero["l_tarjetas"]
    for tarjeta in lista_tarjetas:
            if tarjeta["rect"].collidepoint(pos_xy):
                tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()
                return tarjeta
                

def update(tablero):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    tiempo_actual = pygame.time.get_ticks()
    if(tiempo_actual - tablero["tiempo_ultimo_destape"] > 2000 and tablero["tiempo_ultimo_destape"] > 0):
        tablero["tiempo_ultimo_destape"] = 0
        lista_tarjetas = tablero["l_tarjetas"]
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta["descubierto"]==False):
                aux_tarjeta["visible"]=False

        

def tomar_primer_tarjeta(tarjeta):
    tarjeta_uno = tarjeta
    reproductor_sonidos(r"Clase_16\Homero_Memotest\recursos\voltear.wav",0.1)
    mostrar(tarjeta)
    print("PRIMER TARJETA")
    return tarjeta_uno

def tomar_segunda_tarjeta(tarjeta):
    tarjeta_dos = tarjeta
    mostrar(tarjeta)
    print("SEGUNDA TARJETA")
    return tarjeta_dos

def comparar_tarjetas(tablero,tarjeta_uno,tarjeta_dos):
    if tarjeta_uno["path_imagen"] == tarjeta_dos["path_imagen"]:
        tarjeta_uno["descubierto"] = True
        tarjeta_dos["descubierto"] = True
        print("COINCIDE\n")
        reproductor_sonidos(r"Clase_16\Homero_Memotest\recursos\clic.wav",0.1)
        return True
     
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

#FUNCIONES AUXILIARES            
def comprobar_final(tablero):
    lista_tarjetas = tablero["l_tarjetas"]
    if tarjeta.cantidad_tarjetas_descubiertas(lista_tarjetas) == len(lista_tarjetas):
        return True

def ocultar_imagenes(d_tablero):
    for tarjeta in d_tablero["l_tarjetas"]:
        if tarjeta["descubierto"] == False:
            tarjeta["visible"] = False

def reproductor_sonidos(sonido,volumen):
    sound = pygame.mixer.Sound(sonido)
    sound.set_volume(volumen)
    pygame.mixer.Sound.play(sound)

def reproducir_musica_principal(sonido,volumen):
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play(-1)

def mostrar(tarjeta):
    tarjeta["visible"] = True
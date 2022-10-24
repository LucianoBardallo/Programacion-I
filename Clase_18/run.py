import pygame
import tablero
import random
from constantes import *

pygame.init() #Se inicializa pygame

#AJUSTES PANTALLA
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

#SETEO DE TIEMPOS
tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

tick_1500ms = pygame.USEREVENT+1
pygame.time.set_timer(tick_1500ms,1500)

#MUSICA DE FONDO
tablero.reproducir_musica_principal(r"Clase_17\recursos\fondo.wav",0.1)

#CREACION DE IMAGENES
tablero_fondo = tablero.crear_imagen(r"Clase_17\recursos\fondo.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
tablero_fondo_win = tablero.crear_imagen(r"Clase_17\recursos\win.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
tablero_fondo_start = tablero.crear_imagen(r"Clase_17\recursos\fondo_start.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
icon_start = tablero.crear_imagen(r"Clase_17\recursos\start.png",200,100,50,50)

#CREACION DE TABLERO
tablero_juego = tablero.init()
clock_fps = pygame.time.Clock()

#BAANDERAS
una_pasada = True
una_pasada2 = True
running = True

#BUCLE PRINCIPAL DEL JUEGO
while running:
    #SETEA FPS
    tiempo = clock_fps.tick(60)

    for event in pygame.event.get():
        #VERIFICA SI EL USAURIO CERRO EL JUEGO
        if event.type == pygame.QUIT:
            running = False
        #VERIFICA SI EL USUARIO INTERACTUO CON EL MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.colicion(tablero_juego,event.pos)
        #VERIFICA SI EL USUARIO APRETO EL ENTER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                terminar_juego = False
                tablero.reiniciar_tablero(tablero_juego)
        #EVENTOS DE TIEMPO
        if event.type == tick_1s:
            pass
        if event.type == tick_1500ms:
            pass
    
    #VERIFICA SI EL USUARIO EMPEZO EL JUEGO
    terminar_juego = tablero.comprobar_juego(tablero_juego)
    if terminar_juego == False:
        if una_pasada:
            una_pasada = False
        tablero.update(tablero_juego)
        tablero.update_background(pantalla_juego,tablero_fondo,"1")
        tablero.render(tablero_juego,pantalla_juego)
    else:
        pygame.mixer.music.stop()
        if una_pasada2:
            tablero.reproducir_sonidos(r"Clase_17\recursos\ganador.mp3",0.1)
            una_pasada2= False
        tablero.update_background(pantalla_juego,tablero_fondo_win,"2")
    pygame.display.flip()

# DONE! TIME TO QUIT
pygame.quit()

# Se pinta el fondo de la ventana de blanco
    #pantalla_juego.fill((255, 255, 255))

'''
if start:
        tablero.update_background(pantalla_juego,tablero_fondo_start,"0")
        tablero.update_icon(pantalla_juego,icon_start)
    else:
        #VERIFICA SI EL USUARIO TERMINO EL JUEGO
'''
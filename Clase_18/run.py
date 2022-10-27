import pygame
import random
import imagenes
import tablero
import musica
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

#MUSICA
musica.Musica.reproducir_musica_principal(r"Clase_18\recursos\fondo.wav",0.1)
sonido_ganador = pygame.mixer.Sound(r"Clase_18\recursos\ganador.mp3")
sonido_ganador.set_volume(0.1)

#CREACION DE IMAGENES
tablero_fondo = imagenes.Imagen(r"Clase_18\recursos\fondo.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
tablero_fondo_win = imagenes.Imagen(r"Clase_18\recursos\win.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
tablero_fondo_start = imagenes.Imagen(r"Clase_18\recursos\fondo_start.jpg",ANCHO_PANTALLA,ALTO_PANTALLA,0,0)
icon_start = imagenes.Imagen(r"Clase_18\recursos\start.png",200,100,50,50)
icon_exit = imagenes.Imagen(r"Clase_18\recursos\salir.png",200,100,50,50)

#CREACION DE TABLERO
tablero_juego = tablero.Tablero()
tablero_juego.mezclar_posicion_tarjetas()

#INICIO DE RELOJ
clock_fps = pygame.time.Clock()

#BAANDERAS
una_pasada = True
una_pasada2 = True
comienzo_juego = True
running = True

def play():
    running = True

    while running:
        #SETEA FPS
        tiempo = clock_fps.tick(60)

        #LISTA DE EVENTOS
        for event in pygame.event.get():

            #VERIFICA SI EL USAURIO CERRO EL JUEGO
            if event.type == pygame.QUIT:
                running = False

            #VERIFICA SI EL USUARIO INTERACTUO CON EL MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN :
                comienzo_juego = tablero_juego.colicion(event.pos)
                tablero_juego.colicion(event.pos)

            #VERIFICA SI EL USUARIO APRETO EL ENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    terminar_juego = False
                    una_pasada = True
                    tablero_juego.reiniciar_tablero(sonido_ganador)
                if event.key == pygame.K_ESCAPE:
                    running = False

            #EVENTOS DE TIEMPO
            if event.type == tick_1s:
                pass
            if event.type == tick_1500ms:
                pass
            
        #VERIFICA EL ESTADO DEL JUEGO
        terminar_juego = tablero_juego.comprobar_juego()
        if comienzo_juego:
            tablero_juego.update_background(pantalla_juego,tablero_fondo_start,"0")
            tablero_juego.update_icon(pantalla_juego,icon_start,(50,50))
            #tablero.update_icon(pantalla_juego,icon_exit,(ANCHO_PANTALLA-250,ALTO_PANTALLA-300))
        else:
            if terminar_juego == False:
                tablero_juego.update()
                tablero_juego.update_background(pantalla_juego,tablero_fondo,"1")
                tablero_juego.render(pantalla_juego)
            else:
                pygame.mixer.music.stop()
                if una_pasada:
                    pygame.mixer.Sound.play(sonido_ganador)
                    una_pasada= False
                tablero_juego.update_background(pantalla_juego,tablero_fondo_win,"2")
            
        pygame.display.flip()

#BUCLE PRINCIPAL DEL JUEGO
def main_menu():
    #BAANDERAS
    una_pasada = True
    comienzo_juego = True
    running = True

    while running:
        #SETEA FPS
        tiempo = clock_fps.tick(60)

        #LISTA DE EVENTOS
        for event in pygame.event.get():

            #VERIFICA SI EL USAURIO CERRO EL JUEGO
            if event.type == pygame.QUIT:
                running = False

            #VERIFICA SI EL USUARIO INTERACTUO CON EL MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN :
                comienzo_juego = tablero_juego.colicion(event.pos)
                tablero_juego.colicion(event.pos)

            #VERIFICA SI EL USUARIO APRETO EL ENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    terminar_juego = False
                    una_pasada = True
                    tablero_juego.reiniciar_tablero(sonido_ganador)
                if event.key == pygame.K_ESCAPE:
                    running = False

            #EVENTOS DE TIEMPO
            if event.type == tick_1s:
                pass
            if event.type == tick_1500ms:
                pass
            
        #VERIFICA EL ESTADO DEL JUEGO
        terminar_juego = tablero_juego.comprobar_juego()
        if comienzo_juego:
            tablero_juego.update_background(pantalla_juego,tablero_fondo_start,"0")
            tablero_juego.update_icon(pantalla_juego,icon_start,(50,50))
            #tablero.update_icon(pantalla_juego,icon_exit,(ANCHO_PANTALLA-250,ALTO_PANTALLA-300))
        else:
            if terminar_juego == False:
                tablero_juego.update()
                tablero_juego.update_background(pantalla_juego,tablero_fondo,"1")
                tablero_juego.render(pantalla_juego)
            else:
                pygame.mixer.music.stop()
                if una_pasada:
                    pygame.mixer.Sound.play(sonido_ganador)
                    una_pasada= False
                tablero_juego.update_background(pantalla_juego,tablero_fondo_win,"2")
            
        pygame.display.flip()

main_menu()

#TIEMPO DE SALIR
pygame.quit()

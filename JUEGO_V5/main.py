import pygame
import sys
from pygame.locals import *
from configuraciones import *
from auxiliar import *
from botones import Boton
from imagenes import Imagen
from jugador import Jugador
from objetos import *
from enemigos import *
from nivel import Nivel

flags = DOUBLEBUF

PANTALLA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
reloj = pygame.time.Clock()
pygame.init()

fondo_juego = Imagen(RUTA_IMAGEN + r"Menu\Fondo\space_out.jpg",ANCHO_VENTANA+300,ALTO_VENTANA,0,0)
fondo_nivel = Imagen(RUTA_IMAGEN + r"Menu\Fondo\planets.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(RUTA_IMAGEN + r"Menu\Fondo\menu.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_puntuacion = Imagen(RUTA_IMAGEN + r"Menu\Button\07.png",20,20,1000,10)
fondo_municion = Imagen(RUTA_IMAGEN + r"Menu\Button\08.png",20,20,400,ALTO_VENTANA-30)
fondo_ganador = Imagen(RUTA_IMAGEN + r"Menu\Fondo\level_complete.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)

#CARGA UNA FUENTE
def obtener_fuente(tamaño):
    return pygame.font.Font(RUTA_IMAGEN + r"\Menu\Text\font.ttf", tamaño)

fuente_interface = obtener_fuente(20)


#JUEGO
def juego(opcion):
    tiempo = pygame.time.get_ticks()

    nivel = Nivel(opcion,PANTALLA)

    while True:
        teclas = pygame.key.get_pressed()
        eventos = pygame.event.get()

        delta_ms = reloj.tick(FPS)
        
        PANTALLA.blit(fondo_juego.surface,fondo_juego.rect)

        nivel.actualizar_nivel(delta_ms,teclas,eventos)   

        pygame.display.flip()

#SELECCION DE NIVEL
def seleccion_nivel():
    nivel_1 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\01.png")
    nivel_2 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\02.png")
    nivel_3 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\03.png")
    nivel_4 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\04.png")
    nivel_5 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\05.png")
    nivel_6 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\06.png")
    nivel_7 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\07.png")
    nivel_8 = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\08.png")

    while True:
        PANTALLA.blit(fondo_nivel.surface, (0,0))
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NIVEL_1 = Boton(imagen=nivel_1, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_2 = Boton(imagen=nivel_2, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_3 = Boton(imagen=nivel_3, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_4 = Boton(imagen=nivel_4, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_5 = Boton(imagen=nivel_5, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_6 = Boton(imagen=nivel_6, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_7 = Boton(imagen=nivel_7, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        NIVEL_8 = Boton(imagen=nivel_8, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=obtener_fuente(55), color_base=CYAN, color_flotante="White")

        QUIT = Boton(imagen=None, pos=(ANCHO_VENTANA // 2, int(ALTO_VENTANA * 0.9)), 
        texto_entrada="QUIT", fuente=obtener_fuente(30), color_base=CYAN, color_flotante="White")


        for boton in [NIVEL_1, NIVEL_2, NIVEL_3, NIVEL_4, NIVEL_5, NIVEL_6, NIVEL_7, NIVEL_8, QUIT]:
            boton.cambiar_color(MENU_MOUSE_POS)
            boton.actualizar(PANTALLA)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL_1.verificar_entrada(MENU_MOUSE_POS):
                    juego("nivel_1")
                if NIVEL_2.verificar_entrada(MENU_MOUSE_POS):
                    juego("nivel_2")
                if NIVEL_3.verificar_entrada(MENU_MOUSE_POS):
                    juego("nivel_3")
                if NIVEL_4.verificar_entrada(MENU_MOUSE_POS):
                    juego("4")
                if NIVEL_5.verificar_entrada(MENU_MOUSE_POS):
                    juego("5")
                if NIVEL_6.verificar_entrada(MENU_MOUSE_POS):
                    juego("6")
                if NIVEL_7.verificar_entrada(MENU_MOUSE_POS):
                    juego("7")
                if NIVEL_8.verificar_entrada(MENU_MOUSE_POS):
                    juego("8")
                if QUIT.verificar_entrada(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU OPCIONES        
def opciones():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("white")

        texto_opciones = obtener_fuente(45).render("MENU DE OPCIONES.", True, "Black")
        rect_opciones = texto_opciones.get_rect(center=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/3)))
        PANTALLA.blit(texto_opciones, rect_opciones)

        OPCIONES_ATRAS = Boton(imagen=None, pos=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/2)), 
            texto_entrada="BACK", fuente=obtener_fuente(75), color_base="Black", color_flotante="Green")

        OPCIONES_ATRAS.cambiar_color(OPTIONS_MOUSE_POS)
        OPCIONES_ATRAS.actualizar(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if OPCIONES_ATRAS.verificar_entrada(OPTIONS_MOUSE_POS):
                    menu_principal()

        pygame.display.flip()

#MENU PRINCIPAL
def menu_principal():
    while True:
        PANTALLA.blit(fondo_menu.surface, (0,0))
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        texto_menu = obtener_fuente(50).render("SPACE ADVENTURE", True, DORADO)
        rect_menu = texto_menu.get_rect(center=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.2)))

        JUGAR_BOTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.4)), 
            texto_entrada="JUGAR", fuente=obtener_fuente(40), color_base=CYAN, color_flotante="White")
        OPCIONES_BOTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.55)), 
            texto_entrada="OPTIONES", fuente=obtener_fuente(40), color_base=CYAN, color_flotante="White")
        SALIR_BOTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.7)), 
            texto_entrada="SALIR", fuente=obtener_fuente(40), color_base=CYAN, color_flotante="White")

        PANTALLA.blit(texto_menu, rect_menu)

        for boton in [JUGAR_BOTON, OPCIONES_BOTON, SALIR_BOTON]:
            boton.cambiar_color(MENU_MOUSE_POS)
            boton.actualizar(PANTALLA)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_BOTON.verificar_entrada(MENU_MOUSE_POS):
                    seleccion_nivel()
                if OPCIONES_BOTON.verificar_entrada(MENU_MOUSE_POS):
                    opciones()
                if SALIR_BOTON.verificar_entrada(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU DEL JUEGO
menu_principal()
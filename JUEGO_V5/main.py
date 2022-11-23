import pygame
import sys
from pygame.locals import *
from configuraciones import *
from auxiliar import *
from botones import Boton
from imagenes import Imagen
from plataformas import Plataforma, Muro
from jugador import Jugador
from objetos import *
from botínes import Botín
from enemigos import *
from balas import Bala

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
def juego(nivel):
    tiempo = pygame.time.get_ticks()
    jugador = Jugador(x = 60, y = 40, velocidad_movimiento = 8, gravedad = 8, fuerza_salto = 8, frame_rate_ms = 40,frame_rate_jump_ms = 120, move_rate_ms = 20, altura_salto = 180, p_scale=0.2)
    
    
    corazones = []
    x = 100
    for i in range(5):
        corazones.append(Imagen(RUTA_IMAGEN + r"Menu\Button\04.png",20,20,x,10))
        x+=30

    municiones = []
    x = 500
    for i in range(jugador.municion):
        municiones.append(Imagen(RUTA_IMAGEN + r"Characters\robot\Objects\Bullet_1.png",20,20,x,ALTO_VENTANA-30))
        x+=30

    #PLATAFORMAS
    plataformas = []
    muros = []
    objetos = []
    objetos_animados = []
    puerta_final = []
    interruptores = []
    enemigos = []
    enemigos_rango = []
    x = 0
    y = 0
    for i in range(0,30):
        if i < 1:
            #OBJETOS
            objetos_animados.append(Objeto_Animado(x=70,y=80,ancho=80,alto=120,tipo_desbloqueado=6,tipo_abierto=4,tipo_bloqueado=5))
            puerta_final.append(Objeto_Animado(x=1050,y=430,ancho=80,alto=120,tipo_desbloqueado=6,tipo_abierto=4,tipo_bloqueado=5))
            interruptores.append(Objeto_Animado(x=400,y=125,ancho=25,alto=75,tipo_desbloqueado=8,tipo_abierto=7,tipo_bloqueado=8))
            objetos.append(Objeto_Estatico(x=450,y=475,ancho=75,alto=75,tipo_desbloqueado=2))
            objetos.append(Objeto_Estatico(x=525,y=475,ancho=75,alto=75,tipo_desbloqueado=2))
            objetos.append(Objeto_Estatico(x=485,y=400,ancho=75,alto=75,tipo_desbloqueado=2))
        if i < 3:
            plataformas.append(Plataforma(x+50,y=200,ancho=50,alto=50,tipo=1))
            plataformas.append(Plataforma(x+150,y=350,ancho=50,alto=50,tipo=1))
            plataformas.append(Plataforma(x+350,y=200,ancho=50,alto=50,tipo=1))
        if i < 6:
            plataformas.append(Plataforma(x+900,y=150,ancho=50,alto=50,tipo=1))
        if i < 8:
            muros.append(Muro(x=300,y=y,ancho=50,alto=50,tipo=4))
        if i < 12:
            plataformas.append(Plataforma(x+600,y=300,ancho=50,alto=50,tipo=1))
            #Cambia Y
            muros.append(Muro(x=0,y=y,ancho=50,alto=50,tipo=4))
            muros.append(Muro(x=1150,y=y,ancho=50,alto=50,tipo=4))
        if i < 23:
            plataformas.append(Plataforma(x,y=550,ancho=50,alto=50,tipo=1))
            muros.append(Muro(x,y=0,ancho=50,alto=50,tipo=1,reverso = True))
        x += 50
        y += 50

    x = 0
    y = 0
    botínes = []
    for i in range(10):
        if i < 5:
            botínes.append(Botín(x+900,y=50,frame_rate_ms=60))
        botínes.append(Botín(x+650,y=200,frame_rate_ms=60))
        x += 50
    for i in range(5):
        botínes.append(Botín(x=230,y=y+50,frame_rate_ms=60))
        y += 50

    enemigo_1 = Enemigo_Melee(x=500,y=400,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=400)
    enemigo_2 = Enemigo_Melee(x=800,y=190,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=200)
    enemigo_3 = Enemigo_Distancia(x=400,y=100,velocidad_movimiento=0,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=0)
    enemigos.append(enemigo_1)
    enemigos.append(enemigo_2)
    enemigos_rango.append(enemigo_3)

    while True:
        teclas = pygame.key.get_pressed()
        eventos = pygame.event.get()

        delta_ms = reloj.tick(FPS)
        
        PANTALLA.blit(fondo_juego.surface,fondo_juego.rect)

        listas = [plataformas,objetos_animados,objetos,muros,botínes,interruptores,puerta_final]
        for lista in listas:
            for elemento in lista:
                if type(elemento) == Botín:
                    elemento.actualizar(delta_ms)
                elemento.renderizar(PANTALLA)
                
        for enemigo in enemigos:
            if not enemigo.vivo:
                enemigos.remove(enemigo)
                jugador.puntuacion += 200
            enemigo.actualizar(PANTALLA,delta_ms,plataformas,jugador.municiones)
        for enemigo in enemigos_rango:
            if not enemigo.vivo:
                enemigos_rango.remove(enemigo)
                jugador.puntuacion += 200
            enemigo.actualizar(PANTALLA,delta_ms,plataformas,jugador.municiones,jugador.rectangulo_colision)

        if not jugador.ganar:
            for corazon in corazones:
                PANTALLA.blit(corazon.surface,corazon.rect)
            for municion in municiones:
                PANTALLA.blit(municion.surface,municion.rect)
        
            texto_entrada_puntuacion = f"{jugador.puntuacion}".zfill(7)
            texto_puntuacion = fuente_interface.render(texto_entrada_puntuacion, True, CYAN)
            texto_entrada_municion = f"{jugador.municion}"
            texto_municion = fuente_interface.render(texto_entrada_municion,True,CYAN)
            texto_entrada_vida = "VIDA"
            texto_vida = fuente_interface.render(texto_entrada_vida,True,CYAN)
            texto_entrada_municion = "MUNICION"
            texto_municion = fuente_interface.render(texto_entrada_municion,True,CYAN)
            texto_entrada_muerto = "HAS MUERTO"
            texto_muerto = fuente_interface.render(texto_entrada_muerto,True,RED)

            PANTALLA.blit(fondo_puntuacion.surface,fondo_puntuacion.rect)
            PANTALLA.blit(texto_puntuacion,(1030,10))
            PANTALLA.blit(texto_vida,(10,10))
            PANTALLA.blit(texto_municion,(300,ALTO_VENTANA-30))
            if not jugador.vivo:
                PANTALLA.blit(texto_muerto,(ANCHO_VENTANA//2-50,ALTO_VENTANA//2-50))
        else:
            PANTALLA.blit(fondo_ganador.surface,fondo_ganador.rect)

        jugador.actualizar(delta_ms,PANTALLA,teclas,eventos,municiones,plataformas,objetos,objetos_animados,muros,botínes,interruptores,puerta_final,enemigos,corazones,enemigos_rango)   
        
        
        

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
                    juego("1")
                if NIVEL_2.verificar_entrada(MENU_MOUSE_POS):
                    juego("2")
                if NIVEL_3.verificar_entrada(MENU_MOUSE_POS):
                    juego("3")
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
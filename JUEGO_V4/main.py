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

SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
reloj = pygame.time.Clock()
pygame.init()

fondo_juego = Imagen(RUTA_IMAGEN + r"Menu\Fondo\space_out.jpg",ANCHO_VENTANA+300,ALTO_VENTANA,0,0)
fondo_nivel = Imagen(RUTA_IMAGEN + r"Menu\Fondo\planets.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(RUTA_IMAGEN + r"Menu\Fondo\menu.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_puntuacion = Imagen(RUTA_IMAGEN + r"Menu\Button\07.png",20,20,1000,10)
fondo_municion = Imagen(RUTA_IMAGEN + r"Menu\Button\08.png",20,20,10,60)
# fondo_button1 = Imagen(PATH_IMAGE + r"Menu\hologram_UI\Card X2\Card X2.png",280,40,-10,0)
# fondo_button2 = Imagen(PATH_IMAGE + r"Menu\hologram_UI\Card X2\Card X2.png",210,40,980,0)
# fondo_button3 = Imagen(PATH_IMAGE + r"Menu\hologram_UI\Card X2\Card X2.png",1300,40,-60,ALTO_VENTANA-40)

#CARGA UNA FUENTE
def get_font(tamaño):
    return pygame.font.Font(RUTA_IMAGEN + r"\Menu\Text\font.ttf", tamaño)

fuente_interface = get_font(20)

#JUEGO
def play(nivel):
    tiempo = pygame.time.get_ticks()
    jugador = Jugador(x = 60, y = 40, velocidad_movimiento = 8, gravedad = 8, fuerza_salto = 8, frame_rate_ms = 40,frame_rate_jump_ms = 120, move_rate_ms = 20, altura_salto = 180, p_scale=0.2,interval_time_jump=300)
    
    corazones = []
    x = 100
    for i in range(jugador.vidas):
        corazones.append(Imagen(RUTA_IMAGEN + r"Menu\Button\04.png",20,20,x,10))
        x+=30

    municiones = []
    x = 200
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

    enemigo_1 = Enemigo(x=1100,y=400,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,pasos=800)
    enemigo_2 = Enemigo(x=1100,y=190,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,pasos=400)
    enemigos.append(enemigo_1)
    enemigos.append(enemigo_2)

    while True:
        teclas = pygame.key.get_pressed()
        eventos = pygame.event.get()

        delta_ms = reloj.tick(FPS)
        
        SCREEN.blit(fondo_juego.surface,fondo_juego.rect)

        for plataforma in plataformas:
            plataforma.renderizar(SCREEN)
        for objeto in objetos_animados:
            objeto.renderizar(SCREEN)
        for objeto in objetos:
            objeto.renderizar(SCREEN)
        for muro in muros:
            muro.renderizar(SCREEN)
        for botín in botínes:
            botín.actualizar(delta_ms)
            botín.renderizar(SCREEN)
        for interruptor in interruptores:
            interruptor.renderizar(SCREEN)
        for puerta in puerta_final:
            puerta.renderizar(SCREEN)
        for enemigo in enemigos:
            if enemigo.vidas == 0:
                enemigos.remove(enemigo)
                jugador.puntuacion += 200
            enemigo.actualizar(delta_ms,plataformas,jugador.municiones)
            enemigo.renderizar(SCREEN)

        for corazon in corazones:
            SCREEN.blit(corazon.surface,corazon.rect)
        for municion in municiones:
            SCREEN.blit(municion.surface,municion.rect)
    
        texto_entrada_puntuacion = f"{jugador.puntuacion}".zfill(7)
        texto_puntuacion = fuente_interface.render(texto_entrada_puntuacion, True, CYAN)
        texto_entrada_municion = f"{jugador.municion}"
        texto_municion = fuente_interface.render(texto_entrada_municion,True,CYAN)
        texto_entrada_vida = "VIDA"
        texto_vida = fuente_interface.render(texto_entrada_vida,True,CYAN)
        texto_entrada_municion = "MUNICION"
        texto_municion = fuente_interface.render(texto_entrada_municion,True,CYAN)
        
        
        SCREEN.blit(fondo_puntuacion.surface,fondo_puntuacion.rect)
        SCREEN.blit(texto_puntuacion,(1030,10))
        SCREEN.blit(texto_vida,(10,10))
        SCREEN.blit(texto_municion,(10,ALTO_VENTANA-30))
        

        jugador.eventos(delta_ms,teclas,eventos,municiones)
        jugador.actualizar(delta_ms,plataformas,objetos,objetos_animados,muros,botínes,interruptores,puerta_final,enemigos,corazones)
        jugador.renderizar(SCREEN)
        jugador.actualizar_bala(delta_ms,SCREEN)

        pygame.display.flip()

#SELECCION DE NIVEL
def selec_level():
    nivel_one = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\01.png")
    nivel_two = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\02.png")
    nivel_three = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\03.png")
    nivel_four = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\04.png")
    nivel_five = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\05.png")
    nivel_six = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\06.png")
    nivel_seven = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\07.png")
    nivel_eight = pygame.image.load(RUTA_IMAGEN + r"Menu\Levels\08.png")

    while True:
        SCREEN.blit(fondo_nivel.surface, (0,0))
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NIVEL_1 = Boton(imagen=nivel_one, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_2 = Boton(imagen=nivel_two, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_3 = Boton(imagen=nivel_three, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_4 = Boton(imagen=nivel_four, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.28)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_5 = Boton(imagen=nivel_five, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_6 = Boton(imagen=nivel_six, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_7 = Boton(imagen=nivel_seven, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        NIVEL_8 = Boton(imagen=nivel_eight, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.70)), 
            texto_entrada="", fuente=get_font(55), color_base=CYAN, color_flotante="White")

        QUIT = Boton(imagen=None, pos=(ANCHO_VENTANA // 2, int(ALTO_VENTANA * 0.9)), 
        texto_entrada="QUIT", fuente=get_font(30), color_base=CYAN, color_flotante="White")


        for button in [NIVEL_1, NIVEL_2, NIVEL_3, NIVEL_4, NIVEL_5, NIVEL_6, NIVEL_7, NIVEL_8, QUIT]:
            button.cambiar_color(MENU_MOUSE_POS)
            button.actualizar(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL_1.verificar_entrada(MENU_MOUSE_POS):
                    play("1")
                if NIVEL_2.verificar_entrada(MENU_MOUSE_POS):
                    play("2")
                if NIVEL_3.verificar_entrada(MENU_MOUSE_POS):
                    play("3")
                if NIVEL_4.verificar_entrada(MENU_MOUSE_POS):
                    play("4")
                if NIVEL_5.verificar_entrada(MENU_MOUSE_POS):
                    play("5")
                if NIVEL_6.verificar_entrada(MENU_MOUSE_POS):
                    play("6")
                if NIVEL_7.verificar_entrada(MENU_MOUSE_POS):
                    play("7")
                if NIVEL_8.verificar_entrada(MENU_MOUSE_POS):
                    play("8")
                if QUIT.verificar_entrada(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU OPCIONES        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        opcion_text = get_font(45).render("MENU DE OPCIONES.", True, "Black")
        opcion_rect = opcion_text.get_rect(center=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/3)))
        SCREEN.blit(opcion_text, opcion_rect)

        OPTIONS_BACK = Boton(imagen=None, pos=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/2)), 
            texto_entrada="BACK", fuente=get_font(75), color_base="Black", color_flotante="Green")

        OPTIONS_BACK.cambiar_color(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.actualizar(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.verificar_entrada(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.flip()

#MENU PRINCIPAL
def main_menu():
    while True:
        SCREEN.blit(fondo_menu.surface, (0,0))
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_text = get_font(50).render("SPACE ADVENTURE", True, DORADO)
        menu_rect = menu_text.get_rect(center=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.2)))

        PLAY_BUTTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.4)), 
            texto_entrada="JUGAR", fuente=get_font(40), color_base=CYAN, color_flotante="White")
        OPTIONS_BUTTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.55)), 
            texto_entrada="OPTIONES", fuente=get_font(40), color_base=CYAN, color_flotante="White")
        QUIT_BUTTON = Boton(imagen=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.7)), 
            texto_entrada="SALIR", fuente=get_font(40), color_base=CYAN, color_flotante="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.cambiar_color(MENU_MOUSE_POS)
            button.actualizar(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.verificar_entrada(MENU_MOUSE_POS):
                    selec_level()
                if OPTIONS_BUTTON.verificar_entrada(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.verificar_entrada(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU DEL JUEGO
main_menu()
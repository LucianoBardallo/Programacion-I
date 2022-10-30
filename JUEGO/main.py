import pygame
import sys
import player
import enemigo
from imagenes import Imagen
from constantes import *
from botones import *

#SETEA LA VENTANA
SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

#CARGA IMAGENES
fondo_juego = Imagen(PATH_IMAGE + r"locations\forest\all.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(PATH_IMAGE + r"menu\frog.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
cuadro_menu = Imagen(PATH_IMAGE + r"menu\rect.png",ANCHO_VENTANA-int(ANCHO_VENTANA/3),ALTO_VENTANA,0,0)

#CARGA UNA FUENTE
def get_font(tamaño):
    return pygame.font.Font(PATH_IMAGE + r"\menu\font.ttf", tamaño)

#CODIGO DEL JUEGO
def play():
    clock.tick(FPS)
    tiempo = pygame.time.get_ticks()

    #ASIGNACION DE CLASSES
    player_1 = player.Player(0,500,8,16,2,10)
    enemigo_1 = enemigo.Enemigo(1000,450,2,tiempo)
    enemigo_2 = enemigo.Enemigo(1100,450,2,tiempo)
    enemigo_3 = enemigo.Enemigo(1200,450,2,tiempo)
    muercielagos = enemigo.GrupoBatterflies(4)

    #BUBLE PRINCIPAL DEL JUEGO
    while True:
        #TOMA POSICION DEL MOUSE
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        #INICIO DE EVENTOS
        for event in pygame.event.get():
            #EVENTO PARA SALIR
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #EVENTO CUANDO APRETA UNA TECLA
            if event.type == pygame.KEYDOWN:
                #EVENTO PARA SALTAR
                if event.key == pygame.K_SPACE:
                    player_1.control("JUMP")

            #EVENTO CUANDO DEJA DE APRETAR ALGUNA TECLA
            if event.type == pygame.KEYUP:
                #EVENTO PARA QUEDARSE QUIETO
                if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT:
                    player_1.control("STAY")
                
        #EVENTOS DE MANTENER APRETADO ALGUNA TECLA
        lista_teclas = pygame.key.get_pressed()
        #EVENTO PARA MOVER A LA DERECHA
        if(lista_teclas[pygame.K_RIGHT] and not lista_teclas[pygame.K_LEFT]):
            player_1.direccion = "right"
            player_1.control("WALK_R")
            player_1.speed_walk = 8
            #EVENTO DE CORRER A LA DERECHA
            if lista_teclas[pygame.K_LSHIFT]:
                player_1.speed_walk = player_1.speed_run
        #EVENTO PARA MOVER A LA IZQUIERDA
        elif(lista_teclas[pygame.K_LEFT] and not lista_teclas[pygame.K_RIGHT]):
            player_1.direccion = "left"
            player_1.control("WALK_L")
            player_1.speed_walk = 8
            #EVENTO PARA CORRER A LA IZQUIERDA
            if lista_teclas[pygame.K_LSHIFT]:
                player_1.speed_walk = player_1.speed_run
        #EVENTO PARA QUEDARSE QUIETO
        else:
            player_1.control("STAY")

        #CARGA FONDO
        SCREEN.blit(fondo_juego.surface,fondo_juego.rect)
        
        #ACTUALIZA JUEGO
        player_1.draw(SCREEN)
        player_1.update()
        enemigo_1.draw(SCREEN)
        enemigo_1.update()
        enemigo_1.colicion(player_1.rect)
        enemigo_2.draw(SCREEN)
        enemigo_2.update()
        enemigo_2.colicion(player_1.rect)
        enemigo_3.draw(SCREEN)
        enemigo_3.update()
        enemigo_3.colicion(player_1.rect)

        #DIBUJA EL NIVEL
        muercielagos.updatear_murcielagos(SCREEN,player_1.rect)
        #ACTUALIZA PANTALLA
        pygame.display.flip()

#MENU OPCIONES        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        opcion_text = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        opcion_rect = opcion_text.get_rect(center=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/3)))
        SCREEN.blit(opcion_text, opcion_rect)

        OPTIONS_BACK = Button(image=None, pos=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/2)), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.flip()

#MENU PRINCIPAL
def main_menu():
    while True:
        SCREEN.blit(fondo_menu.surface, (0,0))
        SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_text = get_font(30).render("MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(ANCHO_VENTANA-250, 100))
        menu_text2 = get_font(30).render("PRINCIPAL", True, "#b68f40")
        menu_rect2 = menu_text2.get_rect(center=(ANCHO_VENTANA-250, 140))

        PLAY_BUTTON = Button(image=None, pos=(ANCHO_VENTANA-250, 240), 
                            text_input="JUGAR", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(ANCHO_VENTANA-250, 320), 
                            text_input="OPTIONES", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(ANCHO_VENTANA-250, 400), 
                            text_input="SALIR", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)
        SCREEN.blit(menu_text2, menu_rect2)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#INICIA EL MENU DEL JUEGO
main_menu()

# if(lista_teclas[pygame.K_SPACE] and lista_teclas[pygame.K_LEFT]):
#     player_1.control("JUMP_L")
# if(lista_teclas[pygame.K_SPACE] and lista_teclas[pygame.K_RIGHT]):
#     player_1.control("JUMP_R")

 # if event.type == pygame.KEYDOWN:
#     if event.key == pygame.K_LEFT:
#         player_1.control("WALK_L")
#     if event.key == pygame.K_RIGHT:
#         player_1.control("WALK_R")
#     if event.key == pygame.K_SPACE:
#         player_1.control("JUMP_R")

# if event.type == pygame.KEYUP:
#     if event.key == pygame.K_LEFT:
#         player_1.control("STAY_L")
#     if(event.key == pygame.K_RIGHT):
#         player_1.control("STAY_R")
#     if(event.key == pygame.K_SPACE):
#         player_1.control("STAY_R")

# if(lista_teclas[pygame.K_SPACE]):
#     if player_1.direccion == 1:
#         player_1.control("JUMP_SR")
#     else:
#         player_1.control("JUMP_SL")
#     if lista_teclas[pygame.K_LEFT]:
#         player_1.control("JUMP_L")
#     elif lista_teclas[pygame.K_RIGHT]:
#         player_1.control("JUMP_R")

# if (posicion == -ANCHO_VENTANA):
#     SCREEN.blit(fondo_juego.surface,(ANCHO_VENTANA + posicion,0))
#     posicion = 0
# posicion -= 1

# layer01 = Imagen(PATH_IMAGE + r"locations\forest\layer_01_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer02 = Imagen(PATH_IMAGE + r"locations\forest\layer_02_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer03 = Imagen(PATH_IMAGE + r"locations\forest\layer_03_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer04 = Imagen(PATH_IMAGE + r"locations\forest\layer_04_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer05 = Imagen(PATH_IMAGE + r"locations\forest\layer_05_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer06 = Imagen(PATH_IMAGE + r"locations\forest\layer_06_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer07 = Imagen(PATH_IMAGE + r"locations\forest\layer_07_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)

# SCREEN.blit(layer07.surface,layer07.rect)
# SCREEN.blit(layer06.surface,layer06.rect)
# SCREEN.blit(layer05.surface,layer05.rect)
# SCREEN.blit(layer04.surface,layer04.rect)
# SCREEN.blit(layer03.surface,layer03.rect)
# SCREEN.blit(layer02.surface,layer02.rect)
# SCREEN.blit(layer01.surface,layer01.rect)
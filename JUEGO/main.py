import pygame
import sys
import player
import enemigo
from imagenes import Imagen
from constantes import *
from auxiliar import Auxiliar
from botones import *

#SETEA LA VENTANA
SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

#CARGA IMAGENES
fondo_juego = Imagen(PATH_IMAGE + r"locations\mountain\all.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(PATH_IMAGE + r"menu\Background.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_seleccion = Imagen(PATH_IMAGE + r"menu\Background.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
bear = Imagen(PATH_IMAGE + r"caracters\black_bear\face.png",150,150,650,250)
bunny = Imagen(PATH_IMAGE + r"caracters\rabbit\face.png",150,150,500,250)
puppet = Imagen(PATH_IMAGE + r"caracters\puppet\face.png",150,150,500,400)
chicken = Imagen(PATH_IMAGE + r"caracters\chicken\face.png",150,150,650,400)
#cuadro_menu = Imagen(PATH_IMAGE + r"menu\rect.png",ANCHO_VENTANA-int(ANCHO_VENTANA/3),ALTO_VENTANA,0,0)

#CARGA UNA FUENTE
def get_font(tamaño):
    return pygame.font.Font(PATH_IMAGE + r"\menu\font.ttf", tamaño)

jugador = "ONE"

#CODIGO DEL JUEGO
def play(jugador):
    tiempo = pygame.time.get_ticks()

    #ASIGNACION DE CLASSES
    player_1 = Auxiliar.elegir_personaje(jugador)
    enemigo_1 = enemigo.Enemigo(1400,500,2,tiempo)
    muercielagos = enemigo.GrupoBatterflies(1)

    while True: # Bucle del juego
        delta_ms = clock.tick(FPS) # FPS
        PLAY_MOUSE_POS = pygame.mouse.get_pos() # Posicion del mouse
        
        lista_teclas = pygame.event.get()
        lista_precionada = pygame.key.get_pressed() # Teclas apretadas
        
        #CARGA FONDO
        SCREEN.blit(fondo_juego.surface,fondo_juego.rect)
        
        #ACTUALIZA JUEGO   
        player_1.actualizar_personaje(SCREEN,delta_ms,lista_teclas,lista_precionada,player_1.rect)
        enemigo_1.actualizar_enemigo(SCREEN,delta_ms,player_1.rect)

        #DIBUJA EL NIVEL
        muercielagos.updatear_murcielagos(SCREEN,player_1.rect)
        
        #ACTUALIZA PANTALLA
        pygame.display.flip()

def seleccion_personaje():
    while True:
        #SCREEN.blit(fondo_seleccion.surface, (0,0))
        SELECCION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(fondo_seleccion.surface,fondo_seleccion.rect)
        SCREEN.blit(bunny.surface,bunny.rect)
        SCREEN.blit(bear.surface,bear.rect)
        SCREEN.blit(puppet.surface,puppet.rect)
        SCREEN.blit(chicken.surface,chicken.rect)

        opcion_text = get_font(40).render("SELECCION DE PERSONAJES", True, "#b68f40")
        opcion_rect = opcion_text.get_rect(center=(int(ANCHO_VENTANA/2),int(ALTO_VENTANA/10)))
        SCREEN.blit(opcion_text, opcion_rect)

        OPTIONS_BACK = Button(image=None, pos=(ANCHO_VENTANA//2,ALTO_VENTANA-100), 
            text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="Green")
        BUNNY = Button(image=None, pos=(ANCHO_VENTANA//2-350,300), 
            text_input="BUNNY", font=get_font(40), base_color="#d7fcd4", hovering_color="Green")    
        BEAR = Button(image=None, pos=(ANCHO_VENTANA//2+300,300), 
            text_input="BEAR", font=get_font(40), base_color="#d7fcd4", hovering_color="Green")
        PUPPET = Button(image=None, pos=(ANCHO_VENTANA//2-350,450), 
            text_input="PUPPET", font=get_font(40), base_color="#d7fcd4", hovering_color="Green")
        CHICKEN = Button(image=None, pos=(ANCHO_VENTANA//2+320,450), 
            text_input="CHICKEN", font=get_font(40), base_color="#d7fcd4", hovering_color="Green")

        OPTIONS_BACK.changeColor(SELECCION_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        BEAR.changeColor(SELECCION_MOUSE_POS)
        BEAR.update(SCREEN)
        BUNNY.changeColor(SELECCION_MOUSE_POS)
        BUNNY.update(SCREEN)
        CHICKEN.changeColor(SELECCION_MOUSE_POS)
        CHICKEN.update(SCREEN)
        PUPPET.changeColor(SELECCION_MOUSE_POS)
        PUPPET.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUNNY.checkForInput(SELECCION_MOUSE_POS):
                    jugador = "ONE"
                    play(jugador)
                if BEAR.checkForInput(SELECCION_MOUSE_POS):
                    jugador = "TWO"
                    play(jugador)
                if PUPPET.checkForInput(SELECCION_MOUSE_POS):
                    jugador = "THREE"
                    play(jugador)
                if CHICKEN.checkForInput(SELECCION_MOUSE_POS):
                    jugador = "FOUR"
                    play(jugador)
                if OPTIONS_BACK.checkForInput(SELECCION_MOUSE_POS):
                    main_menu()

        pygame.display.flip()



#MENU OPCIONES        
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        opcion_text = get_font(45).render("MENU DE OPCIONES.", True, "Black")
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
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

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
                    seleccion_personaje()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU DEL JUEGO
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


# layer06 = Imagen(PATH_IMAGE + r"locations\forest\layer_06_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
# layer07 = Imagen(PATH_IMAGE + r"locations\forest\layer_07_1920 x 1080.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)

# SCREEN.blit(layer07.surface,layer07.rect)
# SCREEN.blit(layer06.surface,layer06.rect)
# SCREEN.blit(layer05.surface,layer05.rect)
# SCREEN.blit(layer04.surface,layer04.rect)
# SCREEN.blit(layer03.surface,layer03.rect)
# SCREEN.blit(layer02.surface,layer02.rect)
# SCREEN.blit(layer01.surface,layer01.rect)

# if lista_teclas[pygame.K_LSHIFT]: # Correr
        #     player_1.movement = player_1.speed_run
        # elif not lista_teclas[pygame.K_LSHIFT]:
        #     player_1.movement = player_1.speed_walk
import pygame
import sys
from pygame.locals import *
from settings import *
from auxiliar import *
from botones import Button
from imagenes import Imagen
from plataforma import Plataform, Plataform_back
from player import Player
from objets import *
from loot import Loot
from enemigo import *

flags = DOUBLEBUF

SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()
pygame.init()

fondo_juego = Imagen(PATH_IMAGE + r"Menu\Fondo\space_out.jpg",ANCHO_VENTANA+300,ALTO_VENTANA,0,0)
fondo_level = Imagen(PATH_IMAGE + r"Menu\Fondo\planets.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(PATH_IMAGE + r"Menu\Fondo\menu.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)

#CARGA UNA FUENTE
def get_font(tamaño):
    return pygame.font.Font(PATH_IMAGE + r"\Menu\Text\font.ttf", tamaño)

#JUEGO
def play(nivel):
    tiempo = pygame.time.get_ticks()
    player_1 = Player(x = 60, y = 40, speed_walk = 8, gravity = 15, jump_power = 15, frame_rate_ms = 40,frame_rate_jump_ms = 85, move_rate_ms = 20, jump_height = 180, p_scale=0.2,interval_time_jump=300)
    enemy_1 = Enemigo(x=1100,y=400,speed_walk=4,gravity=10,frame_rate_ms=20,move_rate_ms=20,pasos=800)
    enemy_2 = Enemigo(x=1100,y=190,speed_walk=4,gravity=10,frame_rate_ms=20,move_rate_ms=20,pasos=400)

    #PLATAFORMAS
    plataform_list = []
    wall_list = []
    lista_objetos = []
    lista_objetos_animados = []
    final_door = []
    switch_list = []
    x = 0
    y = 0
    for i in range(0,30):
        if i < 1:
            #OBJETOS
            lista_objetos_animados.append(Animated_Object(x=70,y=80,width=80,height=120,type_unlock=6,type_open=4,type_lock=5))
            final_door.append(Animated_Object(x=1050,y=430,width=80,height=120,type_unlock=6,type_open=4,type_lock=5))
            switch_list.append(Animated_Object(x=400,y=125,width=25,height=75,type_unlock=8,type_open=7,type_lock=8))
            lista_objetos.append(Static_Object(x=450,y=475,width=75,height=75,type_unlock=2))
            lista_objetos.append(Static_Object(x=525,y=475,width=75,height=75,type_unlock=2))
            lista_objetos.append(Static_Object(x=485,y=400,width=75,height=75,type_unlock=2))
        if i < 3:
            plataform_list.append(Plataform(x+50,y=200,width=50,height=50,type=1))
            plataform_list.append(Plataform(x+150,y=350,width=50,height=50,type=1))
            plataform_list.append(Plataform(x+350,y=200,width=50,height=50,type=1))
        if i < 6:
            plataform_list.append(Plataform(x+900,y=150,width=50,height=50,type=1))
        if i < 8:
            wall_list.append(Plataform_back(x=300,y=y,width=50,height=50,type=4))
        if i < 12:
            plataform_list.append(Plataform(x+600,y=300,width=50,height=50,type=1))
            #Cambia Y
            wall_list.append(Plataform_back(x=0,y=y,width=50,height=50,type=4))
            wall_list.append(Plataform_back(x=1150,y=y,width=50,height=50,type=4))
        if i < 23:
            plataform_list.append(Plataform(x,y=550,width=50,height=50,type=1))
            wall_list.append(Plataform_back(x,y=0,width=50,height=50,type=1,reverso = True))
        x += 50
        y += 50

    x = 0
    y = 0
    loot_list = []
    for i in range(10):
        if i < 5:
            loot_list.append(Loot(x+900,y=50,frame_rate_ms=60))
        loot_list.append(Loot(x+650,y=200,frame_rate_ms=60))
        x += 50
    for i in range(5):
        loot_list.append(Loot(x=230,y=y+50,frame_rate_ms=60))
        y += 50
    
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill("white")

        lista_pressed = pygame.key.get_pressed()
        lista_keys = pygame.event.get()

        delta_ms = clock.tick(FPS)
        
        SCREEN.blit(fondo_juego.surface,fondo_juego.rect)

        for plataforma in plataform_list:
            plataforma.draw(SCREEN)
        for objeto2 in lista_objetos_animados:
            objeto2.draw(SCREEN)
        for objeto in lista_objetos:
            objeto.draw(SCREEN)
        for wall in wall_list:
            wall.draw(SCREEN)
        for loot in loot_list:
            loot.update(delta_ms)
            loot.draw(SCREEN)
        for switch in switch_list:
            switch.draw(SCREEN)
        for door in final_door:
            door.draw(SCREEN)
        

        player_1.events(delta_ms,lista_pressed)
        player_1.update(delta_ms,plataform_list,lista_objetos,lista_objetos_animados,wall_list,loot_list,switch_list,final_door)
        player_1.draw(SCREEN)
        enemy_1.update(delta_ms,plataform_list)
        enemy_1.draw(SCREEN)
        enemy_2.update(delta_ms,plataform_list)
        enemy_2.draw(SCREEN)


        pygame.display.flip()

#SELECCION DE NIVEL
def selec_level():
    nivel_one = pygame.image.load(PATH_IMAGE + r"Menu\Levels\01.png")
    nivel_two = pygame.image.load(PATH_IMAGE + r"Menu\Levels\02.png")
    nivel_three = pygame.image.load(PATH_IMAGE + r"Menu\Levels\03.png")
    nivel_four = pygame.image.load(PATH_IMAGE + r"Menu\Levels\04.png")
    nivel_five = pygame.image.load(PATH_IMAGE + r"Menu\Levels\05.png")
    nivel_six = pygame.image.load(PATH_IMAGE + r"Menu\Levels\06.png")
    nivel_seven = pygame.image.load(PATH_IMAGE + r"Menu\Levels\07.png")
    nivel_eight = pygame.image.load(PATH_IMAGE + r"Menu\Levels\08.png")

    while True:
        SCREEN.blit(fondo_level.surface, (0,0))
        #SCREEN.blit(cuadro_menu.surface, (ANCHO_VENTANA-500,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        NIVEL_1 = Button(image=nivel_one, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.28)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_2 = Button(image=nivel_two, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.28)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_3 = Button(image=nivel_three, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.28)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_4 = Button(image=nivel_four, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.28)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_5 = Button(image=nivel_five, pos=(ANCHO_VENTANA * 0.15, int(ALTO_VENTANA * 0.70)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_6 = Button(image=nivel_six, pos=(ANCHO_VENTANA * 0.38, int(ALTO_VENTANA * 0.70)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_7 = Button(image=nivel_seven, pos=(ANCHO_VENTANA * 0.62, int(ALTO_VENTANA * 0.70)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        NIVEL_8 = Button(image=nivel_eight, pos=(ANCHO_VENTANA * 0.85, int(ALTO_VENTANA * 0.70)), 
            text_input="", font=get_font(55), base_color=CYAN, hovering_color="White")

        QUIT = Button(image=None, pos=(ANCHO_VENTANA // 2, int(ALTO_VENTANA * 0.9)), 
        text_input="QUIT", font=get_font(30), base_color=CYAN, hovering_color="White")


        for button in [NIVEL_1, NIVEL_2, NIVEL_3, NIVEL_4, NIVEL_5, NIVEL_6, NIVEL_7, NIVEL_8, QUIT]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NIVEL_1.checkForInput(MENU_MOUSE_POS):
                    play("1")
                if NIVEL_2.checkForInput(MENU_MOUSE_POS):
                    play("2")
                if NIVEL_3.checkForInput(MENU_MOUSE_POS):
                    play("3")
                if NIVEL_4.checkForInput(MENU_MOUSE_POS):
                    play("4")
                if NIVEL_5.checkForInput(MENU_MOUSE_POS):
                    play("5")
                if NIVEL_6.checkForInput(MENU_MOUSE_POS):
                    play("6")
                if NIVEL_7.checkForInput(MENU_MOUSE_POS):
                    play("7")
                if NIVEL_8.checkForInput(MENU_MOUSE_POS):
                    play("8")
                if QUIT.checkForInput(MENU_MOUSE_POS):
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

        menu_text = get_font(50).render("SPACE ADVENTURE", True, GOLDEN)
        menu_rect = menu_text.get_rect(center=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.2)))

        PLAY_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.4)), 
            text_input="JUGAR", font=get_font(40), base_color=CYAN, hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.55)), 
            text_input="OPTIONES", font=get_font(40), base_color=CYAN, hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.7)), 
            text_input="SALIR", font=get_font(40), base_color=CYAN, hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    selec_level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU DEL JUEGO
main_menu()
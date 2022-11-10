import pygame
import sys
from pygame.locals import *
from constantes import *
from player import Player
from plataforma import Plataform,Plataform2
from imagenes import Imagen
from auxiliar import *
from botones import Button
from nivel import Nivel
from enemigo import Enemigo

flags = DOUBLEBUF

SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

#CARGA IMAGENES
#PARADAX PRUEBA


#fondo_juego = Imagen(PATH_IMAGE + r"locations\set_bg_05\1_game_background\1_game_background.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_menu = Imagen(PATH_IMAGE + r"menu\Background.png",ANCHO_VENTANA,ALTO_VENTANA,0,0)
fondo_seleccion = Imagen(PATH_IMAGE + r"menu\screen_selection.jpg",ANCHO_VENTANA,ALTO_VENTANA,0,0)
bonnie = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters\players\Glitch\rabbit\idleSleepy.png",21,2)[0]
teddy = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters\players\Glitch\black_bear\idleSleepy.png",21,2)[0]
puppet= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters\players\Glitch\puppet\idleSleepy.png",21,2)[0]
foxxie = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters\players\Glitch\fox\idleSleepy.png",21,2)[0]

#CARGA UNA FUENTE
def get_font(tamaño):
    return pygame.font.Font(PATH_IMAGE + r"\menu\font.ttf", tamaño)

#JUEGO
def play(jugador):
    tiempo = pygame.time.get_ticks()

    #ASIGNACION DE CLASSES
    player_1 = Auxiliar.elegir_personaje(jugador)
    enemigo_1 = Enemigo(1100,100,4,8,20,5)
    nivel_1 = Nivel()
    nivel_1.crear_paradax(PATH_IMAGE + r"locations\set_bg_05\1_game_background\layers\\",7)

    #PLATAFORMAS
    plataform_list = []
    plataform_list.append(Plataform(x=350,y=400,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=400,y=400,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=450,y=400,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=500,y=400,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=550,y=400,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=600,y=400,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=650,y=400,width=50,height=50,type=1))  
    plataform_list.append(Plataform(x=700,y=400,width=50,height=50,type=1))

    plataform_list.append(Plataform(x=750,y=250,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=800,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=850,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=900,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=950,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=1000,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=1050,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=1100,y=250,width=50,height=50,type=1))

    plataform_list.append(Plataform(x=150,y=100,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=200,y=100,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=250,y=100,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=300,y=100,width=50,height=50,type=2))

    plataform_list.append(Plataform(x=300,y=250,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=350,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=400,y=250,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=450,y=250,width=50,height=50,type=1)) 
    plataform_list.append(Plataform(x=500,y=250,width=50,height=50,type=2))

    plataform_list.append(Plataform(x=650,y=100,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=700,y=100,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=750,y=100,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=800,y=100,width=50,height=50,type=1)) 
    plataform_list.append(Plataform(x=850,y=100,width=50,height=50,type=2))

    #PLATAFORMA 2
    plataform_list2 = []
    x = 0

    for i in range(0,24):
        plataform_list2.append(Plataform2(x,y=500,width=50,height=50,type=0))
        x += 50
    x = 0

    for i in range(0,24):
        plataform_list2.append(Plataform2(x,y=550,width=50,height=50,type=1))
        x += 50


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        delta_ms = clock.tick(FPS)
        
        # nivel_1.events(keys,player_1.speed_walk)
        nivel_1.draw_bg(SCREEN,10)
        #SCREEN.blit(fondo_juego.surface,fondo_juego.rect)

        for plataforma in plataform_list:
            plataforma.draw(SCREEN)

        player_1.events(delta_ms,keys)
        player_1.update(delta_ms,plataform_list)
        player_1.draw(SCREEN)

        for plataforma in plataform_list2:
            plataforma.draw(SCREEN)
            
        enemigo_1.update(delta_ms,plataform_list)
        enemigo_1.draw(SCREEN)
        enemigo_1.colicion(player_1.rect)
        
        # enemigos update
        # player dibujarlo
        # dibujar todo el nivel

        pygame.display.flip()

#SELECCION DE PERSONAJE
def seleccion_personaje():
    while True:
        #SCREEN.blit(fondo_seleccion.surface, (0,0))
        SELECCION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(fondo_seleccion.surface,fondo_seleccion.rect)

        opcion_text = get_font(int(ANCHO_VENTANA * 0.025)).render("SELECCION DE PERSONAJES", True, "#b68f40")
        opcion_rect = opcion_text.get_rect(center=(ANCHO_VENTANA//2,int(ALTO_VENTANA * 0.070)))
        bonnie_text = get_font(int(ANCHO_VENTANA * 0.025)).render("BONNIE", True, "#b68f40")
        teddy_text = get_font(int(ANCHO_VENTANA * 0.025)).render("TEDDY", True, "#b68f40")
        puppet_text = get_font(int(ANCHO_VENTANA * 0.025)).render("PUPPET", True, "#b68f40")
        foxxie_text = get_font(int(ANCHO_VENTANA * 0.025)).render("FOXXIE", True, "#b68f40")
        
        SCREEN.blit(opcion_text, opcion_rect)
        SCREEN.blit(bonnie_text, (int(ANCHO_VENTANA * 0.125) - ANCHO_VENTANA * 0.065,int(ALTO_VENTANA * 0.8)))
        SCREEN.blit(teddy_text, (int(ANCHO_VENTANA * 0.375) - ANCHO_VENTANA * 0.065,int(ALTO_VENTANA * 0.8)))
        SCREEN.blit(puppet_text, (int(ANCHO_VENTANA * 0.625) - ANCHO_VENTANA * 0.065,int(ALTO_VENTANA * 0.8)))
        SCREEN.blit(foxxie_text, (int(ANCHO_VENTANA * 0.875) - ANCHO_VENTANA * 0.065,int(ALTO_VENTANA * 0.8)))
        

        OPTIONS_BACK = Button(image=None, pos=(int(ANCHO_VENTANA * 0.125),int(ALTO_VENTANA * 0.94)), 
            text_input="BACK", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        BUNNY = Button(image=bonnie, pos=(int(ANCHO_VENTANA * 0.125),int(ALTO_VENTANA * 0.6)), 
            text_input="", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")    
        BEAR = Button(image=teddy, pos=(int(ANCHO_VENTANA * 0.375),int(ALTO_VENTANA * 0.6)), 
            text_input="", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        PUPPET = Button(image=puppet, pos=(int(ANCHO_VENTANA * 0.625),int(ALTO_VENTANA * 0.6)), 
            text_input="", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        FOX = Button(image=foxxie, pos=(int(ANCHO_VENTANA * 0.875),int(ALTO_VENTANA * 0.6)), 
            text_input="", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")

        for button in [OPTIONS_BACK,BEAR,BUNNY,FOX,PUPPET]:
            button.changeColor(SELECCION_MOUSE_POS)
            button.update(SCREEN)
        
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
                if FOX.checkForInput(SELECCION_MOUSE_POS):
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

        menu_text = get_font(70).render("PYGAME", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.1)))

        PLAY_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.4)), 
            text_input="JUGAR", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.6)), 
            text_input="OPTIONES", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(ANCHO_VENTANA//2, int(ALTO_VENTANA * 0.8)), 
            text_input="SALIR", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

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
                    seleccion_personaje()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

#MENU DEL JUEGO
main_menu()


# bear = Imagen(PATH_IMAGE + r"caracters\players\Glitch\black_bear\face.png",150,150,650,250)
# bunny = Imagen(PATH_IMAGE + r"caracters\players\Glitch\rabbit\face.png",150,150,500,250)
# puppet = Imagen(PATH_IMAGE + r"caracters\players\Glitch\puppet\face.png",150,150,500,400)
# fox = Imagen(PATH_IMAGE + r"caracters\players\Glitch\fox\face.png",150,150,650,400)
# bear = pygame.image.load(PATH_IMAGE + r"caracters\players\Glitch\black_bear\face.png")
# bunny = pygame.image.load(PATH_IMAGE + r"caracters\players\Glitch\rabbit\face.png")
# puppet = pygame.image.load(PATH_IMAGE + r"caracters\players\Glitch\puppet\face.png")
# fox = pygame.image.load(PATH_IMAGE + r"caracters\players\Glitch\fox\face.png")

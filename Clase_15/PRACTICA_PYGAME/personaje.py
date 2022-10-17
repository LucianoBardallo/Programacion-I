import pygame
import colores

def crear_personaje(x,y,ancho,largo):
    dic_personaje = {}
    dic_personaje["surface"] = pygame.image.load(r"Clase_15\PRACTICA_PYGAME\01.png")
    dic_personaje["surface"] = pygame.transform.scale(dic_personaje["surface"],(ancho,largo))
    dic_personaje["rect_pos"] = pygame.Rect(x,y,50,50)
    dic_personaje["rect"] = pygame.Rect(x+50,y+100,150,50)
    dic_personaje["distancia"] = 0
    return dic_personaje

def actualizar_pantalla(player,pantalla):
    #pygame.draw.rect(pantalla,colores.ROJO,player["rect"])
    pantalla.blit(player["surface"],player["rect_pos"])

def update(player,incremento_y):
    nueva_y = player["rect_pos"].y + incremento_y
    if (nueva_y > 50 and nueva_y < 450):
        player["rect_pos"].y = player["rect_pos"].y + incremento_y
        player["rect"].y = player["rect"].y + incremento_y

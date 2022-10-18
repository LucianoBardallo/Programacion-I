import pygame
import colores
import random
import personaje

def crear_obstaculo(x,y,ancho,alto):
    dict_obstaculo = {}
    dict_obstaculo["surface"] = pygame.image.load(r"Clase_15\CLASE_PYGAME_INTRO\04.png")
    dict_obstaculo["surface"] = pygame.transform.scale(dict_obstaculo["surface"],(ancho,alto))
    dict_obstaculo["rect"] = dict_obstaculo["surface"].get_rect()
    dict_obstaculo["rect"].x = x
    dict_obstaculo["rect"].y = y
    dict_obstaculo["visible"] = True
    dict_obstaculo["speed"] = random.randrange (10,20,1)
    return dict_obstaculo

def update(lista_obstaculos):
    for obstaculo in lista_obstaculos:
        rect_obstaculo = obstaculo["rect"]
        rect_obstaculo.y = rect_obstaculo.y + obstaculo["speed"]

def actualizar_pantalla(lista_obstaculos,player,pantalla,sonido):
    for obstaculo in lista_obstaculos:
        #pygame.draw.rect(pantalla,colores.ROJO,pila["rect"])
        pantalla.blit(obstaculo["surface"],obstaculo["rect"])
        if player["rect"].colliderect(obstaculo["rect"]):
            player["vida"] -= 1
            player["surface"] = pygame.image.load(r"Clase_15\CLASE_PYGAME_INTRO\05.png")
            player["surface"] = pygame.transform.scale(player["surface"],(200,200))
            sonido.play()
            restart(obstaculo)  
        if obstaculo["rect"].y > 880:
            restart(obstaculo)
        
        font = pygame.font.SysFont("Arial Narrow", 50)
        text = font.render("VIDAS: {0}".format(player["vida"]), True, colores.NEGRO)
        pantalla.blit(text,(0,40))

def crear_lista_obstaculos(cantidad):
    lista_obstaculos = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_obstaculos.append(crear_obstaculo(x,y,60,60))
    return lista_obstaculos

def restart(obstaculo):
    obstaculo["rect"].x = random.randrange (0,740,60)
    obstaculo["rect"].y = random.randrange (-1000,0,60)
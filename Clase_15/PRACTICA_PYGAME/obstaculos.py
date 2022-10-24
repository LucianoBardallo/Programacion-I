import pygame
import colores
import random

def crear_obstaculo(path,x,y,ancho,alto):
    dict_obstaculo = {}
    dict_obstaculo["surface"] = pygame.image.load(path)
    dict_obstaculo["surface"] = pygame.transform.scale(dict_obstaculo["surface"],(ancho,alto))
    dict_obstaculo["rect"] = dict_obstaculo["surface"].get_rect()
    dict_obstaculo["rect"].x = x
    dict_obstaculo["rect"].y = y
    dict_obstaculo["visible"] = True
    return dict_obstaculo

def update(lista_obstaculos):
    for obstaculo in lista_obstaculos:
        rect_obstaculo = obstaculo["rect"]
        rect_obstaculo.x = rect_obstaculo.x - 1

def actualizar_pantalla(lista_obstaculos,player,pantalla,sonido):
    for obstaculo in lista_obstaculos:
        #pygame.draw.rect(pantalla,colores.ROJO,pila["rect"])
        pantalla.blit(obstaculo["surface"],obstaculo["rect"])
        if player["rect"].colliderect(obstaculo["rect"]):
            player["vida"] -= 25
            sonido.play()
            restart(obstaculo)  
        if obstaculo["rect"].x < 0:
            restart(obstaculo)

def actualizar_pantalla2(lista_piedras,player,pantalla,sonido):
    for piedra in lista_piedras:
        #pygame.draw.rect(pantalla,colores.ROJO,pila["rect"])
        pantalla.blit(piedra["surface"],piedra["rect"])
        if player["rect"].colliderect(piedra["rect"]):
            player["vida"] -= 100
            sonido.play()
            restart(piedra)  
        if piedra["rect"].x < 0:
            restart(piedra)

def crear_lista_obstaculos(cantidad):
    lista_obstaculos = []
    for i in range(cantidad):
        x = random.randrange(1200,3000,500)
        y = random.randrange(400,560,40)
        lista_obstaculos.append(crear_obstaculo(r"Clase_15\PRACTICA_PYGAME\00.png",x,y,40,40))
    return lista_obstaculos

def crear_lista_piedra(cantidad):
    lista_obstaculos = []
    for i in range(cantidad):
        x = random.randrange(1200,3000,500)
        y = random.randrange(400,560,40)
        lista_obstaculos.append(crear_obstaculo(r"Clase_15\PRACTICA_PYGAME\05.png",x,y,50,50))
    return lista_obstaculos

def restart(obstaculo):
    obstaculo["rect"].x = random.randrange(1200,3000,500)
    obstaculo["rect"].y = random.randrange(400,560,40)
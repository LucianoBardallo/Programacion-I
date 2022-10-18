import pygame
import colores
import random

def crear_pila(x,y,ancho,alto):
    dict_pila = {}
    dict_pila["surface"] = pygame.image.load(r"Clase_15\PRACTICA_PYGAME\02.png")
    dict_pila["surface"] = pygame.transform.scale(dict_pila["surface"],(ancho,alto))
    dict_pila["rect"] = dict_pila["surface"].get_rect()
    dict_pila["rect"].x = x
    dict_pila["rect"].y = y
    dict_pila["visible"] = True
    return dict_pila

def update(lista_pilas):
    for pila in lista_pilas:
        rect_pila = pila["rect"]
        rect_pila.x = rect_pila.x - 20

def actualizar_pantalla(lista_pilas,player,pantalla,sonido):
    for pila in lista_pilas:
        #pygame.draw.rect(pantalla,colores.ROJO,pila["rect"])
        pantalla.blit(pila["surface"],pila["rect"])
        if player["rect"].colliderect(pila["rect"]):
            if player["vida"] <= 90:
                player["vida"] += 10
                sonido.play()
            else:
                player["vida"] = 100
            restart(pila)
        if pila["rect"].x < 0:
            restart(pila)

def crear_lista_pila(cantidad):
    lista_pilas = []
    for i in range(cantidad):
        x = random.randrange(1200,3000,500)
        y = random.randrange(400,560,40)
        lista_pilas.append(crear_pila(x,y,40,40))
    return lista_pilas

def restart(pila):
    pila["rect"].x = random.randrange(1200,3000,500)
    pila["rect"].y = random.randrange(400,560,40)
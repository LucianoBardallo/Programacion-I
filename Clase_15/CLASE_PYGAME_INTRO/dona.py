import pygame
import colores
import random

def crear(path,x,y,ancho,alto):
    # Leer una imagen
    imagen_dona = pygame.image.load(path)
    imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rect_dona = imagen_dona.get_rect()
    rect_dona.x = x
    rect_dona.y = y
    dict_dona = {}
    dict_dona["surface"] = imagen_dona
    dict_dona["rect"] = rect_dona
    dict_dona["visible"] = True
    dict_dona["speed"] = random.randrange (10,20,1)
    return dict_dona

def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y = rect_dona.y + dona["speed"]


def actualizar_donas(lista_donas,personaje,ventana_ppal,sonido):
    for dona in lista_donas:
        if(personaje["rect"].colliderect(dona["rect"])):
            personaje["score"] = personaje["score"] + 100
            sonido.play()
            restar_dona(dona)
        if(dona["rect"].y > 880):
            restar_dona(dona)
        ventana_ppal.blit(dona["surface"],dona["rect"])

    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, colores.NEGRO)
    ventana_ppal.blit(text,(0,0))

def actualizar_cerveza(lista_cerveza,personaje,ventana_ppal,sonido):
    for cerveza in lista_cerveza:
        if(personaje["rect"].colliderect(cerveza["rect"])):
            if personaje["vida"] < 3:
                personaje["vida"] += 1
            personaje["surface"] = pygame.image.load(r"Clase_15\CLASE_PYGAME_INTRO\01.png")
            personaje["surface"] = pygame.transform.scale(personaje["surface"],(200,200))
            sonido.play()
            restar_dona(cerveza)
        if(cerveza["rect"].y > 880):
            restar_dona(cerveza)
        ventana_ppal.blit(cerveza["surface"],cerveza["rect"])

def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_donas.append(crear(r"Clase_15\CLASE_PYGAME_INTRO\00.png",x,y,60,60))
    return lista_donas

def crear_lista_cerveza(cantidad):
    lista_cerveza = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_cerveza.append(crear(r"Clase_15\CLASE_PYGAME_INTRO\06.png",x,y,60,60))
    return lista_cerveza

def restar_dona(dona):
    dona["rect"].x = random.randrange (0,740,60)
    dona["rect"].y = random.randrange (-1000,0,60)

import pygame
import tablero
from constantes import *

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

tick_1500ms = pygame.USEREVENT+1
pygame.time.set_timer(tick_1500ms,1500)

tablero.reproducir_musica_principal(r"Clase_17\recursos\fondo.wav",0.1)
tablero_juego = tablero.init()
tablero_fondo = tablero.crear_fondo(r"Clase_17\recursos\fondo.jpg",ALTO_PANTALLA,ANCHO_PANTALLA)
clock_fps = pygame.time.Clock()
running = True
while running:
    tiempo = clock_fps.tick(60)
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.colicion(tablero_juego,event.pos)
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == tick_1s:
            pass
        if event.type == tick_1500ms:
            pass
    tablero.update(tablero_juego)
    # Se pinta el fondo de la ventana de blanco
    pantalla_juego.blit(tablero_fondo["surface"], [0,0])
    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

'''
nueva_tarjeta = {}
nueva_tarjeta["visible"]=False
nueva_tarjeta["descubierto"]=False
nueva_tarjeta["path_imagen"] = PATH_RECURSOS+nombre_imagen
nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA,ALTO_TARJETA))
nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
nueva_tarjeta["rect"].x = x
nueva_tarjeta["rect"].y = y
return nueva_tarjeta
'''

# Se pinta el fondo de la ventana de blanco
    #pantalla_juego.fill((255, 255, 255))
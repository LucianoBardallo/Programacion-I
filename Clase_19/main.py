import pygame
import sys
from constantes import *
import player
import enemigo

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE + r"\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = player.Player(0,0,4,8,8,16)
enemigo_1 = enemigo.Enemigo(1000,500,2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.control("WALK_L")
            if event.key == pygame.K_RIGHT:
                player_1.control("WALK_R")
            if event.key == pygame.K_SPACE:
                player_1.control("JUMP_R")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_1.control("STAY")

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
   
    player_1.update()
    player_1.draw(screen)
    enemigo_1.update()
    enemigo_1.render(screen)
    enemigo_1.colicion(player_1.rect)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)



    







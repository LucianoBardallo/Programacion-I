import pygame

pygame.init()

running = True

window = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption("Vamos a hacer un juego en python!")
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
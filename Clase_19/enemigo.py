import pygame
from auxiliar import Auxiliar
from constantes import *

class Enemigo:
    def __init__(self,x,y,speed_walk):
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_idle1_part1_png_1354834034.png",17,16)
        self.walk = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_walk_png_1354834021.png",4,4,True)
        self.animation = self.walk
        self.frame = 0
        self.move_x = 2
        self.move_y = 0
        self.vida = 1
        self.speedwalk = speed_walk
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += -self.move_x

    def render(self,screen):
        if self.vida == 1:
            self.surface = self.animation[self.frame]
            screen.blit(self.surface,self.rect)

    def colicion(self,pos_xy):
        if self.rect.colliderect(pos_xy):
            self.vida = 0
    

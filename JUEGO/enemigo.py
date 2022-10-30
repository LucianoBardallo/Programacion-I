from turtle import Screen
import pygame
from auxiliar import Auxiliar
from constantes import *

class Enemigo:
    def __init__(self,x,y,speed_walk,tiempo):
        self_hp = 100
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_walk_png_1354834021.png",4,4,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_walk_png_1354834021.png",4,4)
        self.spawn = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_spawn_png_1354834019.png",4,6,True)
        self.muerte_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_shrink_png_1354834050.png",4,6)
        self.muerte_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_shrink_png_1354834050.png",4,6,True)
        self.swipe = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_swipe_png_1354834051.png",4,4)
        self.frame = 0
        self.vidas = 1
        self.move_x = 0
        self.move_y = 0
        self.move = 0
        self.speed_walk = speed_walk
        self.animation = self.spawn
        self.image = self.animation[self.frame]
        self.rect_pos = pygame.Rect(x+55,y+110,80,80) 
        self.rect = pygame.Rect(x,y,50,50)
        self.tiempo = 0
        self.tiempospawn = tiempo
        self.setspawn = 1
    
    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        if(tiempo_actual - self.tiempo > 2000 and self.tiempo > 0):
            self.vidas = 0
            self.tiempo = 0
        if(tiempo_actual - self.tiempospawn > 2000 and self.tiempospawn > 0):
            self.setspawn = 0
            self.tiempospawn = 0

        if(self.frame < len(self.animation) - 1):
            self.frame += 1
        elif(self.animation != self.muerte_r and self.animation != self.muerte_l
            and self.animation != self.spawn): 
            self.frame = 0

        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pos.x += self.move_x
        self.rect_pos.y += self.move_y

        if self.vidas == 1 and self.tiempo == 0 and self.setspawn == 0:
            if(self.move <= 300):
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.move += 1
            elif(self.move <= 600):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.move += 1
            else:
                self.move = 0
        
    def draw(self,screen):
        #pygame.draw.rect(screen,(255,0,0),self.rect_pos)
        if self.vidas == 1:
            self.image = self.animation[self.frame // 4]
            screen.blit(self.image,self.rect)

            
    def colicion(self,pos_xy):
        if self.rect_pos.colliderect(pos_xy):
            if self.vidas == 1 and self.tiempo == 0:
                self.move_x = 0
                self.move_y = 0
                self.tiempo = pygame.time.get_ticks()
                self.animation = self.muerte_r
                if self.move <= 300:
                    self.animation = self.muerte_l
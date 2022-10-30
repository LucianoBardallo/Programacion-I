import pygame
import math
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/walk.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/idle.png",16,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("Clase_19/images/caracters/stink/jump.png",33,1,True)
        self.frame = 0
        self.vidas = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = "right"
        self.is_jump = False
        self.distancia = 0
        self.animation_anterior = self.stay_r
        

    def control(self,action):
        if(action == "WALK_R"):
            self.move_x = self.speed_walk
            if self.rect.y == 500:
                self.animation = self.walk_r
            else:
                self.animation = self.jump_r

        elif(action == "WALK_L"):
            self.move_x = -self.speed_walk
            if self.rect.y == 500:
                self.animation = self.walk_l
            else:
                self.animation = self.jump_l

        elif(action == "STAY"):
            if self.rect.y == 500:
                self.animation = self.stay_r
                if self.direccion == "left":
                    self.animation = self.stay_l
                self.move_x = 0
            else:
                self.animation = self.jump_r
                if self.direccion == "left":
                    self.animation = self.jump_l

        elif(action == "JUMP"):
            self.is_jump = True
            self.animation = self.jump_r
            if self.direccion == "left":
                self.animation = self.jump_l

        if self.animation != self.animation_anterior:
            self.animation_anterior = self.animation
            self.frame = 0

        
    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        if self.is_jump:
            if self.jump >= -10:
                self.rect.y -= (self.jump * abs(self.jump)) * 0.5
                self.jump -= 0.5
            else:
                self.jump = 10
                self.is_jump = False

        self.rect.x += self.move_x
        
        if(self.rect.y < 500):
            self.rect.y += self.gravity
        elif (self.rect.y >= 500):
            self.rect.y = 500


    def draw(self,screen):
        #pygame.draw.rect(screen,(255,0,0),self.rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


    def colicion(self,pos_xy):
        if self.rect.colliderect(pos_xy):
            pass



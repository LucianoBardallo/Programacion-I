import pygame
from settings import *
from auxiliar import Auxiliar

class Bullet:
    def __init__(self,x,y,frame_rate_ms,direction):
        self.direction = direction

        self.shooting = {}
        self.shooting[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Objects/Bullet_{0}.png",5,False,w=25,h=25)
        self.shooting[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Objects/Bullet_{0}.png",5,True,w=25,h=25)

        self.impact = {}
        self.impact[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Objects/Muzzle_{0}.png",5,False,w=25,h=25)
        self.impact[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Objects/Muzzle_{0}.png",5,True,w=25,h=25)

        self.animation = self.shooting[self.direction]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y+self.rect.height/3,self.rect.width/3,self.rect.height/3)
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.tiempo_trayectoria = 0
        self.is_impact = False
        self.speed = 8
        self.move_x = 0

        self.speed_walk = {}
        self.speed_walk[RIGHT] = self.speed
        self.speed_walk[LEFT] = -self.speed

    def movement(self):
        self.speed = -8
        if self.direction == RIGHT:
            self.speed = 8
        self.rect.x += self.speed
        self.collition_rect.x += self.speed
        self.tiempo_trayectoria = pygame.time.get_ticks()

    def draw(self,screen):
        if self.is_impact == False:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def frame_update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms):
        self.movement()
        self.frame_update(delta_ms)
    


        
    
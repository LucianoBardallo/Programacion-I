import pygame
from auxiliar import *
from settings import *

class Loot:
    def __init__(self,x,y,frame_rate_ms):

        self.staying = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Items\Fruits\Apple.png",columnas=17,filas=1,scale=2)
        self.collected = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "Items\Fruits\Collected.png",columnas=6,filas=1,scale=2)
        self.animation = self.staying
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y+self.rect.height/3,self.rect.width/3,self.rect.height/3)
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.is_collected = False
        

    def draw(self,screen):
        if self.is_collected == False:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
            
        



            
    
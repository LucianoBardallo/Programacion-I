import pygame
from settings import *
from auxiliar import Auxiliar

class Object:
    def __init__(self, x, y,width, height, type=1,reverso = False):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "TileSet\space_ship\Objects\Object ({0}).png",9,flip=False,w=width,h=height,reverse=reverso)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)

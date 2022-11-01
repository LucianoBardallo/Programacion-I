import random
import pygame
from auxiliar import Auxiliar
from constantes import *

class Enemigo:
    def __init__(self,x,y,speed_walk,tiempo):
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_walk_png_1354834021.png",4,4,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_walk_png_1354834021.png",4,4)
        self.spawn = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_spawn_png_1354834019.png",4,6,True)
        self.muerte_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_shrink_png_1354834050.png",4,6)
        self.muerte_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_shrink_png_1354834050.png",4,6,True)
        self.swipe = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"assets\npc_juju_bandit_bandana_black_variant_green\npc_juju_bandit_bandana_black_variant_green_x1_swipe_png_1354834051.png",4,4)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.move = 0
        self.tiempo = 0
        self.vidas = 1
        self.setspawn = 1
        self.pasos = 1000
        self.tiempospawn = tiempo
        self.speed_walk = speed_walk
        self.animation = self.spawn
        self.image = self.animation[self.frame]
        self.rect_pos = pygame.Rect(x+55,y+110,80,80) 
        self.rect = pygame.Rect(x,y,50,50)
        
        
    def update(self):
        #EVENTOS QUE PASAN POR TIEMPO
        tiempo_actual = pygame.time.get_ticks()
        if(tiempo_actual - self.tiempo > 300 and self.tiempo > 0):
            self.vidas = 0
            self.tiempo = 0
        if(tiempo_actual - self.tiempospawn > 300 and self.tiempospawn > 0):
            self.setspawn = 0
            self.tiempospawn = 0

        #CARGA DE FRAMES
        if(self.frame < len(self.animation) - 1):
            self.frame += 1
        else: 
            self.frame = 0
    
        #MOVIMIENTO DE PIXELES
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pos.x += self.move_x
        self.rect_pos.y += self.move_y

        #MOVIMIENTO DE ENEMIGO
        if self.vidas == 1 and self.tiempo == 0 and self.setspawn == 0:
            if(self.move <= self.pasos):
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.move += 1
            elif(self.move <= self.pasos*2):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.move += 1
            else:
                self.move = 0
        

    def draw(self,screen):
        #pygame.draw.rect(screen,(255,0,0),self.rect_pos)
        #pygame.draw.rect(screen,(255,0,0),self.rect)
        if self.vidas == 1:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)


    def colicion(self,pos_xy):
        if self.rect_pos.colliderect(pos_xy):
            if self.vidas == 1 and self.tiempo == 0:
                self.move_x = 0
                self.move_y = 0
                self.tiempo = pygame.time.get_ticks()
                self.animation = self.muerte_r
                if self.move <= 1000:
                    self.animation = self.muerte_l


class Batterfly:
    def __init__(self, x, y, speed_x, speed_y, invertido, maximo_x, maximo_y) -> None:

        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"inhabitants\butterfly\fly.png",12,3, invertido)

        self.frame = 0
        self.move_x = speed_x
        self.move_y = speed_y
        self.animation = self.fly

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pos = pygame.Rect(x+20,y+10, 75, 70)
        self.down = False

        self.maximo_x = maximo_x
        self.maximo_y = y - maximo_y
        self.minimo_y = y

    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        self.rect.x += self.move_x
        self.rect_pos.x += self.move_x
        self.controlar_vuelo()
    
    def controlar_vuelo(self):
        if self.rect.y < self.minimo_y and self.down == True:
            self.rect.y += self.move_y
            self.rect_pos.y += self.move_y
        
        else:
            self.down = False
            if self.rect.y > self.maximo_y:
                self.rect.y -= self.move_y
                self.rect_pos.y -= self.move_y
            else:
                self.down = True

    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


class GrupoBatterflies:
    def __init__(self, cantidad) -> None:
        self.lista_murcielagos = []
        self.agregar_murcielagos(cantidad)
        self.cantidad = cantidad
        
    def agregar_murcielagos(self, cantidad):
        for i in range(cantidad):
            invertido = random.randrange(0,2)
            y = random.randrange(100, 380, 20)
            movimiento_x = random.randrange(5, 10)
            movimiento_y = random.randrange(5, 10)
            maximo_y = random.randrange(100,200,10)
            if invertido == 1:
                invertido = False
                x = random.randrange(-ANCHO_VENTANA/2, 0, 20)
                limite_x = ANCHO_VENTANA + 100
            else:
                invertido = True
                movimiento_x *= -1
                x = random.randrange(ANCHO_VENTANA, ANCHO_VENTANA + ANCHO_VENTANA/2, 20)
                limite_x = -100
            
            batterfly = Batterfly(x, y , movimiento_x, movimiento_y, invertido, limite_x, maximo_y)
            self.lista_murcielagos.append(batterfly)

    def updatear_murcielagos(self,screen, rect_player):

        if len(self.lista_murcielagos) < self.cantidad:
            self.agregar_murcielagos(1)

        for murcielago in self.lista_murcielagos:
            murcielago.update()
            murcielago.draw(screen)
            
            if murcielago.rect_pos.colliderect(rect_player):
                self.lista_murcielagos.remove(murcielago)

            if murcielago.move_x > 0:
                if murcielago.rect.x > murcielago.maximo_x:
                    self.lista_murcielagos.remove(murcielago)

            elif murcielago.rect.x < murcielago.maximo_x:
                self.lista_murcielagos.remove(murcielago)
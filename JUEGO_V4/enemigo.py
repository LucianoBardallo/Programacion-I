import pygame
from auxiliar import Auxiliar
from settings import *

class Enemigo:
    def __init__(self,x,y,speed_walk,gravity,frame_rate_ms,move_rate_ms,pasos):
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"Characters\enemies\set_juju\black\juju_idle2.png",37,9,True,scale=0.8)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"Characters\enemies\set_juju\black\juju_idle2.png",37,9,scale=0.8)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,scale=0.8)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,True,scale=0.8)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.move = 0
        self.gravity = gravity
        self.vidas = 1
        self.pasos = pasos
        self.speed_walk = speed_walk
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/2,self.rect.height-20)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms

        
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y


    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.change_y(self.gravity)  

        #MOVIMIENTO DE ENEMIGO
        if self.vidas == 1:
            if(self.move <= self.pasos):
                self.move_x = -self.speed_walk
                self.animation = self.walk_r
                self.move += 1
            elif(self.move <= self.pasos*2):
                self.move_x = self.speed_walk
                self.animation = self.walk_l
                self.move += 1
            else:
                self.move = 0
        

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno   


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0


    def update(self,delta_ms,plataformas):
        self.do_movement(delta_ms,plataformas)
        self.do_animation(delta_ms)

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)

        if self.vidas == 1:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)


    def colicion(self,pos_xy):
        if self.rect.colliderect(pos_xy):
            self.move_x = 0
            self.move_y = 0
            self.vidas = 0




# class Batterfly:
#     def __init__(self, x, y, speed_x, speed_y, invertido, maximo_x, maximo_y) -> None:

#         self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"inhabitants\butterfly\fly.png",12,3, invertido)

#         self.frame = 0
#         self.move_x = speed_x
#         self.move_y = speed_y
#         self.animation = self.fly

#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.rect_pos = pygame.Rect(x+20,y+10, 75, 70)
#         self.down = False

#         self.maximo_x = maximo_x
#         self.maximo_y = y - maximo_y
#         self.minimo_y = y

#     def update(self):
#         if(self.frame < len(self.animation) - 1):
#             self.frame += 1 
#         else: 
#             self.frame = 0

#         self.rect.x += self.move_x
#         self.rect_pos.x += self.move_x
#         self.controlar_vuelo()
    
#     def controlar_vuelo(self):
#         if self.rect.y < self.minimo_y and self.down == True:
#             self.rect.y += self.move_y
#             self.rect_pos.y += self.move_y
        
#         else:
#             self.down = False
#             if self.rect.y > self.maximo_y:
#                 self.rect.y -= self.move_y
#                 self.rect_pos.y -= self.move_y
#             else:
#                 self.down = True

#     def draw(self,screen):
#         #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
#         self.image = self.animation[self.frame]
#         screen.blit(self.image,self.rect)

# class GrupoBatterflies:
    # def __init__(self, cantidad) -> None:
    #     self.lista_murcielagos = []
    #     self.agregar_murcielagos(cantidad)
    #     self.cantidad = cantidad
        
    # def agregar_murcielagos(self, cantidad):
    #     for i in range(cantidad):
    #         invertido = random.randrange(0,2)
    #         y = random.randrange(100, 380, 20)
    #         movimiento_x = random.randrange(5, 10)
    #         movimiento_y = random.randrange(5, 10)
    #         maximo_y = random.randrange(100,200,10)
    #         if invertido == 1:
    #             invertido = False
    #             x = random.randrange(-ANCHO_VENTANA/2, 0, 20)
    #             limite_x = ANCHO_VENTANA + 100
    #         else:
    #             invertido = True
    #             movimiento_x *= -1
    #             x = random.randrange(ANCHO_VENTANA, ANCHO_VENTANA + ANCHO_VENTANA/2, 20)
    #             limite_x = -100
            
    #         batterfly = Batterfly(x, y , movimiento_x, movimiento_y, invertido, limite_x, maximo_y)
    #         self.lista_murcielagos.append(batterfly)

    # def updatear_murcielagos(self,screen, rect_player):

    #     if len(self.lista_murcielagos) < self.cantidad:
    #         self.agregar_murcielagos(1)

    #     for murcielago in self.lista_murcielagos:
    #         murcielago.update()
    #         murcielago.draw(screen)
            
    #         if murcielago.rect_pos.colliderect(rect_player):
    #             self.lista_murcielagos.remove(murcielago)

    #         if murcielago.move_x > 0:
    #             if murcielago.rect.x > murcielago.maximo_x:
    #                 self.lista_murcielagos.remove(murcielago)

    #         elif murcielago.rect.x < murcielago.maximo_x:
    #             self.lista_murcielagos.remove(murcielago)
import pygame
import math
import sys
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/base.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/idle3.png",25,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/jump.png",33,1,True) 
        self.actual_animation = "stay_r"
        self.vidas = 5
        self.frame = 0
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.movement = speed_walk
        self.gravity = gravity
        self.jump_time = jump_power
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.animation_anterior = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = DIRECTION_R
        self.is_jump = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        
        
    def walk(self,direction):
        self.frame_refresh()
        self.direction = direction
        if(direction == DIRECTION_R):
            self.move_x = self.speed_walk
            if not self.is_jump:
                self.actual_animation = "walk_r"
            else:
                self.actual_animation = "jump_r"
        else:
            self.move_x = -self.speed_walk
            if not self.is_jump:
                self.actual_animation = "walk_l"
            else:
                self.actual_animation = "jump_l"

    def stay(self):
        self.frame_refresh()
        if not self.is_jump:
            if(self.direction == DIRECTION_R):
                self.actual_animation = "stay_r"
            else:
                self.actual_animation = "stay_l"
        self.move_x = 0
        self.move_y = 0

    def jump(self):
        self.frame_refresh()
        self.is_jump = True
        if self.direction == DIRECTION_R:
            self.actual_animation = "jump_r"
        else:
            self.actual_animation = "jump_l"

    def do_movement(self,delta_ms):
        # Salto
        if self.is_jump:
            if self.jump_time >= -self.jump_power:
                self.rect.y -= (self.jump_time * abs(self.jump_time)) * 0.5
                self.jump_time -= self.jump_power // 10
            else:
                self.jump_time = self.jump_power
                self.is_jump = False

        # Movimiento de x
        self.rect.x += self.move_x
        
        # Gravedad
        if(self.rect.y < 555):
            self.rect.y += self.gravity
        elif (self.rect.y >= 555):
            self.rect.y = 555

    def do_animation(self,delta_ms):
        # Tiempo de animaciones
        if self.animation == self.jump_r or self.animation == self.jump_l:
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
        else:
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0

        # Animaciones
        if self.is_jump:
            if self.actual_animation == "jump_r":
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l
        else:
            if self.actual_animation == "walk_r":
                self.animation = self.walk_r
            elif self.actual_animation == "stay_r":
                self.animation = self.stay_r
            elif self.actual_animation == "walk_l":
                self.animation = self.walk_l
            elif self.actual_animation == "stay_l":
                self.animation = self.stay_l
                
    def frame_refresh(self):
        if self.animation != self.animation_anterior:
            self.animation_anterior = self.animation
            self.frame = 0

    def update(self,delta_ms):
        self.do_animation(delta_ms)
        self.do_movement(delta_ms)


    def draw(self,screen):
        #pygame.draw.rect(screen,(255,0,0),self.rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def colicion(self,pos_xy):
        if self.rect.colliderect(pos_xy):
            pass

    def events(self,delta_ms,lista_teclas,lista_precionada):
        for event in lista_teclas:
            if event.type == pygame.QUIT: # Salir
                pygame.quit()
                sys.exit() 
                
            if event.type == pygame.KEYDOWN: # Apretar alguna tecla
                if event.key == pygame.K_SPACE: # Saltar
                    self.jump()

            if event.type == pygame.KEYUP: # Dejar de apretar alguna tecla
                if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT: # Quedarse quieto
                    self.stay()
                
        if(lista_precionada[pygame.K_RIGHT] and not lista_precionada[pygame.K_LEFT]): # Mover a la derecha
            self.direction = DIRECTION_R
            self.walk(self.direction)
            
        elif(lista_precionada[pygame.K_LEFT] and not lista_precionada[pygame.K_RIGHT]): # Mover a la izquierda
            self.direction = DIRECTION_L
            self.walk(self.direction)
        else:
            self.stay() #Quedarse quieto

    def actualizar_personaje(self,screen,delta_ms,teclas,presionada,pos_xy):
        self.draw(screen)
        self.update(delta_ms)
        self.events(delta_ms,teclas,presionada)
        self.colicion(pos_xy)

class PlayerONE(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms):
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/base.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/idle3.png",25,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/rabbit/jump.png",33,1,True) 

class PlayerTWO(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/base.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/idle3.png",25,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/black_bear/jump.png",33,1,True)

class PlayerTHREE(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/base.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/idle3.png",25,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/puppet/jump.png",33,1,True)
       
class PlayerFOUR(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/base.png",15,1,True)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/idle3.png",25,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/chicken/jump.png",33,1,True)
        




# def control(self,action):
#         if(action == "WALK_R"):
#             self.speed_walk = 4
#             self.move_x = self.speed_walk
#             if self.rect.y == 550:
#                 self.animation = self.walk_r
#             else:
#                 self.animation = self.jump_r

#         elif(action == "WALK_L"):
#             self.speed_walk = 4
#             self.move_x = -self.speed_walk
#             if self.rect.y == 550:
#                 self.animation = self.walk_l
#             else:
#                 self.animation = self.jump_l
        
#         if(action == "RUN_R"):
#             self.speed_walk = self.speed_run
#             self.move_x = self.speed_walk
#             if self.rect.y == 550:
#                 self.animation = self.walk_r
#             else:
#                 self.animation = self.jump_r

#         elif(action == "RUN_L"):
#             self.speed_walk = self.speed_run
#             self.move_x = -self.speed_walk
#             if self.rect.y == 550:
#                 self.animation = self.walk_l
#             else:
#                 self.animation = self.jump_l

#         elif(action == "STAY"):
#             if self.rect.y == 550:
#                 self.animation = self.stay_r
#                 if self.direction == DIRECTION_L:
#                     self.animation = self.stay_l
#                 self.move_x = 0
#             else:
#                 self.animation = self.jump_r
#                 if self.direction == DIRECTION_L:
#                     self.animation = self.jump_l

#         elif(action == "JUMP"):
#             self.is_jump = True
#             self.animation = self.jump_r
#             if self.direction == DIRECTION_L:
#                 self.animation = self.jump_l

#         if self.animation != self.animation_anterior:
#             self.animation_anterior = self.animation
#             self.frame = 0
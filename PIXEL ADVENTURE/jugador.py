import pygame
from settings import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        
        self.stay_r = {Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Idle ({0}).png",10,False,w=100,h=100)}
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Idle ({0}).png",10,True,w=100,h=100)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Run ({0}).png",8,False,w=100,h=100)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Run ({0}).png",8,True,w=100,h=100)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Jump ({0}).png",10,False,w=100,h=100)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Jump ({0}).png",10,True,w=100,h=100)
        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Dead ({0}).png",10,False,w=100,h=100)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Dead ({0}).png",10,True,w=100,h=100)
        self.run_shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/RunShoot ({0}).png",9,False,w=100,h=100)
        self.run_shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/RunShoot ({0}).png",9,True,w=100,h=100)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Shoot ({0}).png",4,False,w=100,h=100)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Shoot ({0}).png",4,True,w=100,h=100)
        self.melee_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Melee ({0}).png",8,False,w=100,h=100)
        self.melee_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Melee ({0}).png",8,True,w=100,h=100)
        self.jump_shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpMelee ({0}).png",8,False,w=100,h=100)
        self.jump_shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpMelee ({0}).png",8,True,w=100,h=100)
        self.jump_melee_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpShoot ({0}).png",5,False,w=100,h=100)
        self.jump_melee_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpShoot ({0}).png",5,True,w=100,h=100)

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x=(x+self.rect.width/3),y=(y+20),ancho=(self.rect.width/3),alto=(self.rect.height-20))

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_melee = False
        self.is_walk = False
        self.is_run_shoot = False
        self.is_jump_shoot = False
        self.is_jump_melee = False
        self.is_wall = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def walk(self,direction,on_off=False):
        if(on_off and not self.is_jump and not self.is_fall and not self.is_run and not self.is_shoot and not self.is_melee):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                self.frame = 0
                self.is_walk = True      

        if(on_off == False):
            self.is_walk = False
            

    def walk_shoot(self,on_off):
        if(on_off and not self.is_jump and not self.is_fall and not self.is_walk and not self.is_shoot and not self.is_melee):
            if((self.animation != self.walk_r and self.animation != self.walk_l)):
                if(self.direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.run_shoot_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.run_shoot_l
                self.frame = 0
                self.is_run = True
        if(on_off == False):
            self.is_walk = False
                

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def jump_shoot(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_shoot_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_shoot_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
    
    def jump_melee(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_melee_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_melee_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_melee or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off and not self.is_jump and not self.is_fall and not self.is_walk):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def melee(self,on_off = True):
        self.is_melee = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.melee_r and self.animation != self.melee_l and self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.melee_r
                else:
                    self.animation = self.melee_l      

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list,object_list,wall_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_colition(wall_list)):
                self.is_walk = True
                self.is_wall = False
            else:
                self.is_wall = True  

            if(not self.is_on_plataform(plataform_list,object_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False       

    def is_colition(self,wall_list):
        for wall in wall_list:
            if(self.collition_rect.colliderect(wall.collition_rect)):
                if self.direction == DIRECTION_R:
                    self.change_x(-3)
                else:
                    self.change_x(3)
                    
                

    def is_on_plataform(self,plataform_list,object_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break
            for objecto in object_list:
                if(self.ground_collition_rect.colliderect(objecto.ground_collition_rect)):
                    retorno = True
                    break              
        return retorno 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.is_jump:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animation = 0
                if self.is_fall:
                    if(self.frame >= 7 and self.frame < 9 - 1):
                        self.frame += 1
                    else:
                        self.frame = 7
                else:
                    if(self.frame < len(self.animation) - 4):
                        self.frame += 1 
                    else: 
                        self.frame = 0    
        else:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0

    def do_collition(self,delta_ms,loot_list):
        for loot in loot_list:
            if loot.collition_rect.colliderect(self.collition_rect):
                loot.is_collected = True
 
    def update(self,delta_ms,plataform_list,object_list,wall_list,loot_list):
        self.do_movement(delta_ms,plataform_list,object_list,wall_list)
        self.do_animation(delta_ms)
        self.do_collition(delta_ms,loot_list)
        
    
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
    

    def events(self,delta_ms,pressed,keydown,keyup):
        self.tiempo_transcurrido += delta_ms

        if(keydown)

        if(pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]):
            self.walk(DIRECTION_L,True)

        if(not pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]):
            self.walk(DIRECTION_R,True)

        if(not pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT] and not pressed[pygame.K_SPACE] and not self.is_jump and not self.is_fall):
            self.stay()

        if(pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT] and not pressed[pygame.K_SPACE]):
            self.stay()  

        if(pressed[pygame.K_SPACE] and not pressed[pygame.K_a] and not pressed[pygame.K_s]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido 
        
        if(not pressed[pygame.K_s]):
            self.shoot(False)  

        if(not pressed[pygame.K_a]):
            self.melee(False)  

        if(pressed[pygame.K_s] and not pressed[pygame.K_a] and not pressed[pygame.K_LEFT] and  not pressed[pygame.K_RIGHT]):
            self.shoot()   
        
        if(pressed[pygame.K_a] and not pressed[pygame.K_s] and not pressed[pygame.K_LEFT] and  not pressed[pygame.K_RIGHT]):
            self.melee()  
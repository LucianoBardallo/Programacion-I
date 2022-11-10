import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/climb.png",19,1)
        self.happy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/happy.png",21,1)
        self.happy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/happy.png",21,1,True)
        self.angry_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/angry.png",20,1)
        self.angry_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/angry.png",20,1,True)
        self.surprise_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/surprise.png",21,1)
        self.surprise_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/surprise.png",21,1,True)
        self.sleepy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idleSleepy.png",21,2)
        self.sleepy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idleSleepy.png",21,2,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idle3.png",25,2,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/base.png",15,1,True)[:12]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/jump.png",33,1,True)

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
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

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

    def stay(self):
        if(self.is_knife or self.is_shoot):
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
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      



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

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

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
                #print(self.frame)
            else: 
                self.frame = 0
 
    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
            
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido 
        
        if(not keys[pygame.K_a]):
            self.shoot(False)  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.shoot()   
        
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.knife()  

class PlayerONE(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100):
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100)
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/climb.png",19,1)
        self.happy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/happy.png",21,1)
        self.happy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/happy.png",21,1,True)
        self.angry_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/angry.png",20,1)
        self.angry_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/angry.png",20,1,True)
        self.surprise_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/surprise.png",21,1)
        self.surprise_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/surprise.png",21,1,True)
        self.sleepy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idleSleepy.png",21,2)
        self.sleepy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idleSleepy.png",21,2,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/idle3.png",25,2,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/base.png",15,1,True)[:12]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/rabbit/jump.png",33,1,True)
class PlayerTWO(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100)
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/climb.png",19,1)
        self.happy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/happy.png",21,1)
        self.happy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/happy.png",21,1,True)
        self.angry_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/angry.png",20,1)
        self.angry_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/angry.png",20,1,True)
        self.surprise_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/surprise.png",21,1)
        self.surprise_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/surprise.png",21,1,True)
        self.sleepy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/idleSleepy.png",21,2)
        self.sleepy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/idleSleepy.png",21,2,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/idle3.png",25,2,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/base.png",15,1,True)[:12]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/black_bear/jump.png",33,1,True)
class PlayerTHREE(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100)
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/climb.png",19,1)
        self.happy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/happy.png",21,1)
        self.happy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/happy.png",21,1,True)
        self.angry_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/angry.png",20,1)
        self.angry_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/angry.png",20,1,True)
        self.surprise_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/surprise.png",21,1)
        self.surprise_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/surprise.png",21,1,True)
        self.sleepy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/idleSleepy.png",21,2)
        self.sleepy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/idleSleepy.png",21,2,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/idle3.png",25,2,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/base.png",15,1,True)[:12]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/puppet/jump.png",33,1,True)      
class PlayerFOUR(Player):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        super().__init__(x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100)
        self.climb = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/climb.png",19,1)
        self.happy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/happy.png",21,1)
        self.happy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/happy.png",21,1,True)
        self.angry_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/angry.png",20,1)
        self.angry_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/angry.png",20,1,True)
        self.surprise_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/surprise.png",21,1)
        self.surprise_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/surprise.png",21,1,True)
        self.sleepy_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/idleSleepy.png",21,2)
        self.sleepy_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/idleSleepy.png",21,2,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/idle3.png",25,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/idle3.png",25,2,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/base.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/base.png",15,1,True)[:12]
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/jump.png",33,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"caracters/players/Glitch/fox/jump.png",33,1,True)








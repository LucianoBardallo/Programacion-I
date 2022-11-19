import pygame
from settings import *
from auxiliar import Auxiliar
from bullets import Bullet
import sys

class Player:
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        
        self.staying = {}
        self.staying[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Idle ({0}).png",10,False,w=100,h=100)
        self.staying[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Idle ({0}).png",10,True,w=100,h=100)

        self.walking = {}
        self.walking[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Run ({0}).png",8,False,w=100,h=100)
        self.walking[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Run ({0}).png",8,True,w=100,h=100)
        
        self.jumping = {}
        self.jumping[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Jump ({0}).png",5,False,w=100,h=100)
        self.jumping[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Jump ({0}).png",5,True,w=100,h=100)

        self.falling = {}
        self.falling[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Fall ({0}).png",5,False,w=100,h=100)
        self.falling[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Fall ({0}).png",5,True,w=100,h=100)

        self.dead = {}
        self.dead[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Dead ({0}).png",10,False,w=100,h=100)
        self.dead[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Dead ({0}).png",10,True,w=100,h=100)

        self.running_shoot = {}
        self.running_shoot[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/RunShoot ({0}).png",9,False,w=100,h=100)
        self.running_shoot[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/RunShoot ({0}).png",9,True,w=100,h=100)

        self.shooting = {}
        self.shooting[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Shoot ({0}).png",4,False,w=100,h=100)
        self.shooting[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Shoot ({0}).png",4,True,w=100,h=100)

        self.atacking = {}
        self.atacking[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Melee ({0}).png",8,False,w=100,h=100)
        self.atacking[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Melee ({0}).png",8,True,w=100,h=100)

        self.jumping_shoot = {}
        self.jumping_shoot[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpMelee ({0}).png",8,False,w=100,h=100)
        self.jumping_shoot[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpMelee ({0}).png",8,True,w=100,h=100)

        self.jumping_melee = {}
        self.jumping_melee[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpShoot ({0}).png",5,False,w=100,h=100)
        self.jumping_melee[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/JumpShoot ({0}).png",5,True,w=100,h=100)

        self.slide = {}
        self.slide[RIGHT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Slide ({0}).png",10,False,w=100,h=100)
        self.slide[LEFT] = Auxiliar.getSurfaceFromSeparateFiles(PATH_IMAGE + "Characters/robot/Slide ({0}).png",10,True,w=100,h=100)

        self.speed_walk = {}
        self.speed_walk[RIGHT] = speed_walk
        self.speed_walk[LEFT] = -speed_walk

        self.lives = 1
        self.vidas = 5
        self.score = 0
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.gravity = gravity
        self.jump_power = jump_power
        self.direction = RIGHT
        self.animation = self.staying[self.direction]
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/3,self.rect.height-20)

        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.head_collition_rect = pygame.Rect(self.collition_rect)
        self.head_collition_rect.height = GROUND_COLLIDE_H
        self.head_collition_rect.y = y + GROUND_COLLIDE_H

        self.right_collition_rect = pygame.Rect(self.collition_rect)
        self.right_collition_rect.width = GROUND_COLLIDE_H
        self.right_collition_rect.x = x + self.rect.width - GROUND_COLLIDE_H * 3

        self.left_collition_rect = pygame.Rect(self.collition_rect)
        self.left_collition_rect.width = GROUND_COLLIDE_H
        self.left_collition_rect.x = x + GROUND_COLLIDE_H * 2

        self.gun_rect = pygame.Rect(self.collition_rect)
        self.gun_rect.height = GROUND_COLLIDE_H
        self.gun_rect.width = GROUND_COLLIDE_H
        self.gun_rect.x = x + 75
        self.gun_rect.y = y + 50
    
        self.is_jumping = False
        self.is_falling = False
        self.is_walking = False
        self.is_shooting = False
        self.is_melee = False
        self.can_win = False
        self.inmune = False

        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.move_rate_ms = move_rate_ms
        self.start_jump = self.ground_collition_rect.y
        self.jump_height = jump_height
        self.tiempo_activate = 0
        self.tiempo_recolected = 0
        self.tiempo_loot = 0

        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_disparo = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_inmune = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.bullet_list = []
        self.shoot_cooldown = 0
        self.ammo = 30


    def walk(self,direccion):
        self.direction = direccion
        self.move_x = self.speed_walk[self.direction]
        self.is_walking = True
        if self.is_jumping:
            self.move_x = self.speed_walk[self.direction] // 2
         
    def stay(self):
        self.is_walking = False
        self.move_x = 0

    def jump(self, jump=True):
        if jump:
            if self.sobre_plataforma:
                self.is_jumping = True
                self.move_x = 0
                self.move_y = -self.jump_power
                self.start_jump = self.ground_collition_rect.y
        else:
            self.is_jumping = False

    def shoot(self,shoot=True):
        if shoot:
            self.is_shooting = True
            if self.shoot_cooldown == 0 and self.ammo > 0:
                self.shoot_cooldown = 40
                bullet = Bullet(self.gun_rect.x,self.gun_rect.y,frame_rate_ms=20,direction=self.direction)
                self.bullet_list.append(bullet)
                self.ammo -= 1
        else:
            self.is_shooting = False
    
    def melee(self,melee=True):
        self.is_melee = melee
        if melee:
            self.is_melee = True
        
            
    def jump_limit(self):
        if self.ground_collition_rect.y < self.start_jump - 150:
            self.is_jumping = False


    def on_platform(self, plataform_list, object_list):
        if not self.is_jumping:
            self.sobre_plataforma = False
            for plataform in plataform_list:
                if self.ground_collition_rect.colliderect(plataform.ground_collition_rect):
                    self.sobre_plataforma = True
                    break
            for object in object_list:
                if(self.ground_collition_rect.colliderect(object.ground_collition_rect)):
                    self.sobre_plataforma = True
                    break 
            

    def apply_gravity(self):
        if not self.is_jumping:
            if not self.sobre_plataforma:
                self.move_y = self.gravity
                self.is_falling = True
            else:
                self.move_y = 0
                self.is_falling = False

      
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.head_collition_rect.x += delta_x
        self.right_collition_rect.x += delta_x
        self.left_collition_rect.x += delta_x
        self.gun_rect.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.head_collition_rect.y += delta_y
        self.right_collition_rect.y += delta_y
        self.left_collition_rect.y += delta_y
        self.gun_rect.y += delta_y



    def do_movement(self,delta_ms,plataform_list,object_list,wall_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
          
            self.on_platform(plataform_list,object_list)
            self.apply_gravity()
            self.jump_limit()
            self.change_x(self.move_x)
            self.change_y(self.move_y)


    def do_animation(self,delta_ms):
        self.animations()
        self.updatear_frames(delta_ms)


    def animations(self):
        if self.is_jumping:
            self.change_animation(self.jumping)
        elif(self.is_falling):
            self.change_animation(self.falling)
        elif(self.is_walking):
            self.change_animation(self.walking)
        elif(self.is_shooting):
            self.change_animation(self.shooting)
        elif(self.is_melee):
            self.change_animation(self.atacking)
        else:
            self.change_animation(self.staying)


    def change_animation(self, animation):
        if self.animation != animation[RIGHT] and self.animation != animation[LEFT]:
            self.frame = 0
        self.animation = animation[self.direction]


    def updatear_frames(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.is_jumping:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
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

    def update_inmune(self, delta_ms):
        if self.inmune:
            self.tiempo_inmune += delta_ms
            if self.tiempo_inmune > 1500:
                self.tiempo_inmune = 0
                self.inmune = False

    def do_collition(self,delta_ms,loot_list,object_list,switch_list,final_door,wall_list,enemies):
        for wall in wall_list:
            if wall.collition_rect.colliderect(self.right_collition_rect):
                self.change_x(-2)
            elif wall.collition_rect.colliderect(self.left_collition_rect):
                self.change_x(2)
            elif wall.collition_rect.colliderect(self.head_collition_rect):
                self.start_jump = ALTO_VENTANA
            for bullet in self.bullet_list:
                if bullet.collition_rect.colliderect(wall.collition_rect):
                    self.bullet_list.remove(bullet)

        for enemy in enemies:
            if enemy.collition_rect.colliderect(self.collition_rect):
                if not self.inmune:
                    self.vidas -= 1
                    self.inmune = True

        for loot in loot_list:
            if loot.collition_rect.colliderect(self.collition_rect):
                loot.is_collected = True
                self.score += 50
                loot_list.remove(loot)
                    
        for object in object_list:
            if object.collition_rect.colliderect(self.collition_rect):
                object.activate = True
            else:
                object.activate = False

        for switch in switch_list:
            if switch.collition_rect.colliderect(self.collition_rect):
                switch.activate = True
                switch.unlock = True
                self.can_win = True
            else:
                self.tiempo_activate += delta_ms
                if(self.tiempo_activate >= 10000):
                    switch.activate = False
                    switch.unlock = False
                    self.can_win = False
                    self.tiempo_activate = 0

        for door in final_door:
            door.unlock = self.can_win
            if door.collition_rect.colliderect(self.collition_rect):
                door.activate = True
            else:
                door.activate = False
    
    def bullet_update(self,delta_ms,screen):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        for bullet in self.bullet_list:
            bullet.update(delta_ms)
            bullet.draw(screen)
            if bullet.is_impact:
                self.bullet_list.remove(bullet)

    def update(self,delta_ms,plataform,objects,animated_objects,walls,loots,switchs,final_door,enemies):
        self.do_movement(delta_ms,plataform,objects,walls)
        self.do_animation(delta_ms)
        self.do_collition(delta_ms,loots,animated_objects,switchs,final_door,walls,enemies)
        self.update_inmune(delta_ms)

    def draw(self,screen):
        if self.vidas > 0:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.head_collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.right_collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.left_collition_rect)
                pygame.draw.rect(screen,color=(255,255,255),rect=self.gun_rect)
            
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def events(self,delta_ms,keys,lista_eventos):
        self.tiempo_transcurrido += delta_ms

        for event in lista_eventos:
            if event.type == pygame.QUIT: # Salir
                pygame.quit()
                sys.exit() 
                    
            if event.type == pygame.KEYDOWN: # Apretar alguna tecla
                if event.key == pygame.K_SPACE: # Saltar
                    self.jump()
            
                if event.key == pygame.K_s: # Saltar
                    self.shoot()

                if event.key == pygame.K_a: # Saltar
                    self.melee()

            if event.type == pygame.KEYUP: # Dejar de apretar alguna tecla
                if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT and event.key == pygame.K_SPACE: # Quedarse quieto
                    self.stay()
            
                if event.key == pygame.K_SPACE: # Saltar
                    self.jump(False)
                
                if event.key == pygame.K_s: # Saltar
                    self.shoot(False)
                
                if event.key == pygame.K_a: # Saltar
                    self.melee(False)


                
        
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(LEFT)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(RIGHT)

        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  
        
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
                  
        if(keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.melee()

        if(not keys[pygame.K_a]):
            self.melee(False) 

        # if(keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
        #     self.shoot()

        # if(not keys[pygame.K_s]):
        #     self.shoot(False)
        
        
    



   # def walk(self,direction,on_off=False):
    #     if(on_off and not self.is_jump and not self.is_fall):
    #         if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
    #             self.direction = direction
    #             if(direction == RIGHT):
    #                 self.move_x = self.speed_walk
    #                 self.animation = self.walk_r
    #             else:
    #                 self.move_x = -self.speed_walk
    #                 self.animation = self.walk_l
    #             self.frame = 0
    #             self.is_walk = True      

    #     if(on_off == False):
    #         self.is_walk = False
            
    # def jump(self,on_off = True):
    #     if(on_off and self.is_jump == False and self.is_fall == False):
    #         self.y_start_jump = self.rect.y
    #         if(self.direction == RIGHT):
    #             self.move_x = int(self.move_x / 2)
    #             self.move_y = -self.jump_power
    #             self.animation = self.jump_r
    #         else:
    #             self.move_x = int(self.move_x / 2)
    #             self.move_y = -self.jump_power
    #             self.animation = self.jump_l
    #         self.frame = 0
    #         self.is_jump = True
    #     if(on_off == False):
    #         self.is_jump = False
    #         self.stay()

    # def stay(self):
    #     if(self.is_melee or self.is_shoot):
    #         return

    #     if(self.animation != self.stay_r and self.animation != self.stay_l):
    #         if(self.direction == RIGHT):
    #             self.animation = self.stay_r
    #         else:
    #             self.animation = self.stay_l
    #         self.move_x = 0
    #         self.move_y = 0
    #         self.frame = 0

    # def shoot(self,on_off = True):
    #     self.is_shoot = on_off
    #     if(on_off and not self.is_jump and not self.is_fall):
    #         if(self.animation != self.shoot_r and self.animation != self.shoot_l):
    #             self.frame = 0
    #             self.is_shoot = True
    #             if(self.direction == RIGHT):
    #                 self.animation = self.shoot_r
    #             else:
    #                 self.animation = self.shoot_l       

    # def melee(self,on_off = True):
    #     self.is_melee = on_off
    #     if(on_off == True and self.is_jump == False and self.is_fall == False):
    #         if(self.animation != self.melee_r and self.animation != self.melee_l and self.animation != self.walk_r and self.animation != self.walk_l):
    #             self.frame = 0
    #             if(self.direction == RIGHT):
    #                 self.animation = self.melee_r
    #             else:
    #                 self.animation = self.melee_l 





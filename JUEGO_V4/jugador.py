import pygame
from configuraciones import *
from auxiliar import Auxiliar
from balas import Bala
import sys

class Jugador:
    def __init__(self,x,y,velocidad_movimiento,gravedad,fuerza_salto,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,altura_salto,p_scale=1,interval_time_jump=100) -> None:
        
        self.parado = {}
        self.parado[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Idle ({0}).png",10,False,w=100,h=100)
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Idle ({0}).png",10,True,w=100,h=100)

        self.caminando = {}
        self.caminando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Run ({0}).png",8,False,w=100,h=100)
        self.caminando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Run ({0}).png",8,True,w=100,h=100)
        
        self.saltando = {}
        self.saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Jump ({0}).png",5,False,w=100,h=100)
        self.saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Jump ({0}).png",5,True,w=100,h=100)

        self.cayendo = {}
        self.cayendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Fall ({0}).png",5,False,w=100,h=100)
        self.cayendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Fall ({0}).png",5,True,w=100,h=100)

        self.muriendo = {}
        self.muriendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Dead ({0}).png",10,False,w=100,h=100)
        self.muriendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Dead ({0}).png",10,True,w=100,h=100)

        self.disparar_corriendo = {}
        self.disparar_corriendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/RunShoot ({0}).png",9,False,w=100,h=100)
        self.disparar_corriendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/RunShoot ({0}).png",9,True,w=100,h=100)

        self.disparando = {}
        self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Shoot ({0}).png",4,False,w=100,h=100)
        self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Shoot ({0}).png",4,True,w=100,h=100)

        self.atacando = {}
        self.atacando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Melee ({0}).png",8,False,w=100,h=100)
        self.atacando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Melee ({0}).png",8,True,w=100,h=100)

        self.disparar_saltando = {}
        self.disparar_saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpMelee ({0}).png",8,False,w=100,h=100)
        self.disparar_saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpMelee ({0}).png",8,True,w=100,h=100)

        self.atacar_saltando = {}
        self.atacar_saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpShoot ({0}).png",5,False,w=100,h=100)
        self.atacar_saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpShoot ({0}).png",5,True,w=100,h=100)

        self.deslizarse = {}
        self.deslizarse[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,False,w=100,h=100)
        self.deslizarse[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,True,w=100,h=100)

        self.velocidad_movimiento = {}
        self.velocidad_movimiento[DERECHA] = velocidad_movimiento
        self.velocidad_movimiento[IZQUIERDA] = -velocidad_movimiento

        self.lives = 1
        self.vidas = 5
        self.puntuacion = 0
        
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.gravedad = gravedad
        self.fuerza_salto = fuerza_salto
        self.direccion = DERECHA
        self.animacion = self.parado[self.direccion]
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/3,self.rect.height-20)

        self.rectangulo_pies = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_pies.height = ALTURA_PIES
        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES

        self.rectangulo_cabeza = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_cabeza.height = ALTURA_PIES
        self.rectangulo_cabeza.y = y + ALTURA_PIES

        self.rectangulo_derecha = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_derecha.width = ALTURA_PIES
        self.rectangulo_derecha.x = x + self.rect.width - ALTURA_PIES * 3

        self.rectangulo_izquierda = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_izquierda.width = ALTURA_PIES
        self.rectangulo_izquierda.x = x + ALTURA_PIES * 2
    
        self.esta_saltando = False
        self.esta_cayendo = False
        self.esta_caminando = False
        self.esta_disparando = False
        self.esta_pegando = False
        self.puede_ganar = False
        self.invensible = False

        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.move_rate_ms = move_rate_ms
        self.comienzo_salto = self.rectangulo_pies.y
        self.jump_height = altura_salto
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

        self.municiones = []
        self.disparo_cooldown = 0
        self.municion = 30


    def caminar(self,direccion):
        self.direccion = direccion
        self.mover_x = self.velocidad_movimiento[self.direccion]
        self.esta_caminando = True
        if self.esta_saltando:
            self.mover_x = self.velocidad_movimiento[self.direccion] // 2
         
    def parar(self):
        self.esta_caminando = False
        self.mover_x = 0

    def saltar(self, jump=True):
        if jump:
            if self.sobre_plataforma:
                self.esta_saltando = True
                self.mover_x = 0
                self.mover_y = -self.fuerza_salto
                self.comienzo_salto = self.rectangulo_pies.y
        else:
            self.esta_saltando = False

    def disparar(self,shoot=True,lista_ammo=[]):
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0 and self.municion > 0:
                self.disparo_cooldown = 40
                bullet = Bala(self.rectangulo_colision.centerx + (0.6 * self.rectangulo_colision.size[0] * self.direccion),self.rectangulo_colision.centery-20,frame_rate_ms=20,direccion=self.direccion)
                self.municiones.append(bullet)
                self.municion -= 1
                lista_ammo.remove(lista_ammo[-1])
        else:
            self.esta_disparando = False
    
    def atacar(self,melee=True):
        self.esta_pegando = melee
        if melee:
            self.esta_pegando = True
        
            
    def limitar_salto(self):
        if self.rectangulo_pies.y < self.comienzo_salto - 150:
            self.esta_saltando = False


    def verificar_plataforma(self, plataform_list, object_list):
        if not self.esta_saltando:
            self.sobre_plataforma = False
            for plataform in plataform_list:
                if self.rectangulo_pies.colliderect(plataform.rectangulo_pies):
                    self.sobre_plataforma = True
                    break
            for object in object_list:
                if(self.rectangulo_pies.colliderect(object.rectangulo_pies)):
                    self.sobre_plataforma = True
                    break 
            

    def aplicar_gravedad(self):
        if not self.esta_saltando:
            if not self.sobre_plataforma:
                self.mover_y = self.gravedad
                self.esta_cayendo = True
            else:
                self.mover_y = 0
                self.esta_cayendo = False

      
    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_cabeza.x += delta_x
        self.rectangulo_derecha.x += delta_x
        self.rectangulo_izquierda.x += delta_x


    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_cabeza.y += delta_y
        self.rectangulo_derecha.y += delta_y
        self.rectangulo_izquierda.y += delta_y



    def hacer_movimiento(self,delta_ms,plataformas,objetos):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
          
            self.verificar_plataforma(plataformas,objetos)
            self.aplicar_gravedad()
            self.limitar_salto()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)


    def hacer_animaciones(self,delta_ms):
        self.animaciones()
        self.actualizar_frames(delta_ms)


    def animaciones(self):
        if self.esta_saltando:
            self.cambiar_animacion(self.saltando)
        elif(self.esta_cayendo):
            self.cambiar_animacion(self.cayendo)
        elif(self.esta_caminando):
            self.cambiar_animacion(self.caminando)
        elif(self.esta_disparando):
            self.cambiar_animacion(self.disparando)
        elif(self.esta_pegando):
            self.cambiar_animacion(self.atacando)
        else:
            self.cambiar_animacion(self.parado)


    def cambiar_animacion(self, animation):
        if self.animacion != animation[DERECHA] and self.animacion != animation[IZQUIERDA]:
            self.frame = 0
        self.animacion = animation[self.direccion]


    def actualizar_frames(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.esta_saltando:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0          
        else:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0

    def actualizar_invensible(self, delta_ms):
        if self.invensible:
            self.tiempo_inmune += delta_ms
            if self.tiempo_inmune > 1500:
                self.tiempo_inmune = 0
                self.invensible = False

    def hacer_colisiones(self,delta_ms,botínes,objetos,interruptores,puerta_final,muros,enemigos,corazones):
        for muro in muros:
            if muro.rectangulo_colision.colliderect(self.rectangulo_derecha):
                self.cambiar_x(-2)
            elif muro.rectangulo_colision.colliderect(self.rectangulo_izquierda):
                self.cambiar_x(2)
            elif muro.rectangulo_colision.colliderect(self.rectangulo_cabeza):
                self.comienzo_salto = ALTO_VENTANA
            for bala in self.municiones:
                if bala.rectangulo_colision.colliderect(muro.rectangulo_colision):
                    self.municiones.remove(bala)

        for enemigo in enemigos:
            if enemigo.rectangulo_colision.colliderect(self.rectangulo_colision):
                if not self.invensible:
                    self.vidas -= 1
                    self.invensible = True
                    if self.vidas > 0:
                        corazones.remove(corazones[-1])

        for botín in botínes:
            if botín.rectangulo_colision.colliderect(self.rectangulo_colision):
                botín.recolectado = True
                self.puntuacion += 50
                botínes.remove(botín)
                    
        for objeto in objetos:
            if objeto.rectangulo_colision.colliderect(self.rectangulo_colision):
                objeto.activado = True
            else:
                objeto.activado = False

        for interruptor in interruptores:
            if interruptor.rectangulo_colision.colliderect(self.rectangulo_colision):
                interruptor.activado = True
                interruptor.unlock = True
                self.puede_ganar = True
            else:
                self.tiempo_activate += delta_ms
                if(self.tiempo_activate >= 10000):
                    interruptor.activado = False
                    interruptor.unlock = False
                    self.puede_ganar = False
                    self.tiempo_activate = 0

        for puerta in puerta_final:
            puerta.unlock = self.puede_ganar
            if puerta.rectangulo_colision.colliderect(self.rectangulo_colision):
                puerta.activado = True
            else:
                puerta.activado = False
    
    def actualizar_bala(self,delta_ms,pantalla):
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.actualizar(delta_ms)
            bala.renderizar(pantalla)
            if bala.impacto:
                self.municiones.remove(bala)
                

    def actualizar(self,delta_ms,plataformas,objetos,objetos_animados,muros,botínes,interruptores,puerta_final,enemigos,corazones):
        self.hacer_movimiento(delta_ms,plataformas,objetos)
        self.hacer_animaciones(delta_ms)
        self.hacer_colisiones(delta_ms,botínes,objetos_animados,interruptores,puerta_final,muros,enemigos,corazones)
        self.actualizar_invensible(delta_ms)

    def renderizar(self,pantalla):
        if self.vidas > 0:
            if(DEBUG):
                pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_cabeza)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_derecha)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_izquierda)
            
            self.imagen = self.animacion[self.frame]
            pantalla.blit(self.imagen,self.rect)

    def eventos(self,delta_ms,teclas,eventos,municiones):
        self.tiempo_transcurrido += delta_ms

        for evento in eventos:
            if evento.type == pygame.QUIT: # Salir
                pygame.quit()
                sys.exit() 
                    
            if evento.type == pygame.KEYDOWN: # Apretar alguna tecla
                if evento.key == pygame.K_SPACE: # Saltar
                    self.saltar()
            
                if evento.key == pygame.K_s: # Saltar
                    self.disparar(True,municiones)

                if evento.key == pygame.K_a: # Saltar
                    self.atacar()

            if evento.type == pygame.KEYUP: # Dejar de apretar alguna tecla
                if evento.key == pygame.K_RIGHT and evento.key == pygame.K_LEFT and evento.key == pygame.K_SPACE: # Quedarse quieto
                    self.parar()
            
                if evento.key == pygame.K_SPACE: # Saltar
                    self.saltar(False)
                
                if evento.key == pygame.K_s: # Saltar
                    self.disparar(False)
                
                if evento.key == pygame.K_a: # Saltar
                    self.atacar(False)


                
        
        if(teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT]):
            self.caminar(IZQUIERDA)

        if(not teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT]):
            self.caminar(DERECHA)

        if(teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()  
        
        if(not teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()
           
                  
        # if(keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
        #     self.melee()

        # if(not keys[pygame.K_a]):
        #     self.melee(False) 

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





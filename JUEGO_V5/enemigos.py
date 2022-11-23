import pygame
from auxiliar import Auxiliar
from configuraciones import *
from balas import Bala

class Enemigo:
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0):

        self.direccion = DERECHA
        self.parado = {}
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,11,True,scale=0.8)[:402]
        self.parado[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,11,scale=0.8)[:402]

        self.caminando = {}
        self.caminando[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,True,scale=0.8)
        self.caminando[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,scale=0.8)

        self.vidas = 3
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.mover = 0
        self.gravedad = gravedad
        self.velocidad_movimiento = velocidad_movimiento
        self.animacion = self.caminando[self.direccion]
        self.imagen = self.animacion[self.frame]

        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/2,self.rect.height-20)

        self.rectangulo_pies = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_pies.height = ALTURA_PIES
        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES

        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms

        self.patrulla = patrulla
        self.mover_izquierda = True
        self.vivo = True

        self.comienzo_patrulla = self.rect.centerx
        
    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x

    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y

    def verificar_plataforma(self, plataformas):
        self.sobre_plataforma = False
        for plataforma in plataformas:
            if self.rectangulo_pies.colliderect(plataforma.rectangulo_pies):
                self.sobre_plataforma = True
                break

    def aplicar_gravedad(self):
        if not self.sobre_plataforma:
            self.mover_y = self.gravedad
        else:
            self.mover_y = 0

    def hacer_movimiento(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.verificar_plataforma(plataform_list)
            self.aplicar_gravedad()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)

    def hacer_animacion(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def actualizar_vida(self,balas):
        for bala in balas:
            if bala.rectangulo_colision.colliderect(self.rectangulo_colision):
                balas.remove(bala)
                self.vidas -= 1

        if self.vidas < 1:
            self.vivo = False

    def renderizar(self,pantalla):
        if self.vidas > 0:
            if DEBUG:
                pygame.draw.rect(pantalla,(255,0,0),self.rectangulo_colision)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
            self.imagen = self.animacion[self.frame]
            pantalla.blit(self.imagen,self.rect)

    def actualizar(self,pantalla,delta_ms,plataformas,bullets):
        self.hacer_movimiento(delta_ms,plataformas)
        self.hacer_animacion(delta_ms)
        self.actualizar_vida(bullets)
        self.renderizar(pantalla)

class Enemigo_Melee(Enemigo):
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0):
        super().__init__(x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla)

    def patrullar(self):
        if self.vidas > 0:
            if self.rect.x >= self.comienzo_patrulla - self.patrulla and self.mover_izquierda:
                self.mover_x = -self.velocidad_movimiento
                self.animacion = self.caminando[IZQUIERDA]
            elif self.rect.x <= self.comienzo_patrulla + self.patrulla:
                self.mover_izquierda = False
                self.mover_x = self.velocidad_movimiento
                self.animacion = self.caminando[DERECHA]
            else:
                self.mover_izquierda = True

    def hacer_movimiento(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.verificar_plataforma(plataform_list)
            self.aplicar_gravedad()
            self.patrullar()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)

class Enemigo_Distancia(Enemigo):
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0):
        super().__init__(x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla)

        self.rectangulo_vision = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_vision.centery = y + 75
        self.rectangulo_vision.height = ALTURA_PIES * 3
        self.rectangulo_vision.width = 400

        self.animacion = self.parado[DERECHA]

        self.municiones = []
        self.disparo_cooldown = 0
        
    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_vision.x += delta_x

    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_vision.y += delta_y    

    def disparar(self,shoot=True):
        '''
        Este metodo se encarga del disparo del personaje, creardo objetos balas y guardandolo en una lista

        Parametros: Recibe un booleano para saber si el personaje tiene que disparar o no, tambien recibe una lista de municiones que se remueven si se gastan las balas
        '''
        self.esta_disparando = False
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0:
                self.disparo_cooldown = 40
                bala = Bala(self.rectangulo_colision.centerx + (0.6 * self.rectangulo_colision.size[0] * self.direccion),self.rectangulo_colision.centery-20,frame_rate_ms=20,direccion=self.direccion,velocidad_disparo=4)
                self.municiones.append(bala)

    def actualizar_bala(self,delta_ms,pantalla):
        '''
        Este metodo se encarga de actualizar las balas y dibujarlas en pantalla, tambien verifica si estas impactaron con el entorno o no
        '''
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.actualizar(delta_ms,pantalla)
            if bala.impacto:
                self.municiones.remove(bala)

    def renderizar(self,pantalla):
        if self.vivo:
            if DEBUG:
                pygame.draw.rect(pantalla,(255,0,0),self.rectangulo_colision)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
                pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_vision)
            self.imagen = self.animacion[self.frame]
            pantalla.blit(self.imagen,self.rect)

    def hacer_movimiento(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.verificar_plataforma(plataform_list)
            self.aplicar_gravedad()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)

    def hacer_colision(self, pos_xy):
        self.disparar(False)
        if self.rectangulo_vision.colliderect(pos_xy):
            self.disparar(True)
        for bala in self.municiones:
            if bala.rectangulo_colision.colliderect(pos_xy):
                self.municiones.remove(bala)
            
    def actualizar(self,pantalla,delta_ms,plataformas,balas,pos_xy):
        self.hacer_movimiento(delta_ms,plataformas)
        self.hacer_animacion(delta_ms)
        self.hacer_colision(pos_xy)
        self.actualizar_vida(balas)
        self.actualizar_bala(delta_ms,pantalla)
        self.renderizar(pantalla)



        




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
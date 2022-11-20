import pygame
from auxiliar import Auxiliar
from configuraciones import *

class Enemigo:
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,pasos):

        self.direccion = DERECHA
        self.parado = {}
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,9,True,scale=0.8)
        self.parado[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,9,scale=0.8)

        self.caminando = {}
        self.caminando[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,scale=0.8)
        self.caminando[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,True,scale=0.8)

        self.vidas = 3
        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.mover = 0
        self.gravedad = gravedad
        self.pasos = pasos
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

        #MOVIMIENTO DE ENEMIGO
        if self.vidas > 0:
            if(self.mover <= self.pasos):
                self.mover_x = -self.velocidad_movimiento
                self.animacion = self.caminando[DERECHA]
                self.mover += 1
            elif(self.mover <= self.pasos*2):
                self.mover_x = self.velocidad_movimiento
                self.animacion = self.caminando[IZQUIERDA]
                self.mover += 1
            else:
                self.mover = 0
        
    def hacer_animacion(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def hacer_colision(self,bullets):
        for bullet in bullets:
            if bullet.rectangulo_colision.colliderect(self.rectangulo_colision):
                bullets.remove(bullet)
                self.vidas -= 1

    def actualizar(self,delta_ms,plataformas,bullets):
        self.hacer_movimiento(delta_ms,plataformas)
        self.hacer_animacion(delta_ms)
        self.hacer_colision(bullets)

    def renderizar(self,screen):
        if self.vidas > 0:
            if DEBUG:
                pygame.draw.rect(screen,(255,0,0),self.rectangulo_colision)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.rectangulo_pies)
            self.imagen = self.animacion[self.frame]
            screen.blit(self.imagen,self.rect)

    
        




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
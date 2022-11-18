from aux_constantes import *
from aux_frames import Auxiliar
from class_padre import GrupoDisparosX
import pygame

class Jugador:
    def __init__(self, pos_x, pos_y, speed_walk) -> None:

        self.direccion = DERECHA
        self.stay = {}
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2)[:51]
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2,True)[:51]
        
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1)[:12]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1,True)[:12]

        self.jump = {}
        self.jump[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[:23]
        self.jump[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[:23]

        self.fall = {}
        self.fall[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[22:28]
        self.fall[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[22:28]
        
        
        self.animacion = self.stay[self.direccion]
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.rect_pies = pygame.Rect(self.rect.x + self.rect.w/3, self.rect.y + self.rect.h -10, self.rect.w/3, 5)
        self.move_x = 0
        self.move_y = 0

        self.speed_walk = {}
        self.speed_walk[DERECHA] = speed_walk
        self.speed_walk[IZQUIERDA] = -speed_walk

        self.sobre_plataforma = True
        self.caminando = False
        self.saltando = False
        self.cayendo = False

        self.speed_jump = 10
        self.gravedad = 10
        self.inicio_salto = self.rect_pies.y


        self.speed_shoot = {}
        self.speed_shoot[DERECHA] = 20
        self.speed_shoot[IZQUIERDA] = -20
        self.orb = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\disparo_animacion.png",16,2)[:31]
        self.municion = 30
        self.proyectiles = GrupoDisparosX()


        self.invulnerable = False
        self.golpeado = False
        self.hitted = {}
        self.hitted[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1)[:13]
        self.hitted[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1, True)[:13]
        self.tiempo_invulnerabilidad = 0
        self.timer = 0

        self.vida = 100
        self.vivo = True

    def mover(self,direccion):
        if not self.golpeado:
            self.direccion = direccion
            self.caminando = True
            self.move_x = self.speed_walk[self.direccion]
            
            
    def detener(self):
        if not self.golpeado:
            self.caminando = False
            self.move_x = 0


    def saltar(self, saltar):
        if not self.golpeado:
            if saltar:
                if self.sobre_plataforma:
                    self.saltando = True
                    self.move_x = 0
                    self.move_y = -self.speed_jump
                    self.inicio_salto = self.rect_pies.y
            else:
                self.saltando = False


    def limitar_salto(self):
        if self.rect_pies.y < self.inicio_salto - 150:
            self.saltando = False


    def verificar_plataforma(self, plataformas):
        if not self.saltando and not self.golpeado:
            self.sobre_plataforma = False
            for plataforma in plataformas:
                if self.rect_pies.colliderect(plataforma.rect_piso):

                    if self.caminando:
                        self.move_x = self.speed_walk[self.direccion] + plataforma.move_x
                    else:
                        self.move_x = plataforma.move_x
                    self.sobre_plataforma = True
                    break
            


    def aplicar_gravedad(self):
        if not self.golpeado and not self.saltando:
            if not self.sobre_plataforma:
                self.move_y = self.gravedad
                self.cayendo = True
            else:
                self.move_y = 0
                self.cayendo = False


    def disparar(self):
        if self.municion > 0 and not self.golpeado:
            self.proyectiles.agregar_disparo(self.rect.centerx, self.rect.centery, self.speed_shoot[self.direccion], 0, 0, 30, 30, self.orb)
            self.municion -= 1


    def recibir_golpe(self):
        if not self.invulnerable:
            self.golpeado = True
            self.invulnerable = True
            self.saltando = False
            
            self.move_x = -self.speed_walk[self.direccion] / 2
            self.move_y = -2
            
    def modificar_vida(self,modificacion):
        self.vida += modificacion
        if self.vida == 0:
            self.vivo = False


    def actualizar_invulnerabilidad(self, delta_ms):
        if self.invulnerable:
            self.tiempo_invulnerabilidad += delta_ms
            if self.tiempo_invulnerabilidad > 1500:
                self.tiempo_invulnerabilidad = 0
                self.invulnerable = False


    def verificar_colision_enemigos(self,enemigos):
        if self.rect.collidelist(enemigos) != -1:
            self.recibir_golpe()



    def animaciones(self):
        if not self.golpeado:
            if self.saltando:
                self.cambiar_animacion(self.jump)
            else:
                if self.cayendo:
                    self.cambiar_animacion(self.fall)
                else:
                    if self.caminando:
                        self.cambiar_animacion(self.walk)
                    else:
                        self.cambiar_animacion(self.stay)
        else:
            self.cambiar_animacion(self.hitted)


    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]

         
    def actualizar_posicion(self):
    
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pies.x += self.move_x
        self.rect_pies.y += self.move_y


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else:
            self.frame = 0
            
            if self.golpeado:
                self.golpeado = False
                self.detener()
            else:
                if self.cayendo:
                    self.frame = len(self.animacion) - 1

    
    def draw(self,screen):
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)
        pygame.draw.rect(screen, C_BLUE, self.rect_pies)

    

    def actualizar_player(self, screen, plataformas, objetivos, delta_ms):
        self.timer += delta_ms

        if self.timer > 30:
            self.timer = 0
            self.verificar_plataforma(plataformas)
            self.aplicar_gravedad()
            self.actualizar_posicion()
            self.animaciones()
            self.updatear_frames()
            self.proyectiles.actualizar_disparos(screen, objetivos)
            self.verificar_colision_enemigos(objetivos)
            self.actualizar_invulnerabilidad(delta_ms)
            self.draw(screen)
        



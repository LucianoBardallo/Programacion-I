import pygame
from configuraciones import *
from auxiliar import Auxiliar
from balas import Bala
import sys

class Jugador:
    def __init__(self,x,y,velocidad_movimiento,gravedad,fuerza_salto,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,altura_salto,p_scale=1) -> None:
        
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
        self.vivo = True
        self.ganar = False

        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.move_rate_ms = move_rate_ms
        self.comienzo_salto = self.rectangulo_pies.y
        self.altura_salto = altura_salto

        self.tiempo_activado = 0
        self.tiempo_recolectado = 0
        self.tiempo_looteado = 0
        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_disparo = 0
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_movimiento = 0
        self.tiempo_inmune = 0

        self.municiones = []
        self.disparo_cooldown = 0
        self.municion = 15


    #ACCIONES
    def caminar(self,direccion:int): 
        '''
        Este metodo se encarga de darle un valor al movimiento de la X del personaje dependiendo de la direccion a donde este mirando

        Parametros: Recibe la direccion de a donde mira el personaje
        '''
        if self.vivo:
            self.direccion = direccion
            self.mover_x = self.velocidad_movimiento[self.direccion]
            self.esta_caminando = True
            if self.esta_saltando:
                self.mover_x = self.velocidad_movimiento[self.direccion] // 2
         
    def parar(self):
        '''
        Este metodo se encarga de hacer que el personaje se quede parado dandole como valor 0 al movimiento de la x
        '''
        self.esta_caminando = False
        self.mover_x = 0

    def disparar(self,shoot=True,municiones=[]):
        '''
        Este metodo se encarga del disparo del personaje, creardo objetos balas y guardandolo en una lista

        Parametros: Recibe un booleano para saber si el personaje tiene que disparar o no, tambien recibe una lista de municiones que se remueven si se gastan las balas
        '''
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0 and self.municion > 0:
                self.disparo_cooldown = 40
                bala = Bala(self.rectangulo_colision.centerx + (0.6 * self.rectangulo_colision.size[0] * self.direccion),self.rectangulo_colision.centery-20,frame_rate_ms=20,direccion=self.direccion,velocidad_disparo=8)
                self.municiones.append(bala)
                self.municion -= 1
                municiones.remove(municiones[-1])
        else:
            self.esta_disparando = False
    
    def atacar(self,melee=True):
        '''
        Este metodo se encarga del ataque melee del personaje
        '''
        self.esta_pegando = melee
        if melee:
            self.esta_pegando = True
        
    def saltar(self, jump=True):
        '''
        Este metodo se encarga del salto de personaje, dandole un valor al movimiento de Y del personaje, y tomando de donde comenzo el salto

        Parametros: Recibe como parametro un bool para saber si el personaje puede saltar o no.
        '''
        if jump:
            if self.sobre_plataforma:
                self.esta_saltando = True
                self.mover_x = 0
                self.mover_y = -self.fuerza_salto
                self.comienzo_salto = self.rectangulo_pies.y
        else:
            self.esta_saltando = False

    #VERIFICACIONES     
    def limitar_salto(self):
        '''
        Este metodo se encarga de limitar el salto del personaje, para que no salte infinitamente
        '''
        if self.rectangulo_pies.y < self.comienzo_salto - 150:
            self.esta_saltando = False


    def verificar_plataforma(self, plataformas, objetos):
        '''
        Este metodo se encarga de verificar el personaje esta sobre una plataforma comprobando la colision de los pies del jugador con la colision de la plataforma

        Parametros: Recibe como parametro una lista de plataformas y objetos
        '''
        if not self.esta_saltando:
            self.sobre_plataforma = False
            for plataform in plataformas:
                if self.rectangulo_pies.colliderect(plataform.rectangulo_pies):
                    self.sobre_plataforma = True
                    break
            for object in objetos:
                if(self.rectangulo_pies.colliderect(object.rectangulo_pies)):
                    self.sobre_plataforma = True
                    break 
            

    def aplicar_gravedad(self):
        '''
        Este metodo se encarga de aplicarle gravedad al personaje cuando no esta sobre una superficie o llego al limite del salto
        '''
        if not self.esta_saltando:
            if not self.sobre_plataforma:
                self.mover_y = self.gravedad
                self.esta_cayendo = True
            else:
                self.mover_y = 0
                self.esta_cayendo = False

    def actualizar_invensible(self, delta_ms):
        '''
        Es metodo se encarga actualizar la invensibilidad del personaje una vez es golpeado por un enemigo o bala
        '''
        if self.invensible:
            self.tiempo_inmune += delta_ms
            if self.tiempo_inmune > 1500:
                self.tiempo_inmune = 0
                self.invensible = False

    
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

    def comprobar_vidas(self):
        if self.vidas < 1:
            self.vivo = False
    
    #MOVIMIENTO
    def cambiar_x(self,delta_x:int):
        '''
        Este metodo se encarga de mover todos los rectangulos en X del personaje, permitendo darle movimiento al jugador

        Parametros: Recibe un entero que representa el move_x del personaje
        '''
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_cabeza.x += delta_x
        self.rectangulo_derecha.x += delta_x
        self.rectangulo_izquierda.x += delta_x


    def cambiar_y(self,delta_y):
        '''
        Este metodo se encarga de mover todos los rectangulos en Y del personaje, permitendo darle movimiento al jugador

        Parametros: Recibe un entero que representa el move_y del personaje
        '''
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_cabeza.y += delta_y
        self.rectangulo_derecha.y += delta_y
        self.rectangulo_izquierda.y += delta_y

    #ANIMACIONES
    def animaciones(self):
        '''
        Este metodo se encarga de cambiar la animacion actual del personaje
        '''
        if self.vivo:
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
        else:
            self.cambiar_animacion(self.muriendo)


    def cambiar_animacion(self, animation):
        '''
        Este metodo se encarga de resetear la animacion del personaje dependiendo si es distinta a la anterior y le da un nuevo valor
        '''
        if self.animacion != animation[DERECHA] and self.animacion != animation[IZQUIERDA]:
            self.frame = 0
        self.animacion = animation[self.direccion]


    def actualizar_frames(self,delta_ms):
        '''
        Este metodo se encarga de actualizar los frames de una animacion dependiendo del tiempo pasado por parametro
        '''
        self.tiempo_transcurrido_animacion += delta_ms
        if self.esta_saltando or self.esta_cayendo:
            if(self.tiempo_transcurrido_animacion >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animacion = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0
                    if self.esta_cayendo:
                        self.frame = len(self.animacion) - 1   
                 
        else:
            if(self.tiempo_transcurrido_animacion >= self.frame_rate_ms):
                self.tiempo_transcurrido_animacion = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0
                    if self.vivo == False:
                        self.frame = len(self.animacion) - 1 

    def renderizar(self,pantalla):
        '''
        Este metodo se encarga de dibujar el personaje en la pantalla

        Parametros: Recibe como parametro la pantalla donde se van a fundir las imaganes
        '''
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_cabeza)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_derecha)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_izquierda)
        
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def eventos(self,teclas,eventos,municiones):
        #EVENTOS
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

        #TECLAS PRESIONADAS
        if(teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT]):
            self.caminar(IZQUIERDA)

        if(not teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT]):
            self.caminar(DERECHA)

        if(teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()  
        
        if(not teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()

    #COLISIONES
    def hacer_colisiones(self,delta_ms:int,botínes:list,objetos:list,interruptores:list,puerta_final:list,muros:list,enemigos:list,corazones:list,enemigos_rango:list):
        '''
        Este metodo se encarga de verificar todas las colisiones del personaje con el entorno del juego
        '''
        for muro in muros:
            if muro.rectangulo_colision.colliderect(self.rectangulo_derecha):
                self.cambiar_x(-1)
            elif muro.rectangulo_colision.colliderect(self.rectangulo_izquierda):
                self.cambiar_x(1)
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
                    if self.vidas >= 0:
                        corazones.remove(corazones[-1])
        
        for enemigo in enemigos_rango:
            if enemigo.rectangulo_colision.colliderect(self.rectangulo_colision):
                if not self.invensible:
                    self.vidas -= 1
                    self.invensible = True
                    if self.vidas >= 0:
                        corazones.remove(corazones[-1])
            for bala in enemigo.municiones:
                if bala.rectangulo_colision.colliderect(self.rectangulo_colision):
                    if not self.invensible:
                        self.vidas -= 1
                        self.invensible = True
                        if self.vidas >= 0:
                            corazones.remove(corazones[-1])


        for botín in botínes:
            if botín.rectangulo_colision.colliderect(self.rectangulo_colision):
                botín.recolectado = True
                self.puntuacion += 50
                botínes.remove(botín)
                    
        for objeto in objetos:
            objeto.activado = False
            if objeto.rectangulo_colision.colliderect(self.rectangulo_colision):
                objeto.activado = True
                
        for interruptor in interruptores:
            if interruptor.rectangulo_colision.colliderect(self.rectangulo_colision):
                
                interruptor.activado = True
                interruptor.desbloqueado = True
                self.puede_ganar = True
            else:
                if interruptor.activado:
                    self.tiempo_activado += delta_ms
                if(self.tiempo_activado >= 10000):
                    interruptor.activado = False
                    interruptor.desbloqueado = False
                    self.puede_ganar = False
                    self.tiempo_activado = 0

        for puerta in puerta_final:
            puerta.desbloqueado = self.puede_ganar
            puerta.activado = False
            if puerta.rectangulo_colision.colliderect(self.rectangulo_colision) and self.puede_ganar:
                puerta.activado = True
                self.ganar = True
                

    #MOVIMIENTO
    def hacer_movimiento(self,delta_ms,plataformas,objetos):
        '''
        Este metodo se encarga de agrupar todos los metodos que esten dandole movimiento al personaje
        '''
        self.tiempo_transcurrido_movimiento += delta_ms
        if(self.tiempo_transcurrido_movimiento >= self.move_rate_ms):
            self.tiempo_transcurrido_movimiento = 0

            self.verificar_plataforma(plataformas,objetos)
            self.aplicar_gravedad()
            self.cambiar_y(self.mover_y)
            if self.vivo:
                self.limitar_salto()
                self.cambiar_x(self.mover_x)
                

    #ANIMACIONES
    def hacer_animaciones(self,delta_ms):
        '''
        Este metodo se encarga de agrupar todos los metodos que esten dandole animacion al personaje
        '''
        self.animaciones()
        self.actualizar_frames(delta_ms)      

    #ACTUALIZACION PRINCIPAL
    def actualizar(self,delta_ms,pantalla,teclas,eventos,municiones,plataformas,objetos,objetos_animados,muros,botínes,interruptores,puerta_final,enemigos,corazones,enemigos_rango):
        '''
        Este metodo es el principal del personaje, donde se agrupan todos los metodos usados anteriormente para hacer que el personaje funcione de manera correcta
        '''
        self.eventos(teclas,eventos,municiones)
        if not self.ganar:
            self.comprobar_vidas()
            self.hacer_movimiento(delta_ms,plataformas,objetos)
            self.hacer_animaciones(delta_ms)
            self.hacer_colisiones(delta_ms,botínes,objetos_animados,interruptores,puerta_final,muros,enemigos,corazones,enemigos_rango)
            self.actualizar_invensible(delta_ms)
            self.actualizar_bala(delta_ms,pantalla)
            self.renderizar(pantalla)
        

    



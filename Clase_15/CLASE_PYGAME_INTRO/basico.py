import pygame
import colores
import dona
import personaje
import fondo
import obstaculos

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

# AGREGAR MUSICA
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load(r"Clase_15\CLASE_PYGAME_INTRO\fondo.mp3")
pygame.mixer.music.play(-1)
sonido_masticar = pygame.mixer.Sound(r"Clase_15\CLASE_PYGAME_INTRO\masticar.mp3")
sonido_masticar.set_volume(0.5)
sonido_ouch = pygame.mixer.Sound(r"Clase_15\CLASE_PYGAME_INTRO\ouch.mp3")
sonido_ouch.set_volume(0.5)
sonido_duff = pygame.mixer.Sound(r"Clase_15\CLASE_PYGAME_INTRO\iuju.mp3")
sonido_duff.set_volume(0.5)

#Cargar imagenes
player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200)
lista_donas = dona.crear_lista_donas(50)
pantalla_fondo = fondo.crear_fondo(800,800)
lista_obstaculos = obstaculos.crear_lista_obstaculos(10)
lista_cerveza = dona.crear_lista_cerveza(1)


running = True
i = 0
while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)
                dona.update(lista_cerveza)
                obstaculos.update(lista_obstaculos)
                if player["vida"] <= 0:
                    running = False

    ventana_ppal.blit(pantalla_fondo["surface"], [0,i])
    ventana_ppal.blit(pantalla_fondo["surface"], [0, -ALTO_VENTANA+i])
    if i == ALTO_VENTANA:
        i = 0
    i += 1

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT] :
        personaje.update(player,-10)
    if lista_teclas[pygame.K_RIGHT] :
        personaje.update(player,10)

    obstaculos.actualizar_pantalla(lista_obstaculos,player,ventana_ppal,sonido_ouch)
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_donas(lista_donas,player,ventana_ppal,sonido_masticar)
    dona.actualizar_cerveza(lista_cerveza,player,ventana_ppal,sonido_duff)

    pygame.display.flip()
pygame.quit()
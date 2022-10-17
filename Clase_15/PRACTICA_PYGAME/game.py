import pygame
import colores
import elementos
import personaje
import background

ANCHO_VENTANA = 1200
LARGO_VENTANA = 600

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,LARGO_VENTANA))
pygame.display.set_caption("VOLVER AL FUTURO")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

# CREANDO IMAGENES
fondo = background.crear_fondo(1200,600)
pila = elementos.crear_pila(1000,500,40,40)
player = personaje.crear_personaje(10,350,250,225)
logo = background.crear_decoracion(1100,550,100,150)

lista_pilas = elementos.crear_lista_pila(10)

posicion = 0

# AGREGAR MUSICA
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load(r"Clase_15\PRACTICA_PYGAME\BTF.wav")
pygame.mixer.music.play(-1)

# SISTEMA PRINCIPAL DEL JUEGO
running = True
while (running):
    # CREAR UN TEXTO
    fuente = pygame.font.SysFont("Arial",30)
    player["distancia"] = player["distancia"] + 1
    texto = fuente.render("DISTANCIA: {0} M".format(player["distancia"]),True,colores.BLANCO)
    if player["distancia"] >= 1000:
        texto = fuente.render("DISTANCIA: {0} KM".format(round(player["distancia"] / 1000)),True,colores.BLANCO)
        player["distancia"] += 1
    else:
        texto = fuente.render("DISTANCIA: {0} M".format(player["distancia"]),True,colores.BLANCO)
        player["distancia"] += 1
        

    lista_eventos = pygame.event.get()
    # EVENTOS
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                elementos.update(lista_pilas)

    lista_teclas = pygame.key.get_pressed()

    if(lista_teclas[pygame.K_UP]):
        personaje.update(player,-5)
    if(lista_teclas[pygame.K_DOWN]):
        personaje.update(player,5)
    
    ventana_ppal.blit(fondo["surface"],(posicion,0))
    ventana_ppal.blit(fondo["surface"],(ANCHO_VENTANA + posicion,0))
    ventana_ppal.blit(logo["surface"],(1050,0))
    ventana_ppal.blit(texto,(20,10))

    elementos.actualizar_pantalla(lista_pilas,player,ventana_ppal)
    personaje.actualizar_pantalla(player,ventana_ppal)

    if (posicion == -ANCHO_VENTANA):
        ventana_ppal.blit(fondo["surface"],(ANCHO_VENTANA + posicion,0))
        posicion = 0
    posicion -= 15
    pygame.display.flip()
pygame.quit()
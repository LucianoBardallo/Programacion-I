import pygame
import colores
import elementos
import personaje
import background
import obstaculos

ANCHO_VENTANA = 1200
LARGO_VENTANA = 600

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,LARGO_VENTANA))
pygame.display.set_caption("VOLVER AL FUTURO")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,50)

timer2 = pygame.USEREVENT + 1
pygame.time.set_timer(timer2,500)

# CREANDO IMAGENES
fondo = background.crear_fondo(1200,600)
pila = elementos.crear_pila(1000,500,40,40)
player = personaje.crear_personaje(10,350,250,225)
logo = background.crear_decoracion(1100,550,100,150)

lista_pilas = elementos.crear_lista_pila(10)
lista_obstaculos = obstaculos.crear_lista_obstaculos(4)
lista_piedras = obstaculos.crear_lista_piedra(1)

posicion = 0

# AGREGAR MUSICA
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load(r"Clase_15\PRACTICA_PYGAME\BTF.wav")
pygame.mixer.music.play(-1)
sonido_choque = pygame.mixer.Sound(r"Clase_15\PRACTICA_PYGAME\Choque.wav")
sonido_choque.set_volume(0.1)
sonido_energia = pygame.mixer.Sound(r"Clase_15\PRACTICA_PYGAME\Energia.wav")
sonido_energia.set_volume(0.1)
sonido_crash = pygame.mixer.Sound(r"Clase_15\PRACTICA_PYGAME\autocrash.wav")
sonido_crash.set_volume(0.1)


# SISTEMA PRINCIPAL DEL JUEGO
running = True
game_over = False
while (running):
    # TEXTOS
    fuente = pygame.font.SysFont("Arial",30)
    texto = fuente.render("DISTANCIA: {0} M".format(round(player["distancia"])),True,colores.BLANCO)
    vida = fuente.render("ENERGIA: {0}".format(round(player["vida"])),True,colores.BLANCO)   
    if player["distancia"] >= 1000:
        texto = fuente.render("DISTANCIA: {0} KM".format(round(player["distancia"] / 1000)),True,colores.BLANCO)
        player["distancia"] += 0.5
    else:
        texto = fuente.render("DISTANCIA: {0} M".format(round(player["distancia"])),True,colores.BLANCO)
        player["distancia"] += 0.5

    lista_eventos = pygame.event.get()
    # EVENTOS
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False    

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                player["vida"] = player["vida"] - 0.5
                elementos.update(lista_pilas)
                obstaculos.update(lista_obstaculos)
                obstaculos.update(lista_piedras)
                if player["vida"] <= 0:
                    game_over = True

    lista_teclas = pygame.key.get_pressed()

    if(lista_teclas[pygame.K_UP]):
        personaje.update(player,-5)
    if(lista_teclas[pygame.K_DOWN]):
        personaje.update(player,5)
    
    ventana_ppal.blit(fondo["surface"],(posicion,0))
    ventana_ppal.blit(fondo["surface"],(ANCHO_VENTANA + posicion,0))
    ventana_ppal.blit(logo["surface"],(1050,0))
    ventana_ppal.blit(texto,(20,10))
    ventana_ppal.blit(vida,(20,40))

    elementos.actualizar_pantalla(lista_pilas,player,ventana_ppal,sonido_energia)
    obstaculos.actualizar_pantalla2(lista_piedras,player,ventana_ppal,sonido_crash)
    obstaculos.actualizar_pantalla(lista_obstaculos,player,ventana_ppal,sonido_choque)
    personaje.actualizar_pantalla(player,ventana_ppal)
    
    if (posicion == -ANCHO_VENTANA):
        ventana_ppal.blit(fondo["surface"],(ANCHO_VENTANA + posicion,0))
        posicion = 0
    posicion -= 15

    if game_over:
        final = fuente.render("GAME OVER",True,colores.ROJO)
        #final2 = fuente.render("PUNTUACION FINAL: {0}".format(round(player["distancia"])),True,colores.ROJO)
        ventana_ppal.blit(final,(500,280))
        #ventana_ppal.blit(final2,(420,310))

    pygame.display.flip()
pygame.quit()

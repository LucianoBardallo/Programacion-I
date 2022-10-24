import pygame, tablero, fondo, copy, tarjeta
from constantes import *

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('The Simpsons Memotest')

#TIMER
tick = pygame.USEREVENT
pygame.time.set_timer(tick,3000)

#TABLERO
tablero_juego = tablero.init()
lista_tarjetas = tablero_juego["l_tarjetas"]
fondo_tablero = fondo.crear_fondo(r"Clase_16\Homero_Memotest\recursos\fondo.jpg",ANCHO_PANTALLA,ALTO_PANTALLA)

#MUSICA
pygame.mixer.init()
tablero.reproducir_musica_principal(r"Clase_16\Homero_Memotest\recursos\fondo.wav",0.1)

#INICIALIZO VARIABLES
posicion = 0
ocultar = True
tarjeta_uno = None
tarjeta_dos = None
bandera_final = True
game_over = True
una_pasada = True

clock_fps = pygame.time.Clock()

running = True
while running:
    #SETEAR FPS
    tiempo = clock_fps.tick(60)
    # SE VERIFICA SI EEL USUARIO CERRO LA VENTANA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # VERIFICA SI EL USUARIO APRETO EL MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN :
            carta = tablero.colicion(tablero_juego,event.pos)
            if carta["visible"] or carta["descubierto"]:
                continue
            #VERIFICA SI PUEDE JUGAR
            if tarjeta.cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) < 2:
                puede_jugar = True
            else:
                puede_jugar = False
            if puede_jugar:
            # TOMA PRIMER TARJETA
                if (tarjeta_uno == None or tarjeta.cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas) == 0):
                    tarjeta_uno = tablero.tomar_primer_tarjeta(carta)
                else:
                    #TOMA SEGUNDA TARJETA
                    tarjeta_dos = tablero.tomar_segunda_tarjeta(carta)
                    # COMPARA AMBAS TARJETAS
                    if tablero.comparar_tarjetas(tablero_juego,tarjeta_uno,tarjeta_dos):
                        tarjeta_uno = None
                        tarjeta_dos = None
                    # ERROR EN CASO DE NO SE IGUALES
                    else:
                        tablero.reproductor_sonidos(r"Clase_16\Homero_Memotest\recursos\equivocado.wav",0.1)
                        print("NO COINCIDE\n")
                        tarjeta_uno = None
        
    if game_over:
        #PANTALLA DE FONDO
        pantalla_juego.blit(fondo_tablero["surface"], [0,0])

        #OCULTA TODAS LAS IMAGENESS
        if ocultar:
            tablero.ocultar_imagenes(tablero_juego)
            ocultar = False   
        
        #REFRESH DE IMAGENES Y CONDICIONES
        tablero.update(tablero_juego)          
        tablero.render(tablero_juego,pantalla_juego)

    #EVALUA SI TERMINO EL JUEGO
    if tablero.comprobar_final(tablero_juego) and bandera_final:
        game_over = False
        fondo_win = fondo.crear_fondo(r"Clase_16\Homero_Memotest\recursos\win.jpg",ANCHO_PANTALLA,ALTO_PANTALLA)
        pantalla_juego.blit(fondo_win["surface"], [0,0])
        if una_pasada:
            pygame.mixer.music.stop()
            sonido_win = pygame.mixer.Sound(r"Clase_16\Homero_Memotest\recursos\ganador.wav")
            sonido_win.set_volume(0.1)
            pygame.mixer.Sound.play(sonido_win)
            una_pasada = False
        #TEXTO
        font = pygame.font.SysFont("Arial Narrow", 150)
        text = font.render("JUEGO COMPLETADO", True, (0, 0, 0))
        pantalla_juego.blit(text,(100,ALTO_PANTALLA/2+200))
    #MUESTRA TODOS LOS CAMBIOS
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

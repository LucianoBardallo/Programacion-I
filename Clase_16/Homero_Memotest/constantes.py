# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (206, 206, 206)
AZUL = (30, 136, 229)

#Seteos Juego
CANTIDAD_TARJETAS_H = 4
CANTIDAD_TARJETAS_V = 4
ANCHO_PANTALLA = 1366
ALTO_PANTALLA = 768
ALTO_TEXTO = 50
CANTIDAD_TARJETAS_UNICAS = int((CANTIDAD_TARJETAS_H*CANTIDAD_TARJETAS_V)/2)
ANCHO_TARJETA = int(ANCHO_PANTALLA / CANTIDAD_TARJETAS_H)
ALTO_TARJETA =int( (ALTO_PANTALLA - ALTO_TEXTO)/ CANTIDAD_TARJETAS_V)
PATH_RECURSOS = r"C:\Users\lucia\Documents\Programacion I\Clase_16\Homero_Memotest\recursos\\"

#if CANTIDAD_TARJETAS_H <= 4:
#    ANCHO_PANTALLA = CANTIDAD_TARJETAS_H * 180
#else:
#    ANCHO_PANTALLA = CANTIDAD_TARJETAS_H * 250
#if CANTIDAD_TARJETAS_V <= 4:
#    ALTO_PANTALLA = CANTIDAD_TARJETAS_V * 180
#else:
#    ALTO_PANTALLA = CANTIDAD_TARJETAS_V * 250
import pygame
import player

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista

    def elegir_personaje(jugador):
        if jugador == "ONE":
            player_1 = player.PlayerONE(x = 0, y = 555, speed_walk = 3, gravity = 2, jump_power = 12, frame_rate_ms = 40,frame_rate_jump_ms = 10, move_rate_ms = 20)
        elif jugador == "TWO":
            player_1 = player.PlayerTWO(x = 0, y = 555, speed_walk = 3, gravity = 2, jump_power = 12, frame_rate_ms = 40,frame_rate_jump_ms = 10, move_rate_ms = 20)
        elif jugador == "THREE":
            player_1 = player.PlayerTHREE(x = 0, y = 555, speed_walk = 3, gravity = 2, jump_power = 12, frame_rate_ms = 40,frame_rate_jump_ms = 10, move_rate_ms = 20)
        elif jugador == "FOUR":
            player_1 = player.PlayerFOUR(x = 0, y = 555, speed_walk = 3, gravity = 2, jump_power = 12, frame_rate_ms = 40,frame_rate_jump_ms = 10, move_rate_ms = 20)
        return player_1
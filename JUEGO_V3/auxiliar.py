import pygame
import player
from constantes import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(1,quantity+1):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista

    def elegir_personaje(jugador):
        if jugador == "ONE":
            player_1 = player.PlayerONE(x = 400, y = 0, speed_walk = 8, gravity = 12, jump_power = 12, frame_rate_ms = 20,frame_rate_jump_ms = 10, move_rate_ms = 20, jump_height = 180, p_scale=0.2,interval_time_jump=300)
        elif jugador == "TWO":
            player_1 = player.PlayerTWO(x = 400, y = 0, speed_walk = 8, gravity = 12, jump_power = 12, frame_rate_ms = 20,frame_rate_jump_ms = 10, move_rate_ms = 20, jump_height = 180, p_scale=0.2,interval_time_jump=300)
        elif jugador == "THREE":
            player_1 = player.PlayerTHREE(x = 400, y = 0, speed_walk = 8, gravity = 12, jump_power = 12, frame_rate_ms = 20,frame_rate_jump_ms = 10, move_rate_ms = 20, jump_height = 180, p_scale=0.2,interval_time_jump=300)
        elif jugador == "FOUR":
            player_1 = player.PlayerFOUR(x = 400, y = 0, speed_walk = 8, gravity = 12, jump_power = 12, frame_rate_ms = 20,frame_rate_jump_ms = 10, move_rate_ms = 20, jump_height = 180, p_scale=0.2,interval_time_jump=300)
        return player_1
import pygame
import json
from auxiliar import *
from configuraciones import *
from plataformas import *
from objetos import *
from botínes import *

class Nivel:
    def __init__(self,nivel,delta_ms,jugador):
        self.nivel_data = Auxiliar.cargar_nivel(r"JUEGO_V5\niveles.json",nivel)
        self.mapa = self.nivel_data["mapa"]
        self.objetos = self.nivel_data["objetos"]
        self.botin = self.nivel_data["botín"]
        self.enemigos = self.nivel_data["enemigos"]
        self.tiles = self.crear_mapa()

    def crear_mapa(self):
        tiles = []
        x = 0
        y = 0
        for fila in self.mapa:
            for tile in fila:
                if tile == PLATAFORMA:
                    tiles.append(Plataforma(x,y,ancho=50,alto=50,type=1))
                if tile == MURO:
                    tiles.append(Muro(x,y,ancho=50,alto=50,type=4))
                x += 50
            x = 0
            y += 50
        return tiles

    
        
            


    # def crear_muro(self):
    #     pass
    
    # def crear_objeto(self):
    #     pass

    # def crear_loot(self):
    #     pass
    
    # def crear_obstaculo(self):
    #     pass

    def colisiones(self):
        pass

    def renderizar(self,screen):
        for tile in self.tiles:
            tile.renderizar(screen)

    def actualizar(self):
        pass

    
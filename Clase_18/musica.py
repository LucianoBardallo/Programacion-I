import pygame

class Musica:
    def __init__(self,sonido,volumen):
        self.sonido = sonido
        self.volumen = volumen

    def reproducir_sonidos(sonido,volumen):
        sound = pygame.mixer.Sound(sonido)
        sound.set_volume(volumen)
        pygame.mixer.Sound.play(sound)

    def reproducir_musica_principal(sonido,volumen):
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.load(sonido)
        pygame.mixer.music.play(-1)

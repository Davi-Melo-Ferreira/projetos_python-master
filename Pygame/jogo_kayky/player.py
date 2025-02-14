from valores import largura, altura, tamanho, velocidade, x, y
from meu_erro import parede

import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        pass
    
    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_d] or teclas[K_RIGHT]:
            verify_x = x + velocidade
            if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
                x = verify_x
        if teclas[K_a] or teclas[K_LEFT]:
            verify_x = x - velocidade
            if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
                x = verify_x

        if teclas[K_LSHIFT] or teclas[K_RSHIFT]:
            velocidade = 5
        else:
            velocidade = 2

    def atacar(self):
        pass
    
    def pular(self):
        pass
    
    def mudar_arma(self):
        
        pass
import pygame
from pygame import *
from arrow_knife_jump_protect import tela

class Player:
    def __init__(self, vida, x, y, tamanho, velocidade):
        self.vida = vida
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.velocidade = velocidade

    def criar_sprite(self):
        pygame.draw.rect(tela, (255, 255, 255), (self.x, self.y, self.tamanho, self.tamanho))

    def andar(self):
        tecla = pygame.key.get_pressed()
        if tecla[K_a]:
            self.x -= self.velocidade
        if tecla[K_d]:
            self.x += self.velocidade

jogador = Player(10, 500, 300, 30, 5)
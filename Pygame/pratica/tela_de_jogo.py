import pygame
import os

vertical = 1000
horizontal = 500

tela = pygame.display.set_mode((vertical, horizontal))

rodando = True
while rodando:
    tela.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
pygame.quit()
os.system('cls')
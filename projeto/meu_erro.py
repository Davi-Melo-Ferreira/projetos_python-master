import pygame
import os
from pygame.locals import *

pygame.init()

# definindo tamanho de tela
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))

# Definindo o título da janela
pygame.display.set_caption('Projeto_Teste')

# Definindo objeto player
x, y = 400, 230
tamanho = 30

clock = pygame.time.Clock()

rodando = True
while rodando:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Fecha a tela se clicar no x da janela
            rodando = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        x += 3
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        x -= 3
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        y += 3
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        y -= 3
        
    #                      (R, G,  B )
    pygame.draw.rect(tela, (0, 250, 0), (x, y, tamanho, tamanho))

    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS
os.system('cls')
    
pygame.quit()
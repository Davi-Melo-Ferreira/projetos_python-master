import pygame
import os
from pygame import *
from valores import largura, altura, x, y, velocidade, tamanho
import time

pygame.init()

# definindo tamanho de tela
tela = pygame.display.set_mode((largura, altura))

# Definindo o título da janela
pygame.display.set_caption('Projeto_Teste')

clock = pygame.time.Clock()

while True:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Fecha a tela se clicar no x da janela
            exit()

    teclas = pygame.key.get_pressed()
    if teclas[K_d] or teclas[K_RIGHT]:
        verify_x = x + velocidade
        if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
            x = verify_x
    if teclas[K_a] or teclas[K_LEFT]:
        verify_x = x - velocidade
        if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
            x = verify_x
    if teclas[K_s] or teclas[K_DOWN]:
        verify_y = y + velocidade
        if not pygame.Rect(x, verify_y, tamanho, tamanho).colliderect(parede):
            y = verify_y
    if teclas[K_w] or teclas[K_UP]:
        verify_y = y - velocidade
        if not pygame.Rect(x, verify_y, tamanho, tamanho).colliderect(parede):
            y = verify_y
    if teclas[K_LSHIFT] or teclas[K_RSHIFT]:
        velocidade = 5
    else:
        velocidade = 2
            
    #objeto_player         (R, G,  B )
    player = pygame.draw.rect(tela, (0, 250, 0), (x, y, tamanho, tamanho))
    #objeto_parede
    parede = pygame.draw.rect(tela, (0, 0, 250), (200, 300, tamanho, tamanho))
    
    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS
os.system('cls')

pygame.quit()
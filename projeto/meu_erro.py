import pygame
import os
from pygame.locals import *
from valores import largura, altura, x, y, velocidade, tamanho
pygame.init()

# definindo tamanho de tela
tela = pygame.display.set_mode((largura, altura))

# Definindo o título da janela
pygame.display.set_caption('Projeto_Teste')

clock = pygame.time.Clock()

rodando = True
while rodando:
    tela.fill((0, 0, 0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Fecha a tela se clicar no x da janela
            rodando = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        verify_x = x + velocidade
        if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
            x = verify_x
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        verify_x = x - velocidade
        if not pygame.Rect(verify_x, y, tamanho, tamanho).colliderect(parede):
            x = verify_x
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        verify_y = y + velocidade
        if not pygame.Rect(x, verify_y, tamanho, tamanho).colliderect(parede):
            y = verify_y
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        verify_y = y - velocidade
        if not pygame.Rect(x, verify_y, tamanho, tamanho).colliderect(parede):
            y = verify_y
        
    #objeto_player         (R, G,  B )
    player = pygame.draw.rect(tela, (0, 250, 0), (x, y, tamanho, tamanho))
    #objeto_parede
    parede = pygame.draw.rect(tela, (0, 0, 250), (200, 300, tamanho, tamanho))
    
    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS
os.system('cls')
    
pygame.quit()